# EXECUÇÃO DE PROJETOS 2 - 2026/06/03

Projeto: https://github.com/tarsislimadev/fatec-yeb-db

## 1. O que os alunos terão que Pesquisar?

Os squads precisarão investigar as principais vulnerabilidades e mitigações no ciclo de vida de aplicações baseadas em Modelos de Linguagem (LLMs) e Sistemas Agênticos. A pesquisa deve focar em três pilares, cada um voltado para o tema (software) da squad:

Pesquisar sobre riscos críticos como Prompt Injection (direta e indireta), Data Leakage (vazamento de dados sensíveis através das respostas da IA) e Insecure Output Handling (quando a saída da IA executa comandos maliciosos no sistema).

Investigar técnicas para garantir que as respostas da IA sejam baseadas estritamente em dados reais do negócio (Grounding), utilizando arquiteturas de RAG (Geração Aumentada de Recuperação) para mitigar respostas inventadas.

Pesquisar como identificar vieses algorítmicos nos dados de treino ou nas instruções do sistema que possam gerar discriminação, além de entender a importância da transparência na tomada de decisão da IA.

## 2. O que os alunos terão que Desenvolver? (Artefatos Práticos)

Os alunos deverão implementar defesas técnicas e testes automatizados diretamente na arquitetura de suas aplicações.A. Em termos de QA (Garantia de Qualidade):

Os alunos devem criar um roteiro ou script de testes tentando "quebrar" deliberadamente o próprio agente (ex: induzir a IA a ignorar suas restrições de sistema, extrair dados confidenciais ou dar descontos indevidos).

Implementar asserções binárias (Passa / Não Passa) para validar se o formato, o tom e o conteúdo da saída da IA atendem rigorosamente aos critérios de aceite definidos no PRD.

B. Em termos de Segurança e IA Agêntica:

Desenvolver filtros ou prompts de validação intermediários (como um "Agente Validador") que analisam a entrada do usuário e a saída do agente antes de exibi-la na interface, bloqueando conteúdos nocivos ou fora do escopo do negócio.

Garantir que as ferramentas (tools) que o agente aciona (APIs, bancos de dados, scripts de execução) possuam permissões estritas e sanitização de inputs, impedindo que a IA execute ações destrutivas ou não autorizadas.

C. Em termos de Ética e Governança:

Desenvolver um fluxo de aprovação humana na interface para ações críticas ou de alto impacto financeiro/operacional sugeridas pela IA, garantindo que a decisão final permaneça sob controle humano.

Implementar um sistema de log que registre o fluxo de pensamento (Chain of Thought) do agente, documentando quais ferramentas foram chamadas e quais dados foram consultados para justificar a resposta gerada.

## Resumo da Entrega para a Squad

Ao final dessa semana, cada squad deve atualizar seu PRD com uma seção dedicada a demonstrar em execução como o sistema lida de forma segura com entradas maliciosas ou fora de escopo (use formas de comprovação como vídeo ou sequências de prints).
