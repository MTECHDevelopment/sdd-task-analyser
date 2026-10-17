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
import re
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "task_analyzer_spec.md",
    "acceptance_scenarios.md",
    "CONTEXT_RULES.md",
    "docs/video_explicativo_roteiro.md",
    "docs/validation_workflow.md",
]

REQUIRED_HEADINGS = {
    "task_analyzer_spec.md": [
        "## 1. Objetivo",
        "## 2. Escopo",
        "## 3. Arquitetura proposta",
        "## 4. Funcionalidades",
        "## 7. Requisitos não funcionais",
    ],
    "acceptance_scenarios.md": [
        "## Cenários de aceite (Dado–Quando–Então)",
        "## Matriz de cobertura",
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
        "## 6. Controle de alterações",
    ],
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check_required_files() -> list[str]:
    errors: list[str] = []
    for relative_path in REQUIRED_FILES:
        path = REPO_ROOT / relative_path
        if not path.exists():
            errors.append(f"Arquivo obrigatório ausente: {relative_path}")
    return errors


def check_headings() -> list[str]:
    errors: list[str] = []
    for relative_path, headings in REQUIRED_HEADINGS.items():
        content = read_text(REPO_ROOT / relative_path)
        for heading in headings:
            if heading not in content:
                errors.append(f"Heading obrigatório não encontrado em {relative_path}: {heading}")
    return errors


def check_given_when_then() -> list[str]:
    errors: list[str] = []
    content = read_text(REPO_ROOT / "acceptance_scenarios.md")
    scenarios = len(re.findall(r"^### Cenário", content, flags=re.MULTILINE))
    if scenarios < 6:
        errors.append("Mínimo de 6 cenários de aceite não atingido.")

    for token in ["**Dado**", "**Quando**", "**Então**"]:
        if token not in content:
            errors.append(f"Token obrigatório ausente em acceptance_scenarios.md: {token}")
    return errors


def main() -> int:
    errors = [
        *check_required_files(),
        *check_headings(),
        *check_given_when_then(),
    ]

    if errors:
        print("Falha na validação da Fase 1:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Validação da Fase 1 concluída com sucesso.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
