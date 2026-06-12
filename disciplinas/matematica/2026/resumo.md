# Resumo de Matemática 2026

## 1. Conjuntos e conjuntos numéricos

- Conjunto: coleção de elementos definidos por uma propriedade.
- Operações fundamentais:
  - União: $A \cup B$ contém todos os elementos que estão em $A$ ou em $B$.
  - Interseção: $A \cap B$ contém apenas os elementos que estão em ambos.
  - Diferença: $A - B$ contém elementos de $A$ que não estão em $B$.
- Conjuntos numéricos:
  - Naturais ($\mathbb{N}$)
  - Inteiros ($\mathbb{Z}$)
  - Racionais ($\mathbb{Q}$)
  - Irracionais
  - Reais ($\mathbb{R}$)
- Exemplos de aplicações incluem a classificação de valores e o uso de conjuntos em problemas de lógica e probabilidade.

## 2. Equações de primeiro grau

- Forma geral: $ax + b = 0$, com $a \neq 0$.
- Solução:
  - Isolar a variável: $ax = -b$
  - Dividir por $a$: $x = -\frac{b}{a}$
- Exemplo:
  - $2x + 4 = 0$ -> $x = -2$.

## 3. Equações de segundo grau

- Forma geral: $ax^{2} + bx + c = 0$, com $a \neq 0$.
- Discriminante:
  - $\Delta = b^{2} - 4ac$
- Fórmula de Bhaskara:
  - $x = \frac{-b \pm \sqrt{\Delta}}{2a}$
- Exemplo:
  - $x^{2} - 5x + 6 = 0$
  - $\Delta = 1$
  - $x_{1} = 3$, $x_{2} = 2$.

## 4. Inequações

- Definição: desigualdade matemática que usa $>$, $<$, $\geq$ ou $\leq$.
- Diferença principal em relação à equação:
  - Equação: solução isolada ou finita.
  - Inequação: intervalo ou conjunto de valores.
- Regras de resolução:
  1. Isolar a variável.
  2. Somar/subtrair ou multiplicar/dividir ambos os lados.
  3. Inverter o sinal se multiplicar ou dividir por número negativo.
- Exemplo:
  - $2x + 3 > 7$ -> $x > 2$.
  - $-4x + 8 > 0$ -> $x < 2$.
- Representação na reta numérica:
  - Círculo aberto para valores não incluídos ($>$ ou $<$).
  - Círculo fechado para valores incluídos ($\geq$ ou $\leq$).

## 5. Funções

- Definição: relação em que cada elemento do domínio associa-se a um único elemento do contradomínio.
- Notação:
  - $f: A \to B$
  - $f(x)$ é o valor da função em $x$.
- Termos principais:
  - Domínio: conjunto de entradas válidas.
  - Contradomínio: conjunto de possíveis saídas declaradas.
  - Imagem: conjunto real de valores assumidos pela função.
- Exemplo de função:
  - $f(x) = x + 2$ tem domínio dos reais e imagem também nos reais.
  - $f(x) = x^{2}$ com domínio real tem imagem $[0, +\infty)$.
- Teste da reta vertical: se uma reta vertical cruza mais de um ponto do gráfico, a relação não é função.

## 6. Função afim e parábola

- Função afim:
  - Forma: $f(x) = ax + b$.
  - Gráfico: linha reta.
  - Usada como base para regressão linear e ajuste de dados.
- Função quadrática:
  - Forma: $f(x) = ax^{2} + bx + c$, $a \neq 0$.
  - Gráfico: parábola.
  - Elementos importantes: raízes, vértice e discriminante.

## 7. Equações exponenciais

- Definição: incógnita aparece no expoente.
- Forma geral: $b^{x} = a$, com base $b$ positiva e $b \neq 1$.
- Solução em termos de logaritmos:
  - $x = \log_{b}(a)$.
- Esse tipo de equação aparece em crescimento e decrescimento exponencial, juros compostos e modelagem de fenômenos que evoluem por potências.

## 8. Logaritmos

- Definição: o logaritmo de $a$ na base $b$ é o expoente necessário para que $b$ elevado a esse expoente resulte em $a$.
  - Se $b^{x} = a$, então $\log_{b}(a) = x$.
- Condições:
  - $b > 0$, $b \neq 1$
  - $a > 0$
- Casos comuns:
  - Logaritmo decimal: $\log(a)$, base 10.
  - Logaritmo natural: $\ln(a)$, base $e \approx 2{,}718$.
  - Logaritmo binário: base 2.
- Consequências:
  - $\log_{b}(1) = 0$.
  - $\log_{b}(b) = 1$.
  - A função logarítmica é inversa da exponencial de mesma base.
  - Para base $b>1$, $\log_{b}(a)$ é crescente.
  - Para $0<b<1$, $\log_{b}(a)$ é decrescente.

## 9. Propriedades operatórias dos logaritmos

- Produto:
  - $\log_{b}(ac) = \log_{b}(a) + \log_{b}(c)$.
- Quociente:
  - $\log_{b}\left(\frac{a}{c}\right) = \log_{b}(a) - \log_{b}(c)$.
- Potência:
  - $\log_{b}(a^{n}) = n \cdot \log_{b}(a)$.
- Raiz:
  - $\log_{b}(\sqrt[n]{a}) = \frac{1}{n} \log_{b}(a)$.
- Mudança de base:
  - $\log_{b}(a) = \frac{\log_{k}(a)}{\log_{k}(b)}$, com $k>0$ e $k\neq 1$.

## 10. Notas extras

- O material de 2026/04/24 também contém referência a exercícios sobre conjuntos e conjuntos numéricos.
- O arquivo `disciplinas/matematica/2026/04/10/Equação Exponencial.pdf` aborda especificamente equações exponenciais.
- A aula de 2026/04/10 relaciona função afim com regressão linear e método dos mínimos quadrados.
