# Encontro 2026/09/17 - Algebra Linear

## Sistemas Lineares - Cramer

https://www.youtube.com/playlist?list=PLJaV5A58zvnM

## Regra de Cramer

A Regra de Cramer resolve sistemas lineares quadrados, isto é, sistemas com o mesmo número de equações e incógnitas, por meio de determinantes.

Considere o sistema

```text
a₁₁x₁ + a₁₂x₂ + ... + a₁ₙxₙ = b₁
a₂₁x₁ + a₂₂x₂ + ... + a₂ₙxₙ = b₂
				 ⋮
aₙ₁x₁ + aₙ₂x₂ + ... + aₙₙxₙ = bₙ
```

Escreva-o na forma matricial `A · X = B`, em que `A` é a matriz dos coeficientes, `X` é o vetor das incógnitas e `B` é o vetor dos termos independentes. Calcule `D = det(A)`.

- Se `D ≠ 0`, o sistema possui uma única solução. Para cada incógnita `xᵢ`, substitua a coluna `i` de `A` pelo vetor `B`, calcule o determinante `Dᵢ` e use `xᵢ = Dᵢ / D`.
- Se `D = 0`, a Regra de Cramer não determina uma solução única. O sistema pode ser impossível ou possuir infinitas soluções; nesse caso, analise-o por escalonamento ou pelo teorema de Rouché-Capelli.

### Exemplo

Para o sistema

```text
2x + y = 5
x  - y = 1
```

temos

```text
A = | 2  1 |    B = | 5 |    D = det(A) = -3
	| 1 -1 |        | 1 |
```

Substituindo a primeira coluna por `B`, `Dₓ = -6`, portanto `x = Dₓ/D = 2`. Substituindo a segunda coluna, `Dᵧ = -3`, portanto `y = Dᵧ/D = 1`. Logo, a solução é `(x, y) = (2, 1)`.

O método é direto e funciona bem para sistemas pequenos, mas pode exigir muitos cálculos para matrizes grandes. Sempre verifique a solução substituindo seus valores nas equações originais.
