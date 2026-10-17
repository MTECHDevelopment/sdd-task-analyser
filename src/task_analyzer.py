from __future__ import annotations

from collections import Counter
from datetime import datetime, timezone
from typing import Any

VALID_STATUSES = {"todo", "in_progress", "done"}
VALID_PRIORITIES = {"low", "medium", "high", "critical"}


def _parse_due_date(raw_due_date: str) -> datetime:
    normalized = raw_due_date.replace("Z", "+00:00")
    due_date = datetime.fromisoformat(normalized)
    if due_date.tzinfo is None:
        return due_date.replace(tzinfo=timezone.utc)
    return due_date.astimezone(timezone.utc)


def analyze_tasks(tasks: list[dict[str, Any]], now: datetime | None = None) -> dict[str, Any]:
    reference_now = now.astimezone(timezone.utc) if now else datetime.now(timezone.utc)

    by_status: Counter[str] = Counter()
    by_priority: Counter[str] = Counter()
    errors: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    risk_overdue = 0

    for index, task in enumerate(tasks):
        if not isinstance(task, dict):
            errors.append({"index": index, "message": "Task inválida: estrutura deve ser objeto."})
            continue

        task_id = task.get("id")
        title = task.get("title")
        status = task.get("status")
        priority = task.get("priority")
        due_date_raw = task.get("due_date")
        owner = task.get("owner")

        task_errors: list[str] = []

        if not isinstance(task_id, str) or not task_id.strip():
            task_errors.append("Campo obrigatório ausente ou inválido: id")
        elif task_id in seen_ids:
            task_errors.append("Identificador duplicado: id")
        else:
            seen_ids.add(task_id)

        if not isinstance(title, str) or not title.strip():
            task_errors.append("Campo obrigatório ausente ou inválido: title")

        if status not in VALID_STATUSES:
            task_errors.append(f"Status inválido: {status!r}")

        if priority not in VALID_PRIORITIES:
            task_errors.append(f"Priority inválida: {priority!r}")

        parsed_due_date: datetime | None = None
        if due_date_raw is not None:
            if not isinstance(due_date_raw, str):
                task_errors.append("Campo opcional inválido: due_date deve ser string ISO-8601")
            else:
                try:
                    parsed_due_date = _parse_due_date(due_date_raw)
                except ValueError:
                    task_errors.append("Formato inválido: due_date deve seguir ISO-8601")

        if owner is not None and not isinstance(owner, str):
            task_errors.append("Campo opcional inválido: owner deve ser string")

        if task_errors:
            errors.append({"index": index, "id": task_id, "messages": task_errors})
            continue

        by_status[status] += 1
        by_priority[priority] += 1

        if parsed_due_date and parsed_due_date < reference_now and status != "done":
            risk_overdue += 1

    return {
        "summary": {
            "total_tasks": len(tasks),
            "by_status": dict(by_status),
            "by_priority": dict(by_priority),
            "risk_overdue": risk_overdue,
        },
        "errors": errors,
        "generated_at": reference_now.isoformat().replace("+00:00", "Z"),
    }
