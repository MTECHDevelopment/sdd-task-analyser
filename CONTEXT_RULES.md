# CONTEXT_RULES — Governança de Contexto

## 1. Fonte da verdade

- A documentação da Fase 1 é a referência primária para decisões técnicas antes da implementação.
- Alterações de escopo devem atualizar os artefatos de contrato e aceite na mesma mudança.

## 2. Limites da IA

- IA pode apoiar redação, revisão e estruturação de artefatos.
- IA não substitui validação humana final nem aprovação de mudanças críticas.
- Decisões de negócio devem ser explicitadas em documentação versionada.

## 3. Convenções técnicas

- Python 3.13+ como baseline da fase.
- Linguagem objetiva, rastreável e orientada a requisitos.
- Cenários de aceite no padrão Dado–Quando–Então.

## 4. Revisão humana obrigatória

- Toda mudança em artefatos de Fase 1 exige revisão humana.
- Ajustes de contrato funcional precisam de verificação de consistência com rastreabilidade.

## 5. Controle de mudanças

- Todo requisito novo deve incluir referência de rastreabilidade.
- Regressões estruturais dos artefatos devem ser bloqueadas por validação automática.
