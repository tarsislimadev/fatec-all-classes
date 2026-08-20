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
* "Cálculo:" Multiplica-se o escalar $k$ por cada componente do vetor.

* "Exemplo:" Se $\vec{A} = 5\mathbf{i} - 2\mathbf{j} + 3\mathbf{k}$ e $k = 4$, o resultado é $\vec{R} = 20\mathbf{i} - 8\mathbf{j} + 12\mathbf{k}$.


### Matrizes
A multiplicação de uma matriz por um escalar resulta em uma nova matriz de mesmas dimensões, onde cada elemento foi multiplicado pelo valor do escalar.
* "Definição:" Se $A$ é uma matriz e $k$ é um escalar, o produto $k \cdot A$ tem elementos $b_{ij} = k \cdot a_{ij}$.

* "Propriedades:" Incluem a distributividade ($k(A+B) = kA + kB$) e a associatividade ($(k \cdot m)A = k(mA)$).


## Matriz Identidade

A "matriz identidade" é uma matriz quadrada fundamental na álgebra linear, atuando como o "elemento neutro da multiplicação de matrizes". Isso significa que, ao multiplicar qualquer matriz $A$ pela matriz identidade $I$, o resultado é a própria matriz $A$, sem alterações.

### Definição e Estrutura

Uma matriz é classificada como identidade quando atende a dois critérios específicos de construção:
1.  Todos os elementos da "diagonal principal" (do canto superior esquerdo ao inferior direito) são iguais a "1".
2.  Todos os demais elementos (fora da diagonal principal) são iguais a "0".

Ela é geralmente denotada por $I_n$, onde $n$ representa a ordem da matriz (número de linhas e colunas). Diferente de outras matrizes que exigem regras complexas para sua formação, a matriz identidade depende apenas da sua ordem.

### Exemplos por Ordem

A estrutura da matriz varia conforme a sua dimensão $n \times n$:

* "Ordem 1 ($I_1$):"

$$I_1 = [1]$$

* "Ordem 2 ($I_2$):"

$$I_2 = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$$

* "Ordem 3 ($I_3$):"

$$I_3 = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$

* "Forma Geral ($I_n$):"

$$I_n = \begin{bmatrix} 1 & 0 & \cdots & 0 \\ 0 & 1 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 1 \end{bmatrix}$$

### Propriedades Principais

A matriz identidade possui propriedades únicas que a tornam essencial para operações matriciais:

"Elemento Neutro da Multiplicação"

Assim como o número 1 na aritmética comum, a matriz identidade não altera o valor de outra matriz no produto. Para qualquer matriz quadrada $A$ de ordem $n$:
$$A \cdot I_n = I_n \cdot A = A$$

"Relação com a Matriz Inversa"

O conceito de matriz identidade é central para definir a inversão de matrizes. O produto de uma matriz quadrada $A$ pela sua inversa $A^{-1}$ resulta sempre na matriz identidade:
$$A \cdot A^{-1} = A^{-1} \cdot A = I_n$$
Isso implica que a inversa da própria matriz identidade é ela mesma ($I^{-1} = I$).

"Matriz Transposta"

A matriz identidade é simétrica, o que significa que a sua transposta é igual a ela mesma:
$$I^T = I$$

"Determinante"

O determinante de qualquer matriz identidade, independentemente da sua ordem, é sempre igual a "1".

### Utilidade Prática

Além de servir como referência teórica, a matriz identidade é uma ferramenta prática na resolução de "equações matriciais". Como não existe operação de divisão entre matrizes, utiliza-se a multiplicação pela inversa para isolar variáveis.

Por exemplo, na equação $M \cdot A = B$, para encontrar $M$, multiplica-se ambos os lados por $A^{-1}$:
$$M \cdot A \cdot A^{-1} = B \cdot A^{-1}$$
$$M \cdot I = B \cdot A^{-1}$$
$$M = B \cdot A^{-1}$$

Neste processo, a transformação de $A \cdot A^{-1}$ em $I$ e a subsequente simplificação de $M \cdot I$ para $M$ são passos cruciais habilitados pelas propriedades da matriz identidade.
