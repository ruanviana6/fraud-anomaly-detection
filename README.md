# Detecção de Fraudes e Anomalias em Transações Financeiras

Projeto de Machine Learning voltado à **detecção de fraudes, identificação de anomalias, análise de risco e explicabilidade de modelos** em transações financeiras.

> **Status:** em desenvolvimento.  
> O projeto nasceu a partir dos estudos do Bootcamp DIO + Bradesco e está sendo expandido para uma solução de portfólio com foco em boas práticas de dados, Machine Learning, segurança, organização de código e evolução futura para um serviço de inferência.

## Visão geral

Fraudes financeiras são um problema especialmente desafiador porque representam uma parcela muito pequena do volume total de transações. Nesse cenário, um modelo pode apresentar alta acurácia e ainda assim falhar justamente na classe mais importante: a fraude.

Este projeto busca construir uma abordagem que vá além de simplesmente treinar um classificador. O objetivo é avaliar:

- desempenho de diferentes modelos supervisionados;
- impacto do forte desbalanceamento entre as classes;
- trade-off entre detectar mais fraudes e gerar falsos alertas;
- ajuste do threshold de decisão;
- detecção de comportamentos anômalos;
- explicabilidade das previsões;
- evolução futura para um pipeline de inferência mais próximo de um sistema real.

## Dataset

O projeto utiliza o dataset público de transações com cartão de crédito disponibilizado pelo TensorFlow:

`https://storage.googleapis.com/download.tensorflow.org/data/creditcard.csv`

Características principais:

- **284.807 transações**;
- **492 fraudes**;
- aproximadamente **0,17%** das observações pertencem à classe fraudulenta;
- `Class = 0`: transação normal;
- `Class = 1`: fraude;
- variáveis `V1` a `V28` anonimizadas e transformadas;
- `Time`: tempo decorrido entre as transações;
- `Amount`: valor da transação.

## Metodologia

O fluxo atual do projeto é organizado nas seguintes etapas:

```text
Carregamento dos dados
        ↓
Conhecimento e validação do dataset
        ↓
Análise exploratória (EDA)
        ↓
Separação treino/teste com estratificação
        ↓
Pré-processamento sem data leakage
        ↓
Modelos supervisionados
        ↓
Tratamento do desbalanceamento
        ↓
Comparação de métricas
        ↓
Ajuste de threshold
        ↓
Detecção de anomalias
        ↓
Explicabilidade com Feature Importance e SHAP
        ↓
Risk Score / inferência
```

### Preparação dos dados

A análise exploratória mostrou forte assimetria na variável `Amount`. Por isso, o projeto utiliza:

```text
Amount
  ↓
log1p
  ↓
Amount_log
  ↓
StandardScaler
  ↓
Amount_log_scaled
```

Também é realizada a padronização de `Time`.

Para evitar **data leakage**, transformações que precisam aprender parâmetros dos dados são ajustadas somente no conjunto de treinamento e depois aplicadas ao conjunto de teste.

O conjunto de teste permanece separado e mantém a distribuição real das classes.

## Modelos avaliados

Até o momento foram utilizados:

- Logistic Regression como baseline;
- Logistic Regression com `class_weight="balanced"`;
- Logistic Regression com SMOTE aplicado somente ao treino;
- Random Forest;
- XGBoost;
- Isolation Forest para detecção não supervisionada de anomalias.

## Resultados atuais

Resultados obtidos no mesmo conjunto de teste:

| Modelo | Precision | Recall | F1-Score | ROC-AUC | Average Precision |
| --- | ---: | ---: | ---: | ---: | ---: |
| Logistic Regression - Baseline | 0,8243 | 0,6224 | 0,7093 | 0,9573 | 0,7388 |
| Logistic Regression - Balanced | 0,0602 | **0,9184** | 0,1129 | **0,9712** | 0,7113 |
| Logistic Regression - SMOTE | 0,0578 | **0,9184** | 0,1088 | 0,9696 | 0,7222 |
| Random Forest | **0,9524** | 0,8163 | **0,8791** | 0,9528 | **0,8539** |
| XGBoost | 0,8966 | 0,7959 | 0,8432 | 0,9219 | 0,7813 |

A Random Forest apresentou, até esta etapa, o melhor equilíbrio geral entre identificação de fraudes e controle de falsos positivos.

### Ajuste de threshold

O threshold padrão de `0.50` foi comparado com limites menores.

Para a Random Forest, o threshold `0.40` apresentou um equilíbrio melhor entre precision e recall:

