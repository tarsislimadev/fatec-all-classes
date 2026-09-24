# Encontro 2026/09/24 - Algebra Linear

## Classificação de um Sistema Linear

### Sistema Possível e Determinado (SPD)

Possui uma única solução. Graficamente, as retas ou planos se intersectam em um único ponto.

### Sistema Possível e Indeterminado (SPI)

Possui infinitas soluções. As equações são compatíveis e representam a mesma reta, plano ou conjunto geométrico.

### Sistema Impossível (SI)

Não possui solução. As equações são incompatíveis, como retas paralelas distintas.

## Regra de Cramer

Método usado para resolver sistemas quadrados, isto é, com o mesmo número de equações e incógnitas, quando o determinante da matriz dos coeficientes é diferente de zero.

Para o sistema

```text
a₁x + b₁y = c₁
a₂x + b₂y = c₂
```

calcula-se o determinante principal:

```text
D = |a₁ b₁| = a₁b₂ - a₂b₁
	|a₂ b₂|
```

Em seguida, substitui-se a coluna de cada incógnita pelos termos independentes:

```text
Dx = |c₁ b₁|    Dy = |a₁ c₁|
	 |c₂ b₂|         |a₂ c₂|
```

As soluções são `x = Dx/D` e `y = Dy/D`. Se `D = 0`, a Regra de Cramer não determina uma solução única; o sistema pode ser SPI ou SI.

## Método da substituição

Isola-se uma incógnita em uma das equações e substitui-se essa expressão nas demais. Assim, obtém-se uma equação com uma única incógnita. Depois de encontrar seu valor, substitui-se novamente para calcular as outras incógnitas.

Por exemplo, em `x + y = 5` e `2x - y = 4`, isolando `y = 5 - x` e substituindo na segunda equação, temos `2x - (5 - x) = 4`, logo `x = 3` e `y = 2`.

## Método da adição

Somam-se ou subtraem-se equações para eliminar uma das incógnitas. Se necessário, multiplica-se uma ou mais equações por constantes antes da operação. Depois de obter o valor de uma incógnita, substitui-se esse valor em uma das equações originais para encontrar as demais.

No sistema `x + y = 5` e `2x - y = 4`, a soma das equações elimina `y`: `3x = 9`. Portanto, `x = 3` e, substituindo, `y = 2`.

## Escalonamento de matrizes

Representa-se o sistema por uma matriz aumentada e aplicam-se operações elementares nas linhas: trocar duas linhas, multiplicar uma linha por um número não nulo ou somar a uma linha um múltiplo de outra.

O objetivo é obter uma forma escalonada, com zeros abaixo dos pivôs. Em seguida, resolve-se o sistema por substituição regressiva. Uma linha como `[0 0 | c]`, com `c ≠ 0`, indica SI; uma linha totalmente nula indica que há uma dependência entre as equações. O número de pivôs permite identificar a classificação do sistema.
