# Introdução a Inteligencia Artificial - 2026/05/25

## Protocolo HTTP

HTTP (HyperText Transfer Protocol) é o protocolo de aplicação usado para comunicação entre clientes (por exemplo, navegadores) e servidores web. Ele define como as mensagens são formatadas e transmitidas, e quais ações os servidores e clientes devem tomar em resposta a várias requisições.

Principais conceitos:
- Métodos (verbs): GET, POST, PUT, DELETE, PATCH, HEAD, OPTIONS — indicam a ação desejada sobre o recurso.
- URLs/URIs: identificadores de recursos na web.
- Cabeçalhos (headers): metadados da requisição/resposta (Content-Type, Authorization, Accept, Cache-Control, etc.).
- Corpo (body): dados enviados em requisições ou respostas (ex.: JSON, form data, arquivos).
- Códigos de status: 1xx informativo, 2xx sucesso (200 OK, 201 Created), 3xx redirecionamento, 4xx erro do cliente (400 Bad Request, 401 Unauthorized, 404 Not Found), 5xx erro do servidor (500 Internal Server Error).

Modos de uso:
- Stateless: cada requisição é independente; servidor não necessariamente mantém estado entre requisições.
- Sessões e autenticação: mecanismos como cookies, tokens JWT ou OAuth são usados para manter estado/identidade entre requisições.

HTTP/1.1 vs HTTP/2 vs HTTP/3:
- HTTP/1.1: conexões persistentes, texto claro, cabeçalhos repetitivos.
- HTTP/2: multiplexação de streams, compressão de headers, binary framing — melhora performance.
- HTTP/3: baseado em QUIC (UDP), menor latência e melhor recuperação de perda de pacotes.

Segurança:
- HTTPS é HTTP sobre TLS/SSL — criptografa tráfego para proteger confidencialidade e integridade.

Boas práticas para APIs web:
- Usar métodos HTTP de forma semântica.
- Retornar códigos de status apropriados.
- Versionar a API (ex.: /v1/).
- Validar e sanitizar entrada do usuário.
- Usar HTTPS em produção.

Exemplo simples de requisição HTTP/1.1:

GET /api/items HTTP/1.1
Host: example.com
Accept: application/json

Resposta:

HTTP/1.1 200 OK
Content-Type: application/json

[ { "id": 1, "name": "Item A" } ]

Recursos para estudo:
- RFC 7230–7235 (HTTP/1.1)
- RFC 7540 (HTTP/2)
- Documentação sobre HTTPS e TLS

## Protocolo SSH

SSH (Secure Shell) é um protocolo de rede usado para acesso remoto seguro a máquinas e serviços. Ele cria um canal criptografado entre cliente e servidor, permitindo executar comandos, transferir arquivos e administrar sistemas sem expor credenciais ou dados em texto claro.

Principais usos:
- Acesso remoto ao terminal de servidores.
- Execução de comandos administrativos à distância.
- Transferência segura de arquivos com SCP e SFTP.
- Encaminhamento de portas e túneis criptografados.

Conceitos importantes:
- Autenticação por senha ou por chave pública/privada.
- Porta padrão 22/TCP.
- Criptografia para confidencialidade, integridade e autenticação.

Boas práticas:
- Preferir autenticação por chave em vez de senha.
- Desabilitar acesso direto de root quando possível.
- Alterar configurações padrão e restringir usuários autorizados.
- Manter o serviço atualizado e monitorar tentativas de acesso.

Exemplo de uso:

```bash
ssh usuario@servidor.com
```

Esse comando abre uma sessão remota segura no servidor informado.
