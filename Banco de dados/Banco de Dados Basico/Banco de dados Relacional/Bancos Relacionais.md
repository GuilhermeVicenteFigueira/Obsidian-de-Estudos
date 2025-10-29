
## ***[[INDEX BANCO DE DADOS RELACIONAL  BASICO]]***

# **SQL**
*Estrutura em tabelas(linhas/registro, colunas/campos)*
*Exemplos: PostgreSQL, MySQL, Microsoft SQL Server*
*Linguagem SQL(Structured Query Language)*


## **Conexões entre tabelas**

*O que conecta as tabelas de um banco de dados relacional é chamado de Key /  Chave Estrangeira  ou id como é naturalmente utilizado, é ideal para dados estruturados* 

## **Comandos Mais Utilizados**

##### *Principais comandos SQL*

- *Create Table* -  Cria tabelas
	Comando:
	
		CREATE TABLE usuarios (
		id SERIAL PRIMARY KEY,
		nome Varchar(100),
		email Varchar(100)
		);
		
- *Insert Into* - insere dados
	Comando:
	
		INSERT INTO usuario(nome,email)
		VALUES('Guilherme', 'vicente@gmail.com'
		);

- *Select* -  Consulta dados
	Comando:
	
		SELECT * FROM usuarios; 

- *Update* - Utiliza dados
	Comando:
		UPDATE usuario 
		SET nome = 'guilherme'

- *Delete* - Exclui dados
	Comando: