# Mineração de Dados - 2026/05/22

## Predição e Regressão

Predição é o processo de usar dados conhecidos para estimar um resultado futuro ou desconhecido. Em mineração de dados, ela aparece em dois cenários principais: classificação, quando a saída é uma categoria, e regressão, quando a saída é um valor numérico.

Regressão é uma técnica de aprendizado supervisionado usada para modelar a relação entre variáveis independentes e uma variável dependente contínua. O objetivo é aprender uma função que consiga prever valores próximos aos reais com o menor erro possível.

O fluxo básico de um problema de regressão costuma ser:

- coletar e preparar os dados;
- separar em conjuntos de treino e teste;
- escolher um modelo, como regressão linear, árvore de decisão ou rede neural;
- treinar o modelo com os dados de treino;
- avaliar o desempenho com métricas adequadas;
- ajustar parâmetros e repetir o processo se necessário.

As métricas mais comuns em regressão são:

- MAE, que mede o erro absoluto médio;
- MSE, que penaliza erros maiores;
- RMSE, que é a raiz do erro quadrático médio;
- R², que indica o quanto o modelo explica a variação dos dados.

Exemplos de aplicação incluem previsão de preço de imóveis, estimativa de vendas, projeção de consumo de energia e previsão de demanda.

### Predição

Predição é o ato de usar um modelo treinado para estimar valores ou categorias para novos dados. O processo envolve:

- usar o modelo treinado com novos dados;
- gerar estimativas para resultados desconhecidos;
- avaliar a confiabilidade das predições.

A qualidade das predições depende diretamente da qualidade do modelo e dos dados usados no treinamento. Modelos bem calibrados conseguem generalizar bem para novos dados.

#### Preditores (ou variáveis independentes)

Preditores são as variáveis de entrada usadas para explicar ou prever o comportamento da variável alvo. Também são chamados de variáveis independentes, atributos, características ou features.

Em um problema de regressão, os preditores representam os fatores que influenciam o resultado que se deseja estimar. Por exemplo, na previsão do preço de um imóvel, podem ser preditores a área construída, o número de quartos, a localização e a idade do imóvel.

Características importantes dos preditores:

- fornecem informação para o modelo aprender padrões;
- podem ser numéricos, categóricos ou derivados de outras variáveis;
- devem ter relação com o problema que se quer resolver;
- precisam ser tratados e selecionados com cuidado para melhorar a qualidade da predição.

A escolha dos preditores influencia diretamente o desempenho do modelo. Preditores relevantes ajudam a aumentar a precisão, enquanto preditores irrelevantes, redundantes ou muito ruidosos podem prejudicar o aprendizado.

Na prática, a etapa de preparação dos dados costuma incluir:

- seleção das variáveis mais úteis;
- tratamento de valores ausentes;
- codificação de variáveis categóricas;
- normalização ou padronização, quando necessário;
- criação de novas variáveis a partir das existentes.

Assim, os preditores são a base de qualquer modelo supervisionado, pois é a partir deles que o algoritmo identifica relações e gera previsões.

#### Resposta (ou variavel dependente)

A resposta, também chamada de variável dependente, alvo, saída ou target, é o valor que o modelo tenta prever. Em problemas de regressão, ela é numérica e representa a grandeza que se deseja estimar.

No exemplo de previsão de preço de imóveis, a resposta pode ser o valor do imóvel. Nesse caso, os preditores seriam características como área, localização, número de quartos e idade do imóvel, enquanto a resposta seria o preço final.

Características importantes da resposta:

- é a variável que depende dos preditores;
- é o resultado que o modelo aprende a estimar;
- em regressão, deve ser contínua ou numérica;
- em classificação, costuma ser uma categoria.

A qualidade da resposta influencia diretamente o aprendizado do modelo. Se os dados da resposta estiverem incorretos, incompletos ou inconsistentes, o modelo terá dificuldade para aprender relações confiáveis.

Na preparação dos dados, a resposta normalmente é separada das variáveis de entrada e usada como referência para o treinamento e a avaliação do modelo.

### Regressão Linear

A regressão linear é o modelo mais simples e intuitivo, assumindo uma relação linear entre as variáveis independentes e a dependente. Pode ser simples (uma variável) ou múltipla (várias variáveis). É computacionalmente eficiente e funciona bem quando a relação entre variáveis é aproximadamente linear.

#### Regressão Polinomial

Estende a regressão linear permitindo relações não-lineares entre as variáveis. Adiciona termos polinomiais (quadrático, cúbico, etc.) para capturar padrões mais complexos. Deve-se cuidar com overfitting ao aumentar o grau do polinômio.

#### Regressão Ridge e Lasso

São técnicas de regularização que adicionam uma penalidade aos coeficientes para evitar overfitting. Ridge penaliza a soma dos quadrados dos coeficientes, enquanto Lasso penaliza o valor absoluto, podendo levar coeficientes a zero.

#### Árvores de Decisão para Regressão

Dividem o espaço das variáveis em regiões e fazem predições baseadas na média dos valores na região. São capazes de capturar relações não-lineares complexas, mas tendem a sofrer com overfitting em dados ruidosos.

#### Redes Neurais

Modelos mais complexos compostos de camadas de neurônios interconectados. Podem aprender relações muito complexas, mas requerem mais dados de treino e maior poder computacional.
