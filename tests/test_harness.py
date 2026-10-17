from __future__ import annotations

from datetime import datetime, timezone

from src.task_analyzer import analyze_tasks


def test_analyze_tasks_successful_report() -> None:
    now = datetime(2026, 10, 17, 0, 0, tzinfo=timezone.utc)
    tasks = [
        {
            "id": "T-1",
            "title": "Criar especificação",
            "status": "done",
            "priority": "high",
            "due_date": "2026-10-10T12:00:00Z",
            "owner": "alice",
        },
        {
            "id": "T-2",
            "title": "Implementar validador",
            "status": "in_progress",
            "priority": "medium",
            "due_date": "2026-10-16T12:00:00Z",
        },
    ]

    report = analyze_tasks(tasks, now=now)

    assert report["errors"] == []
    assert report["summary"]["total_tasks"] == 2
    assert report["summary"]["by_status"] == {"done": 1, "in_progress": 1}
    assert report["summary"]["by_priority"] == {"high": 1, "medium": 1}
    assert report["summary"]["risk_overdue"] == 1


def test_missing_id_returns_validation_error() -> None:
    report = analyze_tasks(
        [
            {
                "title": "Task sem id",
                "status": "todo",
                "priority": "low",
            }
        ]
    )

    assert report["summary"]["total_tasks"] == 1
    assert len(report["errors"]) == 1
    assert "Campo obrigatório ausente ou inválido: id" in report["errors"][0]["messages"]


def test_duplicate_id_returns_validation_error() -> None:
    report = analyze_tasks(
        [
            {"id": "T-1", "title": "A", "status": "todo", "priority": "low"},
            {"id": "T-1", "title": "B", "status": "todo", "priority": "high"},
        ]
    )

    assert len(report["errors"]) == 1
    assert "Identificador duplicado: id" in report["errors"][0]["messages"]


def test_empty_task_list_returns_zeroed_summary() -> None:
    report = analyze_tasks([])

    assert report["errors"] == []
    assert report["summary"] == {
        "total_tasks": 0,
        "by_status": {},
        "by_priority": {},
        "risk_overdue": 0,
    }


def test_invalid_due_date_format_returns_error() -> None:
    report = analyze_tasks(
        [
            {
                "id": "T-1",
                "title": "Data inválida",
                "status": "todo",
                "priority": "low",
                "due_date": "17/10/2026",
            }
        ]
    )

    assert len(report["errors"]) == 1
    assert "Formato inválido: due_date deve seguir ISO-8601" in report["errors"][0]["messages"]


def test_optional_fields_can_be_omitted() -> None:
    report = analyze_tasks(
        [
            {
                "id": "T-3",
                "title": "Sem campos opcionais",
                "status": "todo",
                "priority": "critical",
            }
        ]
    )

    assert report["errors"] == []
    assert report["summary"]["by_priority"] == {"critical": 1}
