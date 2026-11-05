# Encontro - 2026/11/05 - Apendizado de Máquinas

## Metodo SEMMA em Ciência de Dados

O SEMMA é uma metodologia de mineração de dados criada pelo SAS, composta por cinco etapas: Sample, Explore, Modify, Model e Assess.

1. Sample (Amostragem): selecionar uma amostra representativa dos dados para análise.
2. Explore (Exploração): investigar os dados, identificando padrões, relações, tendências e possíveis problemas.
3. Modify (Modificação): limpar, transformar e preparar as variáveis para a modelagem.
4. Model (Modelagem): aplicar técnicas de aprendizado de máquina para construir modelos preditivos ou descritivos.
5. Assess (Avaliação): avaliar o desempenho e a utilidade do modelo, comparando os resultados com os objetivos do projeto.

O processo é iterativo: os resultados da avaliação podem indicar a necessidade de retornar a etapas anteriores para aprimorar os dados ou o modelo.

### Sample (Amostragem)

Nesta etapa, define-se a população de interesse e seleciona-se uma amostra representativa para a análise. A amostra deve preservar, tanto quanto possível, as características importantes do conjunto original, evitando vieses e reduzindo o custo computacional. Também é necessário identificar a origem dos dados, o período analisado, o tamanho da amostra e os critérios de inclusão e exclusão.

Uma amostragem inadequada pode produzir conclusões que não representam a realidade. Por isso, quando apropriado, podem ser utilizadas técnicas aleatórias, estratificadas ou sistemáticas, além da separação dos dados em conjuntos de treino, validação e teste.

### Explore (Exploração)

O objetivo é conhecer os dados antes de transformá-los ou aplicar qualquer modelo. Realizam-se análises estatísticas e visualizações para observar distribuições, valores típicos, outliers, relações entre variáveis e possíveis padrões.

Também devem ser investigados valores ausentes, duplicidades, inconsistências, erros de preenchimento e desbalanceamento entre as classes. Essa exploração ajuda a formular hipóteses, escolher variáveis relevantes e definir quais tratamentos serão necessários nas etapas seguintes.

### Modify (Modificação)

Nesta fase, os dados são preparados para a modelagem. As ações podem incluir correção de tipos, remoção de duplicidades, tratamento de valores ausentes e outliers, padronização de categorias e normalização ou padronização de variáveis numéricas.

Também podem ser criadas novas variáveis, selecionadas as características mais úteis e codificadas variáveis categóricas. As transformações devem ser aplicadas de forma consistente e sem utilizar informações do conjunto de teste, evitando vazamento de dados e mantendo a possibilidade de reproduzir o processamento.

### Model (Modelagem)

Com os dados preparados, selecionam-se técnicas de aprendizado de máquina adequadas ao objetivo, como classificação, regressão, agrupamento ou redução de dimensionalidade. Podem ser treinados diferentes algoritmos e configurações para comparar suas capacidades de generalização.

O treinamento deve ser feito com os dados apropriados, utilizando validação cruzada ou um conjunto de validação para ajustar hiperparâmetros. O conjunto de teste deve permanecer separado até a avaliação final, e decisões sobre o modelo devem considerar tanto seu desempenho quanto sua interpretabilidade, custo e aplicabilidade.

### Assess (Avaliação)

Nesta etapa, verifica-se se o modelo atende aos objetivos definidos no projeto. Para isso, utilizam-se métricas compatíveis com o problema: acurácia, precisão, revocação, F1-score e matriz de confusão em classificação; MAE, MSE, RMSE e R² em regressão; ou medidas específicas para agrupamento.

Além das métricas, é importante analisar erros, estabilidade, possíveis vieses, desempenho em diferentes grupos e comparação com uma linha de base. Se os resultados forem insuficientes ou revelarem problemas, retorna-se às etapas de Explore, Modify ou Model para investigar e aprimorar o processo.
