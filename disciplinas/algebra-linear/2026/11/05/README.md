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

<!-- Fonte consultada: [Transformacao linear - Wikipedia](https://pt.wikipedia.org/wiki/Transforma%C3%A7%C3%A3o_linear), acesso em 2026-11-05. -->
