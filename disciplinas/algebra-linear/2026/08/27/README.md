# Encontro 2026/08/27 - Algebra Linear

## Determinante

É um número calculado a partir dos elementos de uma matriz quadrada.

O determinante é utilizado na Algebra Linear como discriminante em algumas situações.

A "diagonal principal" menos a "diagonal secundária".

### Exemplo (matriz quadrada de ordem 2)

Para calcular o determinante de uma matriz $2 \times 2$:

$$\begin{vmatrix} a & b \\ c & d \end{vmatrix} = (a \cdot d) - (b \cdot c)$$

**Exemplo Prático:**
Seja a matriz $M = \begin{vmatrix} 3 & 5 \\ 1 & 4 \end{vmatrix}$:

$\text{det}(M) = (3 \cdot 4) - (5 \cdot 1)$
$\text{det}(M) = 12 - 5$
$\text{det}(M) = 7$

### Exemplo (matriz quadrada de ordem 3)

Para matrizes de ordem 3, o método mais comum é a **Regra de Sarrus**.

**Passo a passo:**
1. Repita as duas primeiras colunas da matriz à direita dela.
2. Some os produtos das três diagonais principais.
3. Subtraia os produtos das três diagonais secundárias.

**Exemplo Prático:**
Seja a matriz $M = \begin{vmatrix} 1 & 2 & 3 \\ 0 & 1 & 4 \\ 5 & 6 & 0 \end{vmatrix}$

Expandindo as colunas:
$\begin{vmatrix} 1 & 2 & 3 \\ 0 & 1 & 4 \\ 5 & 6 & 0 \end{vmatrix} \begin{matrix} 1 & 2 \\ 0 & 1 \\ 5 & 6 \end{matrix}$

Cálculo:
$\text{det}(M) = [(1\cdot 1\cdot 0) + (2\cdot 4\cdot 5) + (3\cdot 0\cdot 6)] - [(3\cdot 1\cdot 5) + (1\cdot 4\cdot 6) + (2\cdot 0\cdot 0)]$
$\text{det}(M) = [0 + 40 + 0] - [15 + 24 + 0]$
$\text{det}(M) = 40 - 39$
$\text{det}(M) = 1$
