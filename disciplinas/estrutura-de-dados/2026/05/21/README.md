# Estrutura de Dados - 2026/05/21

## Grafos

Um grafo é uma estrutura de dados usada para representar relações entre elementos.

### Componentes

#### Vértices (ou nós): representam os elementos.

Vértices (ou nós) são as entidades fundamentais de um grafo. Cada vértice representa um item, ponto ou objeto no domínio modelado (por exemplo, uma pessoa em uma rede social, uma cidade em um mapa ou uma tarefa em um grafo de dependências). Vértices podem armazenar informações ou rótulos (identificadores, atributos) e servem como pontos de conexão para as arestas. Em implementações, vértices costumam ser representados por índices, chaves ou estruturas que guardam seus dados e uma lista de adjacência para suas conexões.

#### Arestas: representam as conexões entre os vértices.

Arestas conectam pares de vértices e representam a relação entre eles. Em um grafo não direcionado, uma aresta {u, v} indica conexão mútua entre u e v; em um grafo direcionado, uma aresta (u -> v) indica uma relação de u para v. Arestas podem ser:

- simples: conectam dois vértices distintos;
- laço (self-loop): conectam um vértice a ele mesmo;
- múltiplas (multigrafo): podem existir várias arestas entre os mesmos dois vértices.

Além disso, arestas podem carregar informações adicionais como peso (custo, distância), rótulos ou capacidades, úteis em algoritmos de menor caminho, fluxo e otimização. Em implementações, arestas são representadas explicitamente em listas de adjacência ou implicitamente na matriz de adjacência (valores booleanos ou numéricos indicando presença/peso).

#### Grafo direcionado: a conexão tem direção.

Em um grafo direcionado, as arestas têm um sentido definido. Isso significa que a relação vai de um vértice de origem para um vértice de destino, e nem sempre a conexão pode ser percorrida no sentido inverso. Por exemplo, se existe uma aresta de A para B, isso não implica necessariamente que exista uma aresta de B para A. Esse tipo de grafo é usado em situações como dependências entre tarefas, links da web, rotas com sentido único e fluxos de informação.

#### Grafo não direcionado: a conexão não tem direção.

Em um grafo não direcionado, as arestas não possuem sentido. Assim, se existe uma conexão entre dois vértices, ela vale nos dois sentidos. Se A está ligado a B, então B também está ligado a A. Esse tipo de grafo é comum em relações simétricas, como amizade em redes sociais, conexões entre cidades em vias de mão dupla e redes em que a relação entre os elementos é recíproca.

#### Grafo ponderado: as arestas possuem peso, custo ou distância.

Em um grafo ponderado, cada aresta recebe um valor numérico chamado peso. Esse peso pode representar distância, custo, tempo, capacidade, prioridade ou qualquer outro critério relevante para o problema. Por exemplo, em um mapa, o peso de uma aresta pode ser a distância entre duas cidades; em uma rede de computadores, pode ser o tempo de transmissão. Grafos ponderados são muito usados em algoritmos de menor caminho, otimização e análise de redes.

### Representações comuns

- Lista de adjacência: cada vértice guarda seus vizinhos.
- Matriz de adjacência: uma matriz indica se existe aresta entre dois vértices.

### Conceitos importantes

- Grau: quantidade de arestas ligadas a um vértice.
- Caminho: sequência de vértices conectados por arestas.
- Ciclo: caminho que começa e termina no mesmo vértice.
- Conectividade: indica se existe caminho entre vértices do grafo.

### Aplicações

- redes sociais
- rotas de transporte
- mapas e navegação
- dependências entre tarefas ou módulos

### Observações

Grafos são úteis para modelar problemas reais em que existe relação entre objetos, permitindo análises como busca, menor caminho e ordenação de dependências.

## Prática - Exemplos

A seguir, exemplos de problemas reais que podem ser modelados e resolvidos com grafos:

- Menor caminho (Shortest Path): rotas em mapas, GPS, menor custo entre cidades (algoritmos: Dijkstra, Bellman-Ford, A*).
- Árvore geradora mínima (Minimum Spanning Tree): planejamento de redes de energia, cabeamento com custo mínimo (Kruskal, Prim).
- Fluxo máximo / Corte mínimo: roteamento de tráfego, capacidade de redes, problemas de emparelhamento com capacidade (Ford–Fulkerson, Edmonds–Karp).
- Emparelhamento em grafos: alocação de tarefas, casamento estável simplificado, pareamento bipartido (Hungarian, Hopcroft–Karp).
- Ordenação topológica / dependências: escalonamento de tarefas, compilação de projetos com dependências (DAGs).
- Detecção de ciclos: detecção de dependências circulares, verificação de integridade de pipelines.
- Conectividade e componentes: identificar clusters em redes sociais, regiões conectadas em mapas.
- Busca e exploração (BFS/DFS): alcance em redes, verificação de caminhos, resolução de labirintos.
- Redes sociais e recomendações: modelagem de amizades, influência, recomendações por proximidade.
- Roteamento em redes de comunicação: encaminhamento de pacotes, balanceamento de carga.
- Planejamento e logística: roteirização de veículos (problema do caixeiro viajante como variante), otimização de rotas.
- Análise de fluxo de trabalho e pipelines: detectar gargalos e otimizar processos.
- Web crawling e análise de links: PageRank, descoberta de comunidades e indexação de páginas.
- Modelagem de circuitos e dependências elétricas: análise de conexões e falhas.
- Imagens e visão computacional: segmentação por construção de grafos de pixels e corte mínimo.

Para cada problema, a escolha da representação (lista de adjacência, matriz de adjacência) e do algoritmo influencia diretamente em eficiência e aplicabilidade.

## Aula 9

https://github.com/orlandosaraivajr/FATEC_1SEM26_ED/tree/main/aula9

### Atividade

[Exercícios Grafos](./Exercicios-Grafos.pdf)
