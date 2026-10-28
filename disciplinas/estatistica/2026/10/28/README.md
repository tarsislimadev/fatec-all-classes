# Encontro 2026/10/28 - Estatística

## Distribuição de Probabilidade

Organizar todos os valores possíveis de uma variável aleatória e associar a cada valor a probabilidade de ele ocorrer.

### Variável Aleatória (V.A.)

Associa um valor numérico ao resultado de um fenômeno aleatóorio

i) V.A. discreta

assume valores que podem ser contados

ii) V.A. contínua

assume valores dentro de um intervalo (valores decimais)

### Exemplo

Uma loja acompanha a quantidade de vendas realizadas durante um intervalo de 30 minutos.

## [Distribuição de Bernoulli](https://pt.wikipedia.org/wiki/Distribui%C3%A7%C3%A3o_de_Bernoulli)

Modelo mais simples e a base para decisões sob incerteza.

Modela cenários onde existe apenas 2 resultados possíveis:

`sucesso` (o evento acontece) ou `fracasso` (o evento não acontece)

### Resultados possíveis

- 1 (sucesso): probabilidade `p`

- 0 (fracasso): probabilidade `1 - p = q`

## Distribuição Binomial

`n` ensaios de Bernoulli

Responde a pergunta: "Qual é a probabilidade de um resultado acontecer `k` vezes em um total de `n` tentativas?"

### Fórmula Binomial

A distribuição binomial calcula a probabilidade de ocorrer exatamente `k` sucessos em `n` tentativas independentes, em que cada tentativa tem probabilidade `p` de sucesso.

`P(X = k) = C(n, k) · p^k · (1 - p)^(n - k)`

Onde:

- `n` = número total de ensaios
- `k` = número de sucessos desejados
- `p` = probabilidade de sucesso em cada ensaio
- `C(n, k)` = número de combinações possíveis de `k` sucessos em `n` tentativas

Em outras palavras, a fórmula multiplica a chance de ter `k` sucessos, considera a chance de falha nos demais ensaios e conta quantas maneiras diferentes esse resultado pode acontecer.

