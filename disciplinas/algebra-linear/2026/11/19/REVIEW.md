# Revisão de Álgebra Linear

## Identificação da disciplina

- Código: MAG020
- Professor: João Eichenberger Neto
- Horário: quinta-feira, das 11h20 às 13h00

## 1. Matrizes e operações

### Multiplicação

O produto \(AB\) existe quando o número de colunas de \(A\) é igual ao número de linhas de \(B\). Se \(A\) tem dimensão \(m \times n\) e \(B\) tem dimensão \(n \times p\), então \(AB\) tem dimensão \(m \times p\). Em geral, a multiplicação não é comutativa:

\[
AB \neq BA.
\]

Na multiplicação por escalar, cada elemento da matriz ou vetor é multiplicado pelo escalar. A operação preserva as dimensões e satisfaz as propriedades distributiva e associativa.

### Matriz identidade

A matriz identidade \(I_n\) é quadrada, possui 1 na diagonal principal e 0 nos demais elementos. Ela é o elemento neutro:

\[
AI_n = I_nA = A.
\]

Também vale \(I_n^{-1}=I_n\), \(I_n^T=I_n\) e \(\det(I_n)=1\).

Não há uma divisão matricial definida como na aritmética comum. Quando possível, a operação equivalente é a multiplicação pela inversa, respeitando a ordem dos fatores:

\[
A/B \text{ (à direita) } = AB^{-1}, \qquad
B\backslash A \text{ (à esquerda) } = B^{-1}A.
\]

## 2. Determinantes e inversas

O determinante é definido para matrizes quadradas e ajuda a verificar invertibilidade e a classificar sistemas.

Para uma matriz \(2 \times 2\):

\[
\det\begin{pmatrix}a&b\\c&d\end{pmatrix}=ad-bc.
\]

Para uma matriz \(3 \times 3\), pode-se usar a Regra de Sarrus. Em geral, a expansão de Laplace usa os cofatores:

\[
C_{ij}=(-1)^{i+j}M_{ij},
\]

em que \(M_{ij}\) é o menor complementar. O padrão de sinais dos cofatores é alternado:

\[
\begin{pmatrix}
 +&-&+&\cdots\\
 -&+&-&\cdots\\
 +&-&+&\cdots
\end{pmatrix}.
\]

O determinante pode ser calculado expandindo por qualquer linha ou coluna:

\[
\det(A)=\sum_j a_{ij}C_{ij}
       =\sum_i a_{ij}C_{ij}.
\]

Uma matriz quadrada \(A\) é invertível se, e somente se, \(\det(A)\neq0\). Nesse caso:

\[
AA^{-1}=A^{-1}A=I.
\]

Para uma matriz \(2 \times 2\):

\[
\begin{pmatrix}a&b\\c&d\end{pmatrix}^{-1}
=\frac{1}{ad-bc}
\begin{pmatrix}d&-b\\-c&a\end{pmatrix}.
\]

Para ordens maiores, o método de Gauss-Jordan transforma a matriz aumentada
\([A\mid I]\) em \([I\mid A^{-1}]\) por operações elementares nas linhas. As principais propriedades são:

- \((AB)^{-1}=B^{-1}A^{-1}\);
- \((A^T)^{-1}=(A^{-1})^T\);
- \(\det(A^{-1})=1/\det(A)\).

## 3. Sistemas lineares

Um sistema pode ser escrito como:

\[
AX=B,
\]

em que \(A\) é a matriz dos coeficientes, \(X\) é o vetor das incógnitas e \(B\) é o vetor dos termos independentes.

### Classificação

- SPD (sistema possível e determinado): possui uma única solução.
- SPI (sistema possível e indeterminado): possui infinitas soluções.
- SI (sistema impossível): não possui solução.

Um sistema homogêneo sempre possui pelo menos a solução nula; portanto, não pode ser impossível.

### Métodos de resolução

- Substituição: isolar uma incógnita e substituí-la nas outras equações.
- Adição: combinar equações para eliminar uma incógnita.
- Escalonamento: aplicar operações elementares à matriz aumentada e usar substituição regressiva.
- Matriz inversa: quando \(A\) é invertível, \(X=A^{-1}B\).
- Regra de Cramer: para sistemas quadrados com \(D=\det(A)\neq0\), substituir cada coluna de \(A\) por \(B\) e calcular \(x_i=D_i/D\). É mais adequada para sistemas pequenos.

