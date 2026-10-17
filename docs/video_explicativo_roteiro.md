# Roteiro do vídeo explicativo (Fase 1)

## 1. Problema

- Contextualizar a necessidade de analisar tarefas com regras consistentes e evidências de validação.
- Explicar riscos de ausência de contrato técnico (retrabalho, divergência e baixa rastreabilidade).

## 2. Solução proposta

- Apresentar o TaskAnalyzer orientado por SDD.
- Mostrar os artefatos da Fase 1:
  - especificação técnica;
  - cenários de aceite;
  - governança CONTEXT_RULES;
  - estratégia de validação e CI/CD.

## 3. Fluxo de utilização

1. Definir/atualizar requisitos no SDD.
2. Validar comportamento esperado com cenários Dado–Quando–Então.
3. Implementar em Python 3.13+ seguindo CONTEXT_RULES.
4. Executar validações automatizadas e revisão humana.
5. Registrar evidências via commits e PR.

## 4. Critérios de aceite demonstrados

- Sucesso com entrada válida.
- Erros de validação (campos obrigatórios e formatos).
- Casos de borda (lista vazia, duplicidades, opcionais ausentes).
- Rastreabilidade entre requisito, cenário e evolução do código.

## 5. Encerramento

- Reforçar que a Fase 1 cria a base para implementação confiável na Fase 2.
- Informar próximos passos: desenvolvimento do core e test harness em `pytest`.
