# QA, Segurança e Ética

Nome: Tarsis Mikael Ventura Dumas de Lima

## Prompt Injection (direta e indireta)

### Direta

Prompt Injection Direta em LLMs acontece quando o cliente insere informações maliciosas no próprio prompt. O atacante manipula o comportamento do modelo, desvia instruções originais e/ou extrai dados sensíveis de um LLM. Esse risco é considerado um dos maiores desafios de segurança em aplicações baseadas em LLMs e sistemas agênticos.

### Indireta

Prompt Injection Indireta em LLMs ocorre quando o atacante não interage diretamente com o modelo, mas insere instruções maliciosas em fontes de dados externas que o LLM consome (como páginas web, documentos PDF, e-mails ou bases de conhecimento via RAG). Quando o agente processa essa fonte externa para responder a uma consulta legítima, ele acaba executando as instruções ocultas, o que pode levar à exfiltração de dados do usuário ou à execução de ações não autorizadas em nome do sistema.

## Data Leakage (vazamento de dados sensíveis através das respostas da IA)

Data Leakage acontece quando o agente de Inteligencia Artificial revela dados confidenciais presentes no treinamento, no contexto de execução ou em integrações com sistemas. As principais causas podem ser o uso de datasets sem anonimização, a falta de controle sobre o o que o agente de Inteligencia Artificial pode memorizar e reproduzir e/ou integrações inseguras com bases de dados ou APIs. Para corrigir, é necessário implementar técnicas de sanitização de dados (PII masking), utilizar camadas de filtragem de saída que detectam padrões de dados sensíveis (como CPFs ou chaves de API) e garantir que o contexto fornecido ao modelo via RAG contenha apenas as informações estritamente necessárias para a tarefa, aplicando permissões de acesso baseadas em funções (RBAC).

## Insecure Output Handling (quando a saída da IA executa comandos maliciosos no sistema).

Insecure Output Handling acontece quando se usa indevidamente a saída de um agente de Inteligencia Artificial (IA) tratando a mesma como confiável, sem verificações. O impacto pode ser crítico, permitindo que a IA execute comandos maliciosos no sistema, como injeções de SQL, Cross-Site Scripting (XSS) ou execução remota de código (RCE), caso a saída seja passada diretamente para interpretadores de código, navegadores ou APIs. Para mitigar esse risco, é fundamental tratar toda saída gerada pela IA como conteúdo não confiável, aplicando sanitização rigorosa, utilizando sandboxes para execução de scripts e implementando validações de esquema (schema validation) antes que qualquer ação automatizada seja disparada pelas ferramentas (tools) do agente. Para corrigir, deve-se adotar o princípio do privilégio mínimo para as APIs consumidas, utilizar bibliotecas de parsing seguro para processar formatos como JSON ou Markdown e garantir que ações críticas passem por uma camada de aprovação humana (Human-in-the-loop) antes da execução final.

## Grounding

Grounding acontece quando modelo de IA ancora suas respostas em bases de conhecimento específicas, verídicas e atualizadas, em vez de depender apenas do conhecimento genérico adquirido durante seu treinamento. Essa técnica é fundamental para reduzir alucinações, garantindo que a IA admita quando não possui uma informação ou responda estritamente com base nos documentos fornecidos. A implementação mais comum é a arquitetura RAG (Retrieval-Augmented Generation), que recupera fragmentos de dados relevantes de um banco de vetores e os injeta no contexto do prompt, forçando o modelo a sintetizar a resposta a partir dessas evidências.

## RAG (Geração Aumentada de Recuperação)

RAG é uma arquitetura que combina a capacidade de geração de texto de um LLM com um sistema de recuperação de informações em tempo real. Em vez de confiar apenas nos pesos estáticos do modelo, o RAG consulta uma base de dados externa (geralmente um banco de vetores) para buscar documentos relevantes à pergunta do usuário. Esses dados são inseridos no contexto do prompt, permitindo que a IA gere respostas mais precisas, citando fontes e minimizando alucinações ao utilizar informações que não faziam parte do seu treinamento original.


