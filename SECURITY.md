# Segurança

Este projeto não deve armazenar credenciais, tokens, chaves de API ou dados pessoais sensíveis no repositório.

## Boas práticas adotadas

- segredos devem ser fornecidos por variáveis de ambiente;
- arquivos `.env` não devem ser versionados;
- o arquivo `.env.example` deve conter apenas nomes de variáveis e valores fictícios;
- dados reais ou sensíveis não devem ser adicionados à pasta `data/`;
- futuras integrações com serviços externos devem enviar somente os dados estritamente necessários;
- dependências e automações de segurança serão revisadas conforme o projeto evoluir.

## Relato de problema de segurança

Não publique credenciais ou dados sensíveis em issues públicas. Caso seja identificado um problema de segurança, descreva-o sem expor segredos e utilize um canal privado quando disponível.
