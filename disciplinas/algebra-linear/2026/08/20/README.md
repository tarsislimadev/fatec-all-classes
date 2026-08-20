# Encontro 2026/08/20 - Algebra Linear

## Multiplicação de Matrizes

A "multiplicação de matrizes" é uma operação binária que resulta em uma nova matriz (produto) cujos elementos são calculados pela soma dos produtos dos elementos correspondentes das linhas da primeira matriz e das colunas da segunda matriz.

Para que a operação seja possível, deve-se respeitar a "condição de existência": o número de "colunas da primeira matriz" deve ser igual ao número de "linhas da segunda matriz".

### Características Principais

*   "Dimensão do Resultado": Se a primeira matriz tem dimensão $m \times n$ e a segunda $n \times p$, a matriz produto resultante terá dimensão "$m \times p$" (linhas da primeira $\times$ colunas da segunda).
*   "Não Comutatividade": Em geral, a ordem importa, ou seja, "$A \cdot B \neq B \cdot A$".
*   "Multiplicação por Escalar": Quando se multiplica uma matriz por um número real $k$, este é multiplicado por "cada elemento" individual da matriz.

### Exemplo de Cálculo

Considere as matrizes $A_{2 \times 2}$ e $B_{2 \times 2}$:

$$
A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}, \quad B = \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}
$$

O produto $C = A \cdot B$ resulta em uma matriz $2 \times 2$, onde o elemento $c_{11}$ é calculado como:

$$
c_{11} = (1 \cdot 5) + (2 \cdot 7) = 5 + 14 = 19
$$

O processo se repete para cada combinação de linha e coluna.
