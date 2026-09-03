# Encontro 2026/09/03 - Algebra Linear

## Co-fator algébrico

O **co-fator algébrico** (ou complemento algébrico) de um elemento `aᵢⱼ` de uma matriz é definido por

`Cᵢⱼ = (-1)ⁱ⁺ʲ · Mᵢⱼ`

em que `Mᵢⱼ` é o **menor complementar**: o determinante da matriz obtida ao eliminar a linha `i` e a coluna `j` da matriz original. O fator `(-1)ⁱ⁺ʲ` determina o sinal do co-fator, seguindo o padrão de sinais:

```text
+  -  +  -  ...
-  +  -  +  ...
+  -  +  -  ...
```

Por exemplo, para a matriz

```text
A = | a  b |
	| c  d |
```

temos `C₁₁ = d`, `C₁₂ = -c`, `C₂₁ = -b` e `C₂₂ = a`.

Os co-fatores permitem calcular o determinante pela expansão de Laplace. Expandindo pela linha `i`:

`det(A) = aᵢ₁Cᵢ₁ + aᵢ₂Cᵢ₂ + ... + aᵢₙCᵢₙ`.

Também é possível expandir por qualquer coluna `j`:

`det(A) = a₁ⱼC₁ⱼ + a₂ⱼC₂ⱼ + ... + aₙⱼCₙⱼ`.
