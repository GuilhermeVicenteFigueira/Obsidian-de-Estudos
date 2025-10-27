HTTP é a sigla de Hypertext Transfer Protocol(Protocolo de Transferencia HiperTexto). é um protocolo usado para enviar  e receber dados pela Web.

O HTTP é Baseado em uma arquitetura cliente servidor , na qual  o cliente envia solicitações  ao servidor para recuperar ou enviar informações.

Quando um cliente faz uma requisição, o servidor responde com o código de status e os dados solicitados.


![[Pasted image 20250518175722.png]]

---

# Headers

O cabeçalho de uma solicitação HTTP para uma Api contém informações adicionais sobre solicitações 
ou a resposta. Ele inclui metadados, como tipo de conteúdo, Token de autorização, cookies, preferências 
de idioma e muito mais. Esse cabeçalhos fornecem detalhes crucias para que o servidor 
processe a solicitação e para que o cliente interprete a resposta.


---
# Corpo da mensagem

O body da solicitação em uma APi contém dados enviados pelo cliente ao servidor . Ele é usado para transferir 
informações importantes, exemplo: Nome, Email, CPF e endereço etc.. para a sua Api da WEB.

---
# Métodos HTTP

Os métodos HTTP, como PUT, GET, POST e DELETE, definem as ações que podem ser executadas em uma API.


| Métodos | funções                                                                                          |
| ------- | ------------------------------------------------------------------------------------------------ |
| Get     | O Get  é usado para solicitar dados de um servidor,<br>Por meio de um URl, é o mais comun na web |
| Put     | O PUT é utilizado pra atualizar dados no server                                                  |
| Post    | O POST  é utilizado para enviar dados para o server.<br>Comunmente usado para criar recusos      |
| Delete  | O DELETE é usado para remover recurso do server,<br>Ao Enviar um DELETE, o recurso é exluido     |

# GET

### Solicita dado:
O métodos GET é usado para solicitar dados de um server . Ao enviar uma solicitação Get, você  está pedindo ao server para retornar infos.

### Parâmetros URL
Os parâmetros podem adicionados à URl para filtrar os resultados ou especificar infos adicionais.

### Respotas de sucesso

Uma resposta de sucesso irá retornar os dados solicitados no corpo da resposta com um código de status 200


---

# PUT 

## enviar dados 
Os métodos put é usado para enviar dados  para o servidor. É Comumente usado para atualizar um recuso existente

## Código status 200 ou 204
Uma resposta de sucesso retornará um código de status 200 indicando que o recurso foi atualizado com sucesso.

## payload Completo
é necessário enviar um playload completo com todas as informações atualizadas para garantir a consistência dos dados.


---
# Post
É a mesma coisa de que PUT porem você cria e o retorno é 201

---
# DELETE

## Excluir recursos
O método DELETE é usado para excluir recursos do servidor. Ao Enviar uma solicitação DELETE, o recurso correspondente será removido

## Codigo de status 204
Uma resposta de sucesso retorna um código de status 204 sem conteúdo para indicar que o recurso foi removido com sucesso.

## Confirmação
Ao enviar uma solicitação DELETE, é importante ter cuidado por a ação é geralmente irreversível.


![[Pasted image 20250518181715.png]]

---
# SLL

O SLL( Secure Sockets Layer) é um protocolo que criptografa os dados trocados entre navegadores servidor da WEB.
Ele garante  uma comunicação  segurança, protege informações confidenciais e gera confiança entre os usuários.

![[Pasted image 20250518181901.png]]

# introdução Api

![[Pasted image 20250518183116.png]]

---

# URL

### Url base:
Uma **URL base** (ou _base URL_) é o segmento inicial e fixo de um endereço na web
que serve como ponto de partida para resolver caminhos relativos ou agrupar recursos sob um mesmo domínio/contexto.

```
https://mercado.com.br
```


---

# Anatomia da resposta de uma api

#### StatusCode

A respota de uma chamada de Api inclui um código de status que indica se a solicitação foi bem-sucedida, como erro e etc..

#### Headers

Assim como  na notificação, a resposta também pode incluir headers adicionais que fornecem informações sobre o contudo,
cache, autenticação, etc...

#### Corpo da Resposta

O compor da resposta contém os dados retornados pela APi. pode ser um documento JSON, XML, HTML ou qualquer outro formato adequado.


---

# Processando a resposta da Api

Depois de fazer um a chamada de API, precisamos extrair os dados relevantes para serem utilizados em nosso app


---
#  Código de Status HTTP


| Codigo | status                   |
| ------ | ------------------------ |
| 200    | Ok                       |
| 201    | Criado                   |
| 204    | Sem Conteúdo             |
| 400    | Requisição invalida      |
| 401    | Não autorizado           |
| 403    | Proibido                 |
| 404    | Não encontrado           |
| 500    | Erro Interno do Servidor |

## Entendendo os códigos de Status

![[Pasted image 20250519161026.png]]

![[Pasted image 20250519161533.png]]

![[Pasted image 20250519161947.png]]