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

### Regressão Linear

A regressão linear é o modelo mais simples e intuitivo, assumindo uma relação linear entre as variáveis independentes e a dependente. Pode ser simples (uma variável) ou múltipla (várias variáveis). É computacionalmente eficiente e funciona bem quando a relação entre variáveis é aproximadamente linear.

### Regressão Polinomial

Estende a regressão linear permitindo relações não-lineares entre as variáveis. Adiciona termos polinomiais (quadrático, cúbico, etc.) para capturar padrões mais complexos. Deve-se cuidar com overfitting ao aumentar o grau do polinômio.

### Regressão Ridge e Lasso

São técnicas de regularização que adicionam uma penalidade aos coeficientes para evitar overfitting. Ridge penaliza a soma dos quadrados dos coeficientes, enquanto Lasso penaliza o valor absoluto, podendo levar coeficientes a zero.

### Árvores de Decisão para Regressão

Dividem o espaço das variáveis em regiões e fazem predições baseadas na média dos valores na região. São capazes de capturar relações não-lineares complexas, mas tendem a sofrer com overfitting em dados ruidosos.

### Redes Neurais

Modelos mais complexos compostos de camadas de neurônios interconectados. Podem aprender relações muito complexas, mas requerem mais dados de treino e maior poder computacional.
