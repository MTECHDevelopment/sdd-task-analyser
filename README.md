# sdd-task-analyser

Repositório da **Fase 1** do TaskAnalyzer: definição de escopo e contrato técnico antes da implementação.

## Entregáveis da Fase 1

- `task_analyzer_spec.md`: contrato SDD (objetivo, escopo, arquitetura, funcionalidades, dados, integrações futuras e requisitos não funcionais).
- `acceptance_scenarios.md`: cenários de aceite no formato Dado–Quando–Então, incluindo sucesso, falhas e bordas.
- `CONTEXT_RULES.md`: governança de contexto, fonte da verdade, limites de IA, revisão humana e controle de mudanças.
- `docs/video_explicativo_roteiro.md`: roteiro padronizado para vídeo explicativo.
- `docs/validation_workflow.md`: ciclo operacional de validação por etapa.
- `tools/validate_phase1.py`: verificador automático de presença e estrutura mínima dos artefatos.
- `.github/workflows/phase1-validation.yml`: validação automática em `push`/`pull_request`.

## Prompt inicial de @MTECHDevelopment (baseline da Fase 1)

O direcionamento inicial foi: formalizar a Fase 1 com escopo e contrato técnico antes do código, incluindo SDD completo, cenários Dado–Quando–Então, regras de contexto (CONTEXT_RULES), roteiro de vídeo explicativo e validação contínua por etapa com Python 3.13+ e integração futura com CI/CD.

## Validação local

```bash
python tools/validate_phase1.py
```
