# Encontro 2026/08/20 - Algebra Linear

## Multiplicação de Matrizes

A "multiplicação de matrizes" é uma operação binária que resulta em uma nova matriz (produto) cujos elementos são calculados pela soma dos produtos dos elementos correspondentes das linhas da primeira matriz e das colunas da segunda matriz.

Para que a operação seja possível, deve-se respeitar a "condição de existência": o número de "colunas da primeira matriz" deve ser igual ao número de "linhas da segunda matriz".

### Características Principais

* "Dimensão do Resultado": Se a primeira matriz tem dimensão $m \times n$ e a segunda $n \times p$, a matriz produto resultante terá dimensão "$m \times p$" (linhas da primeira $\times$ colunas da segunda).
* "Não Comutatividade": Em geral, a ordem importa, ou seja, "$A \cdot B \neq B \cdot A$".
* "Multiplicação por Escalar": Quando se multiplica uma matriz por um número real $k$, este é multiplicado por "cada elemento" individual da matriz.

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

## Divisão de matrizes

Divisão de matrizes

Tecnicamente, "não existe definição para divisão de matrizes", pois a operação não é comutativa e nem todas as matrizes possuem inversa. O processo equivalente é a "multiplicação da primeira matriz pelo inverso da segunda", representado como $A \cdot B^{-1}$.

Para realizar essa operação, a matriz divididora ($B$) deve ser "quadrada e não-singular" (determinante diferente de zero). Como a multiplicação de matrizes não é comutativa, é necessário distinguir entre:
* "Divisão à esquerda": $B^{-1} \cdot A$ (solução para $Bx = A$).
* "Divisão à direita": $A \cdot B^{-1}$ (solução para $xB = A$).

Se a intenção é dividir cada elemento de uma matriz por um número real, trata-se de uma "multiplicação por escalar" (ou matriz $1 \times 1$), onde cada elemento da matriz é dividido individualmente pelo número.

## Multiplicação por escalar

A "multiplicação por escalar" é uma operação fundamental na álgebra linear que consiste em multiplicar cada elemento de um vetor ou matriz por um número real (o escalar).

### Vetores
Ao multiplicar um vetor por um escalar, altera-se a sua magnitude (comprimento) sem mudar sua direção, ou inverte-se a direção se o escalar for negativo.
*   "Cálculo:" Multiplica-se o escalar $k$ por cada componente do vetor.
*   "Exemplo:" Se $\vec{A} = 5\mathbf{i} - 2\mathbf{j} + 3\mathbf{k}$ e $k = 4$, o resultado é $\vec{R} = 20\mathbf{i} - 8\mathbf{j} + 12\mathbf{k}$.

### Matrizes
A multiplicação de uma matriz por um escalar resulta em uma nova matriz de mesmas dimensões, onde cada elemento foi multiplicado pelo valor do escalar.
*   "Definição:" Se $A$ é uma matriz e $k$ é um escalar, o produto $k \cdot A$ tem elementos $b_{ij} = k \cdot a_{ij}$.
*   "Propriedades:" Incluem a distributividade ($k(A+B) = kA + kB$) e a associatividade ($(k \cdot m)A = k(mA)$).
