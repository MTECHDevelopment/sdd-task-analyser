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
Repositório do projeto **TaskAnalyzer** com foco em desenvolvimento guiado por especificação (SDD), IA assistiva e validação contínua.

## Entregáveis da Fase 1

- [`/home/runner/work/sdd-task-analyser/sdd-task-analyser/task_analyzer_spec.md`](./task_analyzer_spec.md)
- [`/home/runner/work/sdd-task-analyser/sdd-task-analyser/acceptance_scenarios.md`](./acceptance_scenarios.md)
- [`/home/runner/work/sdd-task-analyser/sdd-task-analyser/CONTEXT_RULES.md`](./CONTEXT_RULES.md)
- [`/home/runner/work/sdd-task-analyser/sdd-task-analyser/docs/video_explicativo_roteiro.md`](./docs/video_explicativo_roteiro.md)
- [`/home/runner/work/sdd-task-analyser/sdd-task-analyser/docs/validation_workflow.md`](./docs/validation_workflow.md)

## Diretrizes aplicadas

- Python 3.13+
- documentação extensa e rastreável
- validação por etapa
- base para verificação de commits
- preparação para CI/CD

## Próxima etapa (Fase 2)

Implementar o sistema TaskAnalyzer com test harness automatizado em `pytest`, seguindo o contrato definido na Fase 1.
