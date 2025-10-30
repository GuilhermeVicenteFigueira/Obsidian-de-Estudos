DDL engloba os comando responsáveis pela definição e estrutura de banco de dados, isso envolve criar, alterar e remover objetos  como tabelas, inceis, visões (VIEWS), esquema(schemas), etc

## ***Comandos***

### *CREATE:*
- Criar novos objetos (tabelas, índices, sequências, esquemas, view, funções etc..)
````
CREATE DATABASE projeto fabrica de codigos
CREATE TABLE 
````
---
### *ALTER*: 
- Altera a estrutura de um objeto existente
-  Pode ser usado para:
	- Adicionar/Remover/Modificar colunas.
	- Ajustar restrições (constraints).
	- Renomear objetos.

```
-- Adicionar coluna "telefone" na tabela Usuario
ALTER TABLE usuario
	ADD COLUMN telefone VARCHAR(20);


-- Modificar tipo da coluna "telefone" para char(20)
	
ALTER TABLE usuario
	ALTER COLUMN telefone TYPE CHAR(20);
	
-- Renomer a tablea "usuario" para cliente
ALTER TABLE usuarios
	RENAME TO cliente
	
```
---
### *DROP:*
- Remover Objetos do banco (tabelas, views, indices, esquemas, etc.)
- Essa operação é irreversível (a menos que use um backup ou "DROP ... CASCADE" com cautela).

```
-- Deleta o banco de dados
DROP DATABASE;

-- Deleta a tabela Usuario
DROP TABLE usuario;

-- Apagar a view "vw_vendas_mes" se ela existir
DROP VIEW IF EXISTS vw_vendas_mes;
```
---
### TRUNCATE:
 - Remove todas as linhas de uma tabela, sem registrar individualmente cada linha para Rollback
 - è mais rápido  que um DELETE sem WHERE
 - Não remove a estrutura (colunas, restrições, índices), apenas zera dados.

```
-- Excluir rapidamente todos os registros da tabela "orders"
TRUNCATE TABLE orders;
```
---
### RENAME:
- RENAME TABLE usuários TO clientes; 
```
-- (em versões que suportam RENAME)
	RENAME TABLE usuarios TO clientes;
```
---
#### *COMMENT*:
- Adiciona ou altera comentários de descrição para objetos

```
COMMENT ON TABLE produtos IS "Tabela que armazena informações dos produtos da loja";
COMMENT ON COLUMN produtos.price IS "Preço de vendas em reais(BRL)"
```