| Threshold | Precision | Recall | F1-Score | Falsos positivos | Falsos negativos | Fraudes detectadas |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0,50 | 0,9524 | 0,8163 | 0,8791 | 4 | 18 | 80 |
| **0,40** | **0,9130** | **0,8571** | **0,8842** | **8** | **14** | **84** |
| 0,30 | 0,8571 | 0,8571 | 0,8571 | 14 | 14 | 84 |
| 0,20 | 0,7963 | 0,8776 | 0,8350 | 22 | 12 | 86 |

O resultado reforça que a escolha do threshold é uma **decisão de negócio**, e não apenas uma configuração técnica.

## Detecção de anomalias

O Isolation Forest foi utilizado para investigar uma abordagem sem supervisão direta da variável `Class`.

O modelo conseguiu identificar uma parcela relevante das fraudes como anomalias, mas também sinalizou muitas transações legítimas.

Isso reforça um ponto importante:

> **anomalia não é sinônimo de fraude.**

A abordagem não supervisionada será tratada como um possível **sinal complementar de risco**, e não como substituta dos modelos supervisionados.

## Explicabilidade

A explicabilidade é tratada em duas camadas:

### Feature Importance

A Random Forest destacou principalmente variáveis como:

- `V17`;
- `V14`;
- `V12`;
- `V10`;
- `V11`;
- `V16`.

Essas variáveis também aparecem com destaque durante a análise exploratória.

### SHAP

O SHAP está sendo utilizado para analisar:

- influência global das variáveis;
- direção do impacto de cada feature;
- explicação de previsões individuais;
- fatores que aumentam ou reduzem o risco atribuído a uma transação.

Como `V1` a `V28` são variáveis anonimizadas, o projeto não atribui significados de negócio inexistentes a essas features.

## Arquitetura e evolução do projeto

O notebook é utilizado como ambiente de **exploração, experimentação e estudo**. Conforme a solução for consolidada, a lógica reutilizável será gradualmente extraída para módulos Python.

Estrutura alvo:

```text
fraud-anomaly-detection/
│
├── .github/
│   └── workflows/
│
├── data/
│   └── README.md
│
├── notebooks/
│   └── fraud_detection.ipynb
│
├── src/
│   └── fraud_detection/
│       ├── __init__.py
│       ├── data.py
│       ├── preprocessing.py
│       ├── models.py
│       ├── evaluation.py
│       └── inference.py
│
├── tests/
│
├── reports/
│   └── figures/
│
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
└── SECURITY.md
```

A estrutura será criada de forma incremental conforme o projeto exigir, evitando abstrações ou complexidade desnecessária.

## Segurança

O projeto será evoluído seguindo alguns princípios básicos:

- nenhuma chave, token ou credencial deve ser versionada;
- arquivos `.env` permanecem fora do Git;
- futuras integrações utilizarão variáveis de ambiente;
- dados sensíveis não deverão ser enviados diretamente para serviços externos;
- futuras integrações com IA deverão seguir princípios de minimização e anonimização de dados;
- dependências e automações de segurança serão adicionadas conforme a estrutura do projeto evoluir.

O dataset atual utiliza variáveis anonimizadas, o que reduz a exposição de informações sensíveis durante o desenvolvimento.

## Próximos passos

- [ ] concluir a análise individual de previsões com SHAP;
- [ ] desenvolver uma classificação de risco baseada na probabilidade de fraude;
- [ ] consolidar a comparação final dos modelos;
- [ ] organizar o notebook final;
- [ ] extrair pré-processamento e inferência para módulos em `src/`;
- [ ] adicionar testes automatizados;
- [ ] declarar e versionar dependências;
- [ ] configurar CI com GitHub Actions;
- [ ] adicionar controles de segurança e análise de dependências;
- [ ] avaliar criação de uma API de inferência;
- [ ] avaliar containerização;
- [ ] estudar monitoramento e versionamento de modelos;
- [ ] explorar uma futura camada de IA para apoio à interpretação e investigação de alertas.

## Tecnologias

- Python
- pandas
- NumPy
- Matplotlib
- scikit-learn
- imbalanced-learn
- XGBoost
- SHAP
- Jupyter Notebook
- Git / GitHub

## Origem do projeto

O projeto teve como ponto de partida conteúdos estudados no **Bootcamp DIO + Bradesco** e está sendo expandido com análises, decisões metodológicas, melhorias de engenharia e funcionalidades adicionais para transformá-lo em um projeto autoral de portfólio.

---

Este repositório está em evolução. Resultados, arquitetura e documentação podem ser atualizados conforme novas etapas do projeto forem implementadas.