No escalonamento, uma linha \([0\ 0\mid c]\), com \(c\neq0\), indica SI. Linhas nulas indicam dependência entre equações; o número de pivôs auxilia na classificação.

## 4. Combinação e dependência linear

Uma combinação linear de \(v_1,\ldots,v_n\) é:

\[
a_1v_1+\cdots+a_nv_n.
\]

O conjunto de todas essas combinações é o espaço gerado (*span*).

Os vetores são linearmente dependentes quando existe uma combinação não trivial igual ao vetor nulo. São linearmente independentes quando a única combinação que resulta em zero possui todos os coeficientes nulos.

## 5. Transformações lineares

Uma transformação \(T:V\to W\) é linear quando:

\[
T(u+v)=T(u)+T(v),\qquad T(av)=aT(v).
\]

Consequentemente, \(T(0)=0\) e \(T\) preserva combinações lineares. Uma função com termo constante não nulo, como \(T(x)=x+c\), não é linear.

O núcleo e a imagem são:

\[
\ker(T)=\{v\in V:T(v)=0\},\qquad
\operatorname{Im}(T)=\{T(v):v\in V\}.
\]

- \(T\) é injetiva se, e somente se, \(\ker(T)=\{0\}\).
- \(T\) é sobrejetiva se, e somente se, \(\operatorname{Im}(T)=W\).
- Se for simultaneamente injetiva e sobrejetiva, é bijetiva (um isomorfismo).

O teorema do posto e da nulidade afirma:

\[
\dim(V)=\dim(\ker T)+\dim(\operatorname{Im}T).
\]

Depois da escolha de bases, uma transformação de \(\mathbb{R}^n\) em \(\mathbb{R}^m\) pode ser representada por \(T(x)=Ax\). Rotação, reflexão e projeção são exemplos geométricos importantes.

## 6. Autovalores, autovetores e diagonalização

Para um operador \(T:V\to V\), um vetor não nulo \(v\) é autovetor associado ao autovalor \(\lambda\) quando:

\[
T(v)=\lambda v.
\]

Para uma matriz \(A\), os autovalores são encontrados pela equação característica:

\[
\det(A-\lambda I)=0.
\]

Para cada autovalor, o espaço próprio é:

\[
E_\lambda=\ker(A-\lambda I).
\]

A multiplicidade algébrica é o número de vezes que o autovalor aparece no polinômio característico. A multiplicidade geométrica é a dimensão do espaço próprio, e sempre:

\[
1\leq m_g\leq m_a.
\]

Uma matriz \(n\times n\) é diagonalizável quando possui \(n\) autovetores linearmente independentes, isto é, uma base de autovetores. Nesse caso:

\[
A=PDP^{-1},
\]

em que as colunas de \(P\) são os autovetores e \(D\) contém os autovalores correspondentes na diagonal. Autovalores distintos produzem autovetores linearmente independentes. A diagonalização também simplifica potências:

\[
A^k=PD^kP^{-1}.
\]

## 7. Exercícios em JavaScript

Foram registrados dois exercícios de entrada de matrizes quadradas:

- `size.js`: lê a ordem e todos os elementos de uma matriz, exibindo os valores informados.
- `inverse.js`: valida a matriz, monta \([A\mid I]\), aplica Gauss-Jordan com escolha de pivô e retorna a inversa. Rejeita matrizes vazias, não quadradas, com valores não finitos ou singulares.

## Checklist para a prova

- [ ] Verificar a compatibilidade das dimensões antes de multiplicar matrizes.
- [ ] Calcular determinantes \(2\times2\) e \(3\times3\), incluindo sinais dos cofatores.
- [ ] Identificar quando uma matriz é invertível e aplicar Gauss-Jordan.
- [ ] Escrever sistemas na forma \(AX=B\) e classificá-los como SPD, SPI ou SI.
- [ ] Resolver sistemas por substituição, adição, escalonamento e Cramer.
- [ ] Testar combinação e dependência linear.
- [ ] Determinar núcleo, imagem, posto e nulidade de uma transformação.
- [ ] Encontrar autovalores, espaços próprios e verificar diagonalização.
