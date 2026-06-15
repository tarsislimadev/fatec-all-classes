# Banco de Dados Não Relacional

## Unidade 9 - Reavaliação

Pergunta: Segundo Nadeau et al (2013) podemos atribuir significados diferentes para dado, informação e conhecimento. Leia as afirmativas a seguir e escolha a opção correta sobre elas: I. Dado: é o componente básico de um arquivo, é um elemento com um significado no mundo real, que compõe um sistema de arquivos. II. Conhecimento: após a interpretação dos dados, é possível associar um significado aos dados ou processá-los. III. Informação: todo entendimento, obtido por meio de critérios, avaliação dos dados e conhecimento.

Resposta: Apenas a afirmativa I está correta.

Pergunta: Leia com atenção as afirmativas a seguir: - É a descrição do banco de dados. - Representa a estrutura do banco de dados. - Tem uma natureza mais estática, pois não muda com frequência. Selecione a alternativa que apresenta o conceito que está relacionado às afirmativas descritas acima:

Resposta: Esquema

Pergunta: Entidade é um dos conceitos mais importantes da Modelagem Conceitual quando nos referimos a banco de dados relacionais, por isso é fundamental entender a sua dimensão. Leia as afirmativas a seguir sobre entidade: I - Entidade tem relacionamentos - propriedades particulares que a descrevem. II - Entidades são os principais objetos de dados, nos quais informações devem ser coletadas, elas normalmente representam uma pessoa, lugar, coisa ou evento de interesse informativo. III - Uma entidade pode ser um objeto com uma existência física, por exemplo, um aparelho eletrônico ou um objeto com uma existência conceitual um departamento de uma empresa Selecione a opção que apresenta as afirmações corretas sobre as afirmativas apresentadas.

Resposta: A afirmativa I está errada porque o que descreve uma entidade são seus atributos. As afirmativas II e III estão corretas.

Pergunta: O(s) atributo(s) chave(s) tem(têm) a função de atuar(em) como identificador(es) único(s) das instâncias de uma entidade. Dentro da abordagem relacional de banco de dados, denomina-se esta propriedade como Chave Primária de uma tabela, além disso, esses atributos não podem conter valores nulos, devem ser de preenchimento obrigatório. Sabendo dessa afirmação, pense em um sistema de controle comercial no qual existem as entidades NOTA_FISCAL, ITEM_NOTA e PRODUTO, conforme a descrição textual a seguir: NOTA FISCAL (num_nota, data_nota, cod_cliente, total_nota) ITEM_NOTA (num_nota, cod_produto, quantidade) PRODUTO (cod_produto, descricao_produto, preco_produto, marca, tamanho) Observando as três entidades vemos que a entidade ITEM_NOTA não tem nenhum atributo sublinhado, o que demonstra que não está com o(s) atributos-chave indicados. A partir do cenário acima, qual seria ou seriam o(s) atributo(s) correto(s) para serem o(s) identificador(es) da entidade ITEM_NOTA? Selecione a opção que apresenta a resposta certa. 

Resposta: num_nota, cod_produto

Pergunta: Se precisarmos modelar um banco de dados para organizar todos os tipos de usuários de uma universidade observaremos que todos terão dados em comum como: nome, data de nascimento, RG, CPF, telefone, endereço e e-mail, porém algumas informações são específicas dependendo do tipo de papel que representam na universidade. Por exemplo: do tipo de usuário PROFESSOR é necessário saber a sua titulação (graduação, especialização, mestrado, doutorado), tempo de atuação docente, currículo lattes entre outras. Do usuário aluno, é necessário saber o histórico escolar do ensino médio, por qual meio ingressou na universidade, informações socioeconômicas, entre outras. Sabendo dessas informações, pode-se afirmar que no banco de dados da universidade existirá um tipo de entidade que além dos dados do USUÁRIO armazenará as informações específicas de PROFESSORES e ALUNOS. Dentro da classificação das entidades, qual das opções apresenta o tipo mais adequado de entidade para atender as exigências do cenário descrito?

Resposta: Entidade Subordinada

