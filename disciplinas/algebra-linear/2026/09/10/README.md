# Encontro 2026/09/10 - Algebra Linear

## Matriz Inversa

Uma matriz quadrada `A` é invertível quando existe uma matriz `A⁻¹` tal que:

```text
A · A⁻¹ = A⁻¹ · A = I
```

Nesse caso, `I` é a matriz identidade de mesma ordem que `A`. A matriz inversa desfaz a transformação realizada por `A`.

### Condição de existência

Uma matriz quadrada possui inversa se, e somente se, seu determinante for diferente de zero:

```text
det(A) ≠ 0
```

Quando `det(A) = 0`, a matriz é chamada singular e não possui inversa.

### Matriz `2 × 2`

Para

```text
A = [ a  b ]
	[ c  d ]
```

temos:

```text
			 1       [  d  -b ]
A⁻¹ = ------------- · [ -c   a ]
		   ad - bc
```

desde que `ad - bc ≠ 0`. O procedimento consiste em trocar os elementos da diagonal principal, trocar os sinais da diagonal secundária e dividir tudo pelo determinante.

### Método de Gauss-Jordan

Para calcular a inversa de uma matriz de ordem maior, constrói-se a matriz aumentada `[A | I]` e aplicam-se operações elementares nas linhas até obter `[I | A⁻¹]`:

```text
[ A | I ]  →  [ I | A⁻¹ ]
```

As operações permitidas são:

1. trocar duas linhas;
2. multiplicar uma linha por um número real não nulo;
3. somar a uma linha um múltiplo de outra linha.

Se não for possível transformar o bloco esquerdo em `I`, então `A` não é invertível.

### Propriedades

- `(A⁻¹)⁻¹ = A`;
- `(AB)⁻¹ = B⁻¹A⁻¹`;
- `(Aᵀ)⁻¹ = (A⁻¹)ᵀ`;
- `det(A⁻¹) = 1 / det(A)`.

### Sistemas lineares

Um sistema `A x = b`, com `A` invertível, pode ser resolvido multiplicando ambos os lados por `A⁻¹`:

```text
A x = b
A⁻¹ A x = A⁻¹ b
x = A⁻¹ b
```

Assim, o sistema possui uma única solução. Na prática, o método de Gauss costuma ser preferível ao cálculo explícito de `A⁻¹`, especialmente para matrizes grandes.
