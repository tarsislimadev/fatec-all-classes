# Encontro 2026/11/04 - Estatística

## Distribuição de Poisson

### O que é

A distribuição de Poisson é uma distribuição de probabilidade discreta usada para modelar o número de ocorrências de um evento em um intervalo fixo de tempo, espaço ou outra unidade de exposição, quando:

- os eventos ocorrem de forma independente;
- a taxa média de ocorrência é constante;
- a probabilidade de duas ocorrências simultâneas é desprezível.

Ela é adequada para situações como o número de chamadas recebidas por minuto, defeitos em um metro de tecido, acidentes em um dia ou clientes que chegam a uma fila em determinado período.

### Parâmetro

O único parâmetro da distribuição é `λ` (lambda), que representa o número médio de ocorrências no intervalo considerado. Para uma variável aleatória `X` com distribuição de Poisson, escrevemos:

```text
X ~ Poisson(λ)
```

O valor de `λ` deve ser positivo. Na distribuição de Poisson:

```text
E(X) = λ
Var(X) = λ
DP(X) = √λ
```

Assim, a média e a variância possuem o mesmo valor.

### Função de probabilidade

A probabilidade de ocorrerem exatamente `k` eventos é calculada por:

```text
P(X = k) = (e^(-λ) · λ^k) / k!
```

em que:

- `k = 0, 1, 2, ...` é o número de ocorrências;
- `λ` é a média esperada no intervalo;
- `e ≈ 2,71828` é a constante de Euler;
- `k!` é o fatorial de `k`.

### Exemplo

Uma central recebe, em média, 3 chamadas por minuto. Qual é a probabilidade de receber exatamente 5 chamadas em um minuto?

Nesse caso, `λ = 3` e `k = 5`:

```text
P(X = 5) = (e^(-3) · 3^5) / 5!
		 ≈ 0,1008
```

Logo, a probabilidade é de aproximadamente **10,08%**.

### Probabilidades acumuladas

Para calcular probabilidades de vários valores, somamos as probabilidades individuais:

```text
P(X ≤ k) = P(X = 0) + P(X = 1) + ... + P(X = k)
```

As demais situações podem ser obtidas pelo complemento:

```text
P(X > k) = 1 - P(X ≤ k)
P(X ≥ k) = 1 - P(X ≤ k - 1)
P(a ≤ X ≤ b) = P(X ≤ b) - P(X ≤ a - 1)
```

### Relação com a distribuição binomial

A distribuição de Poisson pode aproximar uma distribuição binomial quando `n` é grande, `p` é pequeno e `λ = n · p`. Ela é especialmente útil quando contar diretamente todas as combinações da binomial seria trabalhoso.

Ao resolver um problema, primeiro identifique a unidade do intervalo, determine a taxa média `λ`, defina o número de ocorrências `k` e então aplique a fórmula adequada.
