# Encontro 2026/11/12 - Algebra Linear

## Autovalor e Autovetor

Seja $T: V \to V$ um operador linear. Um escalar $\lambda$ é um **autovalor** de $T$ quando existe um vetor não nulo $v \in V$ tal que

$$T(v) = \lambda v.$$

O vetor $v$ é chamado de **autovetor** associado a $\lambda$. Para encontrar os autovalores de uma matriz quadrada $A$, resolvemos a equação característica

$$\det(A - \lambda I) = 0.$$

Depois, para cada autovalor, calculamos o espaço próprio correspondente, formado pelos vetores que satisfazem

$$\ker(A - \lambda I) = \{v \in V : (A - \lambda I)v = 0\}.$$

### Diagonalização de Operadores

A diagonalização consiste em representar uma matriz quadrada $A$ por meio de uma matriz diagonal semelhante:

$$A = PDP^{-1},$$

em que $D$ é diagonal e $P$ é uma matriz invertível. As colunas de $P$ são autovetores linearmente independentes de $A$, e os elementos da diagonal de $D$ são os autovalores correspondentes, na mesma ordem.

Uma matriz $A \\in M_n$ é diagonalizável se, e somente se, possui uma base de autovetores. Para diagonalizá-la, seguimos estes passos:

1. Encontramos os autovalores resolvendo $\\det(A - \\lambda I) = 0$.
2. Calculamos os espaços próprios $E_\\lambda = \\ker(A - \\lambda I)$.
3. Escolhemos uma base de autovetores em cada espaço próprio.
4. Formamos $P$ com esses autovetores como colunas e $D$ com os autovalores correspondentes na diagonal.

Se $A$ possui $n$ autovetores linearmente independentes, então $P$ é invertível e a diagonalização existe. Em particular, autovalores distintos produzem autovetores linearmente independentes; portanto, uma matriz com $n$ autovalores distintos é diagonalizável.

Por exemplo, se

$$A = P D P^{-1},$$

então as potências de $A$ podem ser calculadas facilmente por

$$A^k = P D^k P^{-1},$$

pois $D^k$ é obtida elevando cada elemento diagonal de $D$ à potência $k$.

## 
