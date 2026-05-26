# Banco de Dados Não Relacional

## Unidade 7 - Perguntas Avaliativas

Pergunta: Um analista de dados precisa remover todos os registros de usuários inativos para reduzir o volume de dados armazenados. Qual comando realiza essa operação com eficiência e segurança?

Resposta: db.usuarios.deleteMany({ ativo: false })

Pergunta: Uma empresa deseja remover todos os clientes que estão inativos e não têm compras registradas. Qual comando implementa corretamente esse critério composto?

Resposta: db.clientes.deleteMany({ inativo: true, compras: 0 })

Pergunta: Uma empresa deseja manter o histórico de dados, mesmo ao "remover" documentos. Qual estratégia a seguir atende esse requisito?

Resposta: Atualizar o campo status para "inativo"

Pergunta: Um desenvolvedor deseja limpar completamente uma coleção de testes chamada temp. Qual comando remove todos os documentos da coleção?

Resposta: db.temp.deleteMany({})
