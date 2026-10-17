# acceptance_scenarios.md

## Cenários de aceite (Dado–Quando–Então)

### Cenário 1 — Análise bem-sucedida com dados válidos

**Dado** uma lista de tarefas com campos obrigatórios válidos e IDs únicos  
**Quando** o analisador executar o processamento  
**Então** o relatório deve ser gerado com resumo total, distribuição por status/prioridade e sem erros.

### Cenário 2 — Falha por task sem `id`

**Dado** uma lista contendo uma tarefa sem campo `id`  
**Quando** o analisador validar a entrada  
**Então** deve registrar erro de validação indicando ausência de identificador obrigatório.

### Cenário 3 — Falha por `status` inválido

**Dado** uma tarefa com valor de `status` fora do conjunto permitido  
**Quando** a validação semântica for executada  
**Então** o sistema deve rejeitar a tarefa e retornar mensagem de erro clara.

### Cenário 4 — Caso de borda com lista vazia

**Dado** uma lista de tarefas vazia  
**Quando** a análise for executada  
**Então** o relatório deve ser gerado com totais zerados e sem exceções não tratadas.

### Cenário 5 — ID duplicado

**Dado** duas tarefas com o mesmo `id`  
**Quando** o sistema validar unicidade  
**Então** deve retornar erro indicando duplicidade de identificador.

### Cenário 6 — Risco de atraso

**Dado** tarefas com prazo vencido e status ainda não concluído  
**Quando** o cálculo de risco for executado  
**Então** o campo `risk_overdue` deve refletir corretamente a quantidade de tarefas em risco.

### Cenário 7 — Robustez com campos opcionais ausentes

**Dado** tarefas válidas sem `due_date` e sem `owner`  
**Quando** a análise for executada  
**Então** o sistema deve processar normalmente, preservando os cálculos aplicáveis.

### Cenário 8 — Estrutura inválida de data

**Dado** tarefa com `due_date` em formato não ISO-8601  
**Quando** a validação de formato for executada  
**Então** deve ser retornado erro de formato para a tarefa afetada.

## Matriz de cobertura

| ID requisito | Cenários relacionados |
|---|---|
| RQ-01 | 1, 4, 6, 7 |
| RQ-03 | Todos |
| RQ-06 | Todos |
