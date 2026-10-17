# Validação por etapa e preparo para CI/CD

## 1. Estratégia de validação incremental

Cada etapa deve seguir o ciclo:

1. atualizar requisito/escopo;
2. alinhar cenário de aceite;
3. implementar mudança;
4. executar validação automatizada;
5. registrar evidência no commit/PR.

## 2. Verificação de commits

Boas práticas mínimas:

1. Commits pequenos e com mensagem descritiva.
2. Um objetivo por commit.
3. Referência ao requisito/cenário afetado no corpo da PR.

Padrão sugerido de mensagem:

- `feat: ...`
- `fix: ...`
- `docs: ...`
- `test: ...`
- `chore: ...`

## 3. Base para integração CI/CD

Pipeline mínimo recomendado (próxima fase):

1. validação de estilo/lint;
2. execução do test harness em `pytest`;
3. validação de segurança básica (segredos/dependências);
4. bloqueio de merge em caso de falha.

## 4. Evidências obrigatórias na PR

- descrição objetiva do que foi feito;
- quais cenários de aceite foram cobertos;
- quais comandos/testes foram executados e resultado;
- limitações e próximos passos, quando aplicável.
