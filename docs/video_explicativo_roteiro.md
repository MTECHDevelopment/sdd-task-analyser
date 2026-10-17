# Roteiro — Vídeo Explicativo (Fase 1)

## 1. Problema

Apresentar a necessidade de formalizar escopo e contrato técnico antes da implementação do TaskAnalyzer.

## 2. Solução proposta

Mostrar os artefatos criados na Fase 1:
- especificação SDD;
- cenários de aceite Dado–Quando–Então;
- governança de contexto;
- validação automática de conformidade.

## 3. Fluxo de utilização

1. Consultar especificação e regras de contexto.
2. Validar cenários de aceite.
3. Executar `python tools/validate_phase1.py`.
4. Confirmar validação no workflow de CI.

## 4. Critérios de aceite demonstrados

- Cobertura de sucesso, falhas e bordas.
- Rastreabilidade requisito → artefato.
- Evidência de validação automatizada em push/pull request.
