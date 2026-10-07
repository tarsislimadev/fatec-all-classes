# Encontro 2026/10/07 - Estatística

## Desvio Padrão

O **desvio padrão** mede o quanto os valores de um conjunto de dados se afastam, em média, da média aritmética. Quanto menor o desvio padrão, mais próximos da média estão os dados; quanto maior, mais dispersos eles estão.

### Cálculo

1. Calcule a média dos valores.
2. Subtraia a média de cada valor e eleve cada diferença ao quadrado.
3. Calcule a média dessas diferenças quadráticas — essa é a **variância**.
4. Extraia a raiz quadrada da variância.

Para uma população, usa-se:

\[
\sigma = \sqrt{\frac{\sum_{i=1}^{N}(x_i - \mu)^2}{N}}
\]

Para uma amostra, divide-se por `n - 1`:

\[
s = \sqrt{\frac{\sum_{i=1}^{n}(x_i - \bar{x})^2}{n - 1}}
\]

O resultado é expresso na mesma unidade dos dados. Por exemplo, se as notas têm desvio padrão baixo, elas são semelhantes entre si; se têm desvio padrão alto, há maior diferença entre as notas.
