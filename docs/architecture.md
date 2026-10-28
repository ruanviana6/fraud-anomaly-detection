# Arquitetura do projeto

A arquitetura foi pensada para começar simples e permitir crescimento gradual sem transformar o notebook em código de produção.

## Responsabilidades

`notebooks/` concentra exploração, estudo e experimentos.

`src/fraud_detection/data.py` concentra carregamento e acesso aos dados.

`src/fraud_detection/preprocessing.py` concentra transformações reutilizáveis e deve evitar vazamento de dados.

`src/fraud_detection/models.py` concentra a criação dos modelos utilizados na solução.

`src/fraud_detection/evaluation.py` concentra métricas e avaliações reutilizadas entre modelos.

`src/fraud_detection/inference.py` concentra regras usadas depois que o modelo já produziu uma probabilidade, como threshold e futura classificação de risco.

`tests/` receberá testes automatizados à medida que a lógica sair do notebook.

`reports/figures/` será usado para imagens e gráficos selecionados para documentação.

## Evolução prevista

A próxima evolução natural é consolidar o pipeline de treinamento e inferência. Somente depois disso serão avaliadas camadas como API, containerização, CI/CD, monitoramento de modelo e integração com IA.

A IA generativa, caso seja adicionada, deverá atuar como camada de apoio à interpretação ou investigação de alertas, não como substituta direta do modelo de fraude.
