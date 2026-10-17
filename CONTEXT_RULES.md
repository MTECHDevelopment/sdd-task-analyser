# CONTEXT_RULES.md

## 1. Fonte da verdade

1. O contrato funcional e técnico do projeto é definido por `task_analyzer_spec.md`.
2. Cenários verificáveis de comportamento são definidos por `acceptance_scenarios.md`.
3. Em caso de conflito entre implementação e documentação, prevalece o contrato aprovado em revisão humana.

## 2. Limites da IA

1. IA pode auxiliar em geração de código, testes e documentação.
2. IA não substitui revisão humana para decisões críticas de negócio.
3. Toda sugestão de IA deve ser validada por critérios objetivos (testes, cenários de aceite e inspeção).

## 3. Convenções técnicas

1. Python 3.13+ é obrigatório.
2. Arquitetura modular com separação clara de domínio, aplicação e infraestrutura.
3. Cada mudança deve manter rastreabilidade com requisito e cenário de aceite.

## 4. Decisões técnicas e registro

1. Decisões relevantes devem ser registradas em pull requests ou documentação equivalente.
2. Mudanças de contrato exigem atualização de SDD e cenários de aceite na mesma entrega.
3. Decisões sem evidência de validação devem ser tratadas como pendentes.

## 5. Revisão humana obrigatória

1. Revisão humana deve validar consistência entre requisito, implementação e testes.
2. Pull request sem evidência de validação mínima não deve ser aprovado.
3. Alterações de alto impacto exigem revisão de pelo menos um revisor adicional.

## 6. Controle de alterações

1. Toda alteração deve ser versionada em branch dedicada.
2. Commits devem ser pequenos, descritivos e rastreáveis ao objetivo da etapa.
3. PR deve descrever: contexto, mudança realizada, validações executadas e resultado.
4. Não introduzir segredos, tokens ou credenciais no repositório.