Pergunta: Sobre chaves em um banco de dados, podemos afirmar que existem vários tipos, cada qual com a sua função e importância dentro da modelagem conceitual. Relacione os conceitos de chaves ao seu respectivo significado. (a) Chave primária        (b) Chave estrangeira    (c) Chave candidata . (  ) tem potencial para identificar unicamente um registro, mas por alguma característica específica não foi o atributo escolhido para essa finalidade. (  ) um atributo ou conjunto de atributos que distingue unicamente uma ocorrência da entidade. (  ) é o atributo que tem a função de relacionar as duas entidades, por isso não pode conter um valor nulo. (  ) define uma restrição de integridade do banco de dados que é uma regra que implica na unicidade de valores na(s) coluna(s) que compõe(m) essa chave. Selecione a alternativa que apresenta a relação correta entre o conceito de chave, seu significado e exemplo dentro do contexto de banco de dados.

Resposta: c-a-b-a

Pergunta:  Sobre formas normais sabemos que existem regras que identificam cada uma dessas etapas, relacione a regra principal a sua forma normal, conforme as colunas a seguir: (a) 1FN        (  ) Ausência de dependências funcionais transitivas. (b) 2 FN       (  ) Ausência de dependências entre os atributos não-chave. (c) 3 FN       (  ) Ausência de dependências de junção. (d) FNBC     (  ) Atributos atômicos e indivisíveis. (e) 4 FN       (  ) Ausência de dependências multivaloradas. (f) 5 FN        (  ) Ausência de dependências funcionais parciais. Selecione a opção que apresenta a sequência correta entre a forma normal e a sua regra principal.

Resposta: c-d-f-a-e-b

Pergunta: Leia com atenção as afirmativas sobre Mapeamento de Relacionamentos de um modelo lógico relacional e analise se as afirmativas são verdadeiras (V) ou falsas (F): a. (  ) As alternativas possíveis de mapeamento de relacionamentos são divididas em dois grandes grupos: Navegação incorporada e Navegação disjunta. b. (  ) A navegação incorporada trabalha diretamente com o conceito de chave primária. c. (  ) A navegação disjunta é considerada mais simples e mais comumente utilizada na atualidade. d. (  ) A navegação disjunta trabalha sem a modificação das definições dos registros já existentes, criando novas entidades, diferentes das existentes, que têm a finalidade de propiciar a navegação, ou seja, quando ocorrerem relacionamentos do tipo N:N. Assinale a alternativa certa sobre a sequência correta de valores verdadeiros (V) e falsos (F) sobre as afirmativas apresentadas.

Resposta: V-V-F-V

Pergunta: Analise o código MySQL a seguir:  create table cliente( id int unsigned not null auto_increment primary key, nome varchar(80) not null, fone varchar(30) not null, endereco varchar(120) not null);  Para inserir um novo registro a esse banco de dados qual comando deve ser utilizado?  Selecione a opção que apresenta o comando para inserir um novo registro a tabela “cliente”.

Resposta: insert into cliente (nome,fone,endereço) values ('Rosa Pereira','16-3371-0987','Rua Visconde Sabugosa, 500');

Pergunta: Analise o código MySQL a seguir:  create table animal ( cod_animal integer not null primary key, nome_animal varchar (30), dataNasc date, sexo char (01), cod_prop integer not null, foreign key (cod_prop) references proprietario(cod_propr));  Leia as afirmativas a seguir, avaliando se são Verdadeiras (V) ou Falsas (F).  a. (  ) O campo cod_animal é uma chave primária e o campo cod_prop é uma chave estrangeira, por isso ambos estão com a informação “not null”, pois esse tipo de campo não pode ter valores nulos. b.(  ) O campo sexo é do tipo char(01), porque provavelmente deve ser inserido apenas o caracter “F” para fêmea e “M” para macho, identificando o sexo do animal. Esse tipo de dado é usado para informações do tipo texto que tem um tamanho fixo. c. (  ) “cod_prop” é um campo de outra tabela que está na tabela animal fazendo o relacionamento entre as tabelas, isso ocorre porque existe um relacionamento do tipo N:N entre elas.  Assinale a alternativa certa sobre a sequência correta de valores verdadeiros (V) e falsos (F) sobre as afirmativas apresentadas. 

Resposta: F-V-F
