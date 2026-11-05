# Encontro 2026/11/05 - Algebra Linear

## Transformacoes lineares

Uma transformacao linear, tambem chamada de aplicacao linear, e uma funcao entre espacos vetoriais sobre o mesmo corpo que preserva as operacoes de soma e multiplicacao por escalar.

Se `T: V -> W`, entao `T` e linear quando, para quaisquer `u, v` em `V` e qualquer escalar `a`,

```text
T(u + v) = T(u) + T(v)
T(a v) = a T(v)
```

Essas duas propriedades podem ser resumidas pela preservacao de combinacoes lineares:

```text
T(a u + b v) = a T(u) + b T(v)
```

Assim, uma transformacao linear nao desloca a origem. De fato:

```text
T(0) = 0
T(-v) = -T(v)
```

### Exemplos e contraexemplo

Sao exemplos de transformacoes lineares:

- `T(x) = 3x`, de `R` em `R`;
- `T(x, y) = x + y`, de `R^2` em `R`;
- `T(x, y) = (3x + y, 2x - 2y)`, de `R^2` em `R^2`;
- a derivacao `f -> f'`, do espaco das funcoes derivaveis para o espaco das funcoes reais.

A funcao `T(x) = x + c`, com `c` diferente de zero, nao e linear, pois `T(0) = c` e nao `0`. No caso de funcoes reais, uma reta `y = ax` e linear; ja `y = ax + b`, com `b` diferente de zero, e uma funcao afim.

### Nucleo e imagem

O nucleo de `T` e o conjunto dos vetores do dominio que sao enviados ao vetor nulo do contradominio:

```text
Ker(T) = {v em V | T(v) = 0}
```

A imagem de `T` e o conjunto de todos os vetores que podem ser obtidos pela transformacao:

```text
Im(T) = {T(v) | v em V}
```

O nucleo e um subespaco de `V`, e a imagem e um subespaco de `W`. Alem disso:

```text
T e injetiva  <=>  Ker(T) = {0}
T e sobrejetiva <=> Im(T) = W
```

Quando `T` e injetiva e sobrejetiva ao mesmo tempo, ela e bijetiva e recebe o nome de isomorfismo. Se o dominio e o contradominio sao o mesmo espaco, `T` e um endomorfismo ou operador linear.

### Teorema do posto e da nulidade

Se `V` tem dimensao finita, entao:

```text
dim(V) = dim(Ker(T)) + dim(Im(T))
```

Isso significa que a dimensao do dominio se divide entre a nulidade, isto e, a dimensao do nucleo, e o posto, que e a dimensao da imagem. Para um operador de um espaco finito nele mesmo, ser injetivo, sobrejetivo ou bijetivo sao condicoes equivalentes.

### Representacao por matrizes

Depois que bases sao escolhidas, toda transformacao linear de `R^n` em `R^m` pode ser representada por uma matriz `A`:

```text
T(x) = A x
```

O nucleo corresponde as solucoes de `A x = 0`, e a imagem e o subespaco gerado pelas colunas de `A`.

Considere:

```text
T(x, y) = (x + y, x - y)

A = [ 1   1 ]
    [ 1  -1 ]
```

Para determinar o nucleo, resolvemos:

```text
x + y = 0
x - y = 0
```

A unica solucao e `(x, y) = (0, 0)`. Portanto, `Ker(T) = {(0, 0)}`. Pelo teorema do posto e da nulidade, a imagem tem dimensao 2 e coincide com `R^2`; logo, `T` e bijetiva. Sua inversa e:

```text
T^(-1)(r, s) = ((r + s)/2, (r - s)/2)
```

### Transformacoes geometricas em `R^2`

Rotacoes, reflexoes e projecoes sao exemplos importantes de transformacoes lineares. Algumas matrizes associadas sao:

```text
Rotacao de 90 graus:
[ 0  -1 ]
[ 1   0 ]

Reflexao no eixo x:
[ 1   0 ]
[ 0  -1 ]

Reflexao no eixo y:
[-1   0 ]
[ 0   1 ]

Projecao no eixo y:
[ 0   0 ]
[ 0   1 ]
```

Por exemplo, a projecao `P(x, y) = (0, y)` tem como nucleo o eixo `x` e como imagem o eixo `y`. Ela nao e injetiva em `R^2`, pois pontos diferentes do mesmo alinhamento vertical podem ter a mesma imagem.

