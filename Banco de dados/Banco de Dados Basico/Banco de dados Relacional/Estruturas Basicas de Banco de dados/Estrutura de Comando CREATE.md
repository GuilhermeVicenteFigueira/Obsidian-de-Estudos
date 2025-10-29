## Criando estruturas
- O comando CREATE serve para estar realizando tanto a criação da TABLE ou o DATABASE

Sintaxe para a ***criação do banco de dados***:
```
CREATE DATABASE ecomerce;
```

Sintaxe para a ***criação de tabelas***:
```
CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    idade SMALLINT,
    quantidade_compras INTEGER,
    pontos_acumulados INT,
    ticket_medio NUMERIC(10,2),
    desconto_medio DECIMAL(5,2),
    estado CHAR(2),
    nome VARCHAR(100),
    observações TEXT,
    ativo BOOLEAN,
    data_nascimento DATE,
    hora_cadastro TIME,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    atualizado_em TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    notas INTEGER[],
    tags TEXT[],
    informacoes_extras JSONB
);
```