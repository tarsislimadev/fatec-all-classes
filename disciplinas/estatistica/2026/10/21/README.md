# Encontro 2026/10/21 - Estatística

## Revisão - Analise Combinatória

### Princípio Fundamental da Contagem

Quantos combos podem ser formados em uma lanchonete que oferece: 4 tipos de sanduíche, 3 tipos de bebidas e 2 tipos de sobremesa?

Resposta: 4 x 3 x 2 = 24 combinações.

```mermaid
flowchart TD
    A[Sanduíche] --> A1[1]
    A --> A2[2]
    A --> A3[3]
    A --> A4[4]

    A1 --> B1[Bebida 1]
    A1 --> B2[Bebida 2]
    A1 --> B3[Bebida 3]

    A2 --> B1
    A2 --> B2
    A2 --> B3

    A3 --> B1
    A3 --> B2
    A3 --> B3

    A4 --> B1
    A4 --> B2
    A4 --> B3

    B1 --> C1[Sobremesa 1]
    B1 --> C2[Sobremesa 2]
    B2 --> C1
    B2 --> C2
    B3 --> C1
    B3 --> C2

    D[Total: 4 x 3 x 2 = 24 combos]
```

### Fatorial

O fatorial de um número natural n é o produto de todos os inteiros positivos até n.

- 0! = 1
- 1! = 1
- 2! = 2 x 1 = 2
- 3! = 3 x 2 x 1 = 6
- 4! = 4 x 3 x 2 x 1 = 24
- 5! = 5 x 4 x 3 x 2 x 1 = 120

```mermaid
graph LR
    F0[0!] --> R0[1]
    F1[1!] --> R1[1]
    F2[2!] --> R2[2]
    F3[3!] --> R3[6]
    F4[4!] --> R4[24]
    F5[5!] --> R5[120]
```

### Combinação (ordem não importa)

A combinação representa o número de grupos que podemos formar escolhendo k elementos de um conjunto de n elementos, sem considerar a ordem.

Fórmula:

C(n, k) = n! / (k! (n - k)!)

Exemplo:

Escolher 2 sabores de pizza entre 5 disponíveis:

C(5, 2) = 5! / (2! 3!) = 10

```mermaid
graph TD
    A[Conjunto: 5 sabores]
    A --> B[Escolha 2 sem ordem]
    B --> C[AB, AC, AD, AE, BC, BD, BE, CD, CE, DE]
    C --> D[Total = 10 combinações]
```

### Arranjo (ordem importa)

O arranjo representa o número de sequências que podemos formar ao escolher k elementos de um conjunto de n elementos, considerando a ordem da escolha.

Fórmula:

A(n, k) = n! / (n - k)!

Exemplo:

Quantas senhas com 3 dígitos distintos podem ser formadas usando os algarismos 1, 2, 3, 4?

A(4, 3) = 4! / (4 - 3)! = 4 x 3 x 2 = 24

Ou seja, a ordem dos dígitos altera a senha, então 123 e 321 são arranjos diferentes.

### Resumo

- Princípio Fundamental da Contagem: multiplica as opções
- Fatorial: produto dos números até n
- Combinação: escolhe grupos sem considerar ordem
- Arranjo: escolhe sequências considerando a ordem