## Autovalor e autovetor

Considere um operador linear `T: V -> V`. Um vetor nao nulo `v` e um autovetor de `T` quando a aplicacao transforma `v` em um multiplo dele proprio:

```text
T(v) = lambda v, com v diferente de 0
```

O escalar `lambda` e o autovalor associado a `v`. Em outras palavras, um autovetor mantem sua direcao depois da transformacao; o autovalor indica como seu comprimento e sentido sao alterados:

- se `lambda > 1`, o vetor e ampliado;
- se `0 < lambda < 1`, o vetor e reduzido;
- se `lambda = 1`, o vetor permanece inalterado;
- se `lambda = 0`, o vetor e enviado ao vetor nulo;
- se `lambda < 0`, alem da alteracao de escala, o sentido e invertido.

Para uma matriz quadrada `A`, a equacao de autovalor e:

```text
A v = lambda v
```

Reorganizando os termos, obtemos:

```text
(A - lambda I)v = 0
```

Como `v` deve ser diferente de zero, o sistema homogeneo precisa ter solucoes nao triviais. Isso acontece quando a matriz `A - lambda I` e singular, isto e, quando seu determinante e zero:

```text
det(A - lambda I) = 0
```

A expressao `p(lambda) = det(A - lambda I)` e chamada de polinomio caracteristico. Suas raizes sao os autovalores de `A`.

### Exemplo de calculo

Considere a matriz:

```text
A = [ 3  1 ]
        [ 0  2 ]
```

O polinomio caracteristico e:

```text
det(A - lambda I) = det([ 3 - lambda   1       ])
                                        det([ 0             2-lambda])
                                    = (3 - lambda)(2 - lambda)
```

Logo, os autovalores sao `lambda = 3` e `lambda = 2`.

Para `lambda = 3`, resolvemos `(A - 3I)v = 0`:

```text
[ 0  1 ] [x] = [0]
[ 0 -1 ] [y]   [0]
```

Assim, `y = 0` e `x` pode ser qualquer numero. Os autovetores associados a `lambda = 3` sao os vetores nao nulos da forma:

```text
v = (x, 0), com x diferente de 0
```

Para `lambda = 2`, resolvemos `(A - 2I)v = 0`:

```text
[ 1  1 ] [x] = [0]
[ 0  0 ] [y]   [0]
```

Nesse caso, `x + y = 0`, portanto os autovetores associados a `lambda = 2` sao os vetores nao nulos da forma:

```text
v = (x, -x), com x diferente de 0
```

### Espaco proprio e multiplicidades

Para um autovalor `lambda`, o espaco proprio associado e o conjunto formado pelo vetor nulo e por todos os autovetores correspondentes:

```text
E_lambda = Ker(A - lambda I)
```

O autovalor pode aparecer mais de uma vez como raiz do polinomio caracteristico. O numero de ocorrencias e sua multiplicidade algebrica. A dimensao do espaco proprio e a multiplicidade geometrica. Sempre vale:

```text
1 <= multiplicidade geometrica <= multiplicidade algebrica
```

Uma matriz `n x n` e diagonalizavel quando possui uma base formada por `n` autovetores linearmente independentes. Nesse caso, existe uma matriz invertivel `P` e uma matriz diagonal `D` tais que:

```text
A = P D P^(-1)
```

As colunas de `P` sao autovetores de `A`, e os elementos da diagonal de `D` sao os autovalores correspondentes.

## Referencias

- WIKIPEDIA. [Transformacao linear](https://pt.wikipedia.org/wiki/Transforma%C3%A7%C3%A3o_linear). Acesso em: 5 nov. 2026.
- WIKIPEDIA. [Autovalor e autovetor](https://pt.wikipedia.org/wiki/Autovalor_e_autovetor). Acesso em: 5 nov. 2026.
- UNIVERSIDADE FEDERAL DO RIO GRANDE DO SUL. Instituto de Matematica e Estatistica. [Transformacoes lineares e exemplos](https://www.ufrgs.br/reamat/AlgebraLinear/livro/s3-transformax00e7x00f5es_lineares.html). Acesso em: 5 nov. 2026.
- LIMA, Elon Lages. *Algebra Linear*. 9. ed. Rio de Janeiro: IMPA, 2016.
