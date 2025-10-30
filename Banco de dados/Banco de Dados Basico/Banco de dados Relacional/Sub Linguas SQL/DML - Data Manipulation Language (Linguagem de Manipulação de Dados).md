DML engloba os comandos que servem para inserir, atualizar deletar e em parte, selecionar dados das tabelas. É o "corpo principal " das operações cotidianas de CRUD (Create, Read, Update, Delete)

### INSERT
- insere novas linhas (tuplas) em uma tabela.

 ```
 -- Inserir um único registro
 INSERT INTO cliente (nome, email, data_cadastro)
 VALUES ('Guilherme Vicente', 'figueira.gui1@exemple,com', '2024-05-30')
 
 -- Inserir multiplos registro de uma vez
 INSERT INTO clientes(nome)
 VALUES
	 ('Bruno'),
	 ('Eduardo');
 ```

---
###  UPDATE:
- Modifica valores de colunas para as linhas que satisfazem uma condição (WHERE)

```
-- alterar o email de um cliente especifico
UPDATE clientes
	SET email = 'xaolinMatadorDePorco@exemple.com'
WHERE id = 1;

-- Incrementar preço de todos os produtos em 10%
UPDATE produtos
 SET price = price * 1.10;
```

---
### UNSERT (INSERT... ON CONFLICT)
- Em PostgresSQL, o comando INSERT ... ON CONFLIT (...) DO UPDATE permite inserir, ou caso chave duplicidade (conflict), atualizar o registro

```
INSERT INTO produtos (product_id,  product_name, price)
VALUES (10,'Produto 10', 199.90)
ON CONFLICT (product_id)
DO UPDATE SET price = EXCLUDED.price;
```

---

### UPDATE
- Modifica valores de colunas para as linhas que satisfazem uma condição (WHERE)

```
-- Altera o email de um cliente especifico
UPDATE clientes
	SET email "Vicentao@Exemplo.com"
WHERE id = 1;

-- Incrementar preço de todos os em 10%
UPDATE produtos
	SET price = price * 1.10;
```