from __future__ import annotations

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = {
    "task_analyzer_spec.md": [
        "## 1. Objetivo",
        "## 2. Escopo",
        "## 3. Arquitetura em camadas",
        "## 8. Matriz de rastreabilidade",
    ],
    "acceptance_scenarios.md": [
        "Dado",
        "Quando",
        "Então",
    ],
    "CONTEXT_RULES.md": [
        "## 1. Fonte da verdade",
        "## 2. Limites da IA",
        "## 4. Revisão humana obrigatória",
    ],
    "docs/video_explicativo_roteiro.md": [
        "## 1. Problema",
        "## 2. Solução proposta",
        "## 4. Critérios de aceite demonstrados",
    ],
    "docs/validation_workflow.md": [
        "## Objetivo",
        "## Ciclo por etapa",
        "## Critérios mínimos de conformidade",
    ],
}


def validate_file(path: Path, required_tokens: list[str]) -> list[str]:
    errors: list[str] = []
    if not path.exists():
        return [f"Arquivo obrigatório ausente: {path.relative_to(ROOT)}"]

    content = path.read_text(encoding="utf-8")
    for token in required_tokens:
        if token not in content:
            errors.append(
                f"Estrutura mínima ausente em {path.relative_to(ROOT)}: '{token}'"
            )
    return errors


def validate_workflow() -> list[str]:
    errors: list[str] = []
    workflow_path = ROOT / ".github/workflows/phase1-validation.yml"
    if not workflow_path.exists():
        return [f"Arquivo obrigatório ausente: {workflow_path.relative_to(ROOT)}"]

    workflow = workflow_path.read_text(encoding="utf-8")
    required_snippets = [
        "permissions:",
        "contents: read",
        "python-version: \"3.13\"",
        "python tools/validate_phase1.py",
        "push:",
        "pull_request:",
    ]
    for snippet in required_snippets:
        if snippet not in workflow:
            errors.append(
                f"Workflow incompleto em {workflow_path.relative_to(ROOT)}: '{snippet}'"
            )
    return errors


def main() -> int:
    errors: list[str] = []

    for relative_path, tokens in REQUIRED_FILES.items():
        errors.extend(validate_file(ROOT / relative_path, tokens))

    errors.extend(validate_workflow())

    if errors:
        print("❌ Validação da Fase 1 falhou:")
        for item in errors:
            print(f"- {item}")
        return 1

    print("✅ Validação da Fase 1 concluída com sucesso.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
