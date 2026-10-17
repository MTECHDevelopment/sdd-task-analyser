# Workflow de Validação — Fase 1

## Objetivo

Padronizar a validação dos artefatos obrigatórios da Fase 1 para evitar regressões documentais.

## Ciclo por etapa

1. Atualizar documentação relacionada ao requisito.
2. Executar validação local:
   - `python tools/validate_phase1.py`
3. Revisar saída e corrigir inconsistências.
4. Submeter alteração com rastreabilidade explícita.
5. Validar novamente no CI (`phase1-validation.yml`).

## Critérios mínimos de conformidade

- Presença de todos os artefatos exigidos.
- Estrutura mínima (seções-chave) em cada arquivo.
- Workflow de CI ativo para `push` e `pull_request`.
