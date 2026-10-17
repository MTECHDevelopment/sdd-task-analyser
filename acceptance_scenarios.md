# Cenários de Aceite — TaskAnalyzer

## Cenário 1 — Sucesso no processamento

**Dado** uma lista válida de tarefas com IDs únicos e datas válidas  
**Quando** o TaskAnalyzer processa a entrada  
**Então** o resultado deve indicar sucesso e retornar tarefas normalizadas sem erros.

## Cenário 2 — Falha por lista vazia

**Dado** uma lista de tarefas vazia  
**Quando** o TaskAnalyzer executa a validação  
**Então** deve retornar erro de validação informando que a lista não pode ser vazia.

## Cenário 3 — Falha por ID duplicado

**Dado** duas tarefas com o mesmo `id`  
**Quando** o TaskAnalyzer valida unicidade  
**Então** deve retornar erro de duplicidade de ID com referência ao valor conflitante.

## Cenário 4 — Falha por data inválida

**Dado** uma tarefa com `created_at` ou `due_date` em formato inválido  
**Quando** o TaskAnalyzer valida campos de data  
**Então** deve retornar erro indicando formato de data inválido.

## Cenário 5 — Campo opcional ausente

**Dado** uma tarefa sem `description`  
**Quando** o TaskAnalyzer processa a entrada  
**Então** deve concluir com sucesso, mantendo o campo opcional como nulo/ausente sem erro.

## Cenário 6 — Borda de coerência temporal

**Dado** uma tarefa com `due_date` anterior a `created_at`  
**Quando** o TaskAnalyzer valida coerência temporal  
**Então** deve retornar erro de regra de negócio para intervalo inválido.
