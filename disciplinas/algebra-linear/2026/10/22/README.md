# Encontro 2026/10/22 - Algebra Linear

## Combinação Linear

Uma **combinação linear** de vetores $v_1, v_2, \ldots, v_n$ é uma expressão da forma

$$a_1v_1 + a_2v_2 + \cdots + a_nv_n,$$

em que $a_1, a_2, \ldots, a_n$ são escalares. Esses escalares são chamados de coeficientes da combinação linear. Por exemplo, $3u - 2v$ é uma combinação linear dos vetores $u$ e $v$.

O conjunto de todas as combinações lineares de um conjunto de vetores é o **subespaço gerado** por eles, também chamado de espaço gerado ou *span*.

## Dependencia Linear

Um conjunto de vetores $v_1, v_2, \ldots, v_n$ é **linearmente dependente** quando existem escalares $a_1, a_2, \ldots, a_n$, não todos nulos, tais que

$$a_1v_1 + a_2v_2 + \cdots + a_nv_n = 0.$$

Isso significa que pelo menos um dos vetores pode ser escrito como combinação linear dos demais. O conjunto é **linearmente independente** quando a única solução da equação acima é

$$a_1 = a_2 = \cdots = a_n = 0.$$

Por exemplo, os vetores $(1, 0)$ e $(0, 1)$ são linearmente independentes. Já $(1, 2)$ e $(2, 4)$ são linearmente dependentes, pois o segundo é o dobro do primeiro.
