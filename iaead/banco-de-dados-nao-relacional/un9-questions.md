# Banco de Dados Não Relacional

## Unidade 9 - Reavaliação

Pergunta: Na migração de sistemas relacionais para NoSQL, alguns desafios surgem em função da flexibilidade do MongoDB. Qual é um risco comum em processos de migração para o MongoDB?

Resposta: Criação de documentos com esquemas divergentes e campos obsoletos.

Pergunta: O desempenho de consultas em grandes volumes de dados depende de técnicas de otimização. Qual é a principal função dos índices em MongoDB?

Resposta: Melhorar a performance das consultas, reduzindo o tempo de busca.

Pergunta: A modelagem de dados é um dos pontos centrais no uso do MongoDB, já que sua flexibilidade exige decisões conscientes para garantir desempenho e consistência. Qual é a principal característica da modelagem de documentos em MongoDB?

Resposta: Estruturação em coleções compostas por documentos BSON flexíveis, que permitem diferentes formatos de dados

Pergunta: Ao manipular arrays em documentos MongoDB, muitas vezes, é necessário atualizar apenas elementos específicos. Qual recurso do MongoDB possibilita a atualização seletiva de elementos dentro de um array?

Resposta: arrayFilters

Pergunta: Em projetos reais, a ausência de estratégias de backup pode causar prejuízos irreparáveis. Qual ferramenta oficial do MongoDB é utilizada para backup de dados?

Resposta: mongodump

Pergunta: As operações de inclusão de documentos representam o ponto inicial na manipulação de dados em MongoDB. Qual comando é utilizado para inserir um único documento em uma coleção?

Resposta: insertOne()

Pergunta: A segurança é um dos pilares de qualquer Banco de Dados, incluindo o MongoDB. Qual prática contribui diretamente para a segurança no MongoDB?

Resposta: Criação de usuários com roles específicas e autenticação habilitada.

Pergunta: A exclusão de documentos é uma ação crítica, que pode ser feita de forma definitiva ou preservando dados para auditoria. Qual é a diferença entre exclusão física e exclusão lógica em MongoDB?

Resposta: A exclusão física remove o documento permanentemente, enquanto a exclusão lógica apenas o marca como inativo.

Pergunta: O modelo BASE é frequentemente utilizado em sistemas distribuídos como os Bancos NoSQL, oferecendo maior disponibilidade, em detrimento da consistência imediata. Sobre o modelo BASE adotado por muitos Bancos NoSQL, assinale a alternativa correta:

Resposta: O modelo BASE oferece consistência eventual, permitindo que os dados fiquem temporariamente inconsistentes em troca de disponibilidade e tolerância a falhas.

Pergunta: Ao tratar de dados organizados, o termo “estruturado” é frequentemente empregado para descrever formatos que seguem modelos formais e rígidos. Sobre dados estruturados, é correto afirmar que:

Resposta: São organizados segundo um esquema fixo e armazenados em Bancos Relacionais com suporte a SQL.
