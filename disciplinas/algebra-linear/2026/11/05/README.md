# Encontro 2026/11/05 - Algebra Linear

## Transformações Lineares

Uma transformação linear é uma função entre espaços vetoriais que preserva a soma de vetores e a multiplicação por escalares. Para uma transformação `T`, devem valer, para quaisquer vetores `u` e `v` e escalar `k`:

```text
T(u + v) = T(u) + T(v)
T(kv) = kT(v)
```

Essas propriedades podem ser reunidas em uma única expressão:

```text
T(au + bv) = aT(u) + bT(v)
```

onde `a` e `b` são escalares. Exemplos incluem rotações, reflexões, projeções e ampliações. Uma transformação linear de `R^n` em `R^m` pode ser representada por uma matriz `A`, de modo que `T(x) = Ax`.

### Núcleo e imagem

O núcleo de `T` é o conjunto dos vetores enviados ao vetor nulo:

```text
Ker(T) = {v | T(v) = 0}
```

A imagem é o conjunto de todos os vetores que podem ser obtidos por `T`:

```text
Im(T) = {T(v) | v pertence ao domínio}
```

Se `T` é representada por uma matriz `A`, o núcleo corresponde às soluções de `Ax = 0`, enquanto a imagem é o espaço gerado pelas colunas de `A`. Pelo teorema do posto e da nulidade:

```text
dim(Ker(T)) + dim(Im(T)) = dim(domínio de T)
```

Uma transformação é injetiva quando vetores diferentes têm imagens diferentes, o que equivale a `Ker(T) = {0}`. É sobrejetiva quando `Im(T)` coincide com o contradomínio. Quando é simultaneamente injetiva e sobrejetiva, ela é bijetiva e possui uma transformação inversa.

### Exemplos

Considere a transformação `T: R^2 -> R^2` definida por:

```text
T(x, y) = (x + y, x - y)
```

Ela é linear, pois, para quaisquer vetores `u` e `v` e escalares `a` e `b`, vale:

```text
T(au + bv) = aT(u) + bT(v)
```

A transformação pode ser representada pela matriz:

```text
A = [ 1  1 ]
	[ 1 -1 ]
```

Assim, `T(x, y) = A [x, y]^T`. Para encontrar o núcleo, resolvemos:

```text
x + y = 0
x - y = 0
```

A única solução é `x = y = 0`, portanto `Ker(T) = {(0, 0)}`. Como o núcleo tem dimensão zero e o domínio tem dimensão dois, o teorema do posto e da nulidade mostra que `dim(Im(T)) = 2`. Logo, a imagem é todo `R^2`, e `T` é injetiva, sobrejetiva e bijetiva.

Sua inversa pode ser obtida resolvendo `T(x, y) = (r, s)`:

```text
x = (r + s)/2
y = (r - s)/2
```

Portanto:

```text
T⁻¹(r, s) = ((r + s)/2, (r - s)/2)
```

Outro exemplo é a projeção no eixo `x`, dada por `P(x, y) = (x, 0)`. Nesse caso, `Ker(P)` é o eixo `y` e `Im(P)` é o eixo `x`. A projeção não é injetiva, pois diferentes vetores podem ter a mesma imagem, nem sobrejetiva em `R^2`, pois seus resultados sempre pertencem ao eixo `x`.
