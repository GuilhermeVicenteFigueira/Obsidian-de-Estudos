## Inserindo dados

- O comando INSERT é utilizado para adicionar dados em uma tabela existente;

Sintaxe para ***inserção única;***
````
	INSERT INTO nome_tabela (coluna1, coluna2)
	VALUES(valor1,valor2)
````
---
Sintaxe ***múltipla***:
````
	INSERT INTO nome_tabela (coluna1, coluna2)
	VALUES
	(valor1,valor1,valor1),
	(valor2,valor2,valor2);
````
---

> [!NOTE]
> #### **Dicas!**
> Ao criar uma tabela é essencial definir corretamente os tipos de dados de cada coluna.
> Isso garante a integridade e desempenho e economia do espaço

---

```
INSERT INTO clientes (
    idade,
    quantidade_compras,
    pontos_acumulados,
    ticket_medio,
    desconto_medio,
    estado,
    nome,
    observações,
    ativo,
    data_nascimento,
    hora_cadastro,
    notas,
    tags,
    informacoes_extras
) VALUES (
    30,
    123,
    1500,
    250.75,
    10.00,
    'SP',
    'Guilherme Vicente',
    'Cliente Frequentimente faz muitas compras',
    TRUE,
    '2006-02-15',
    '10:18:00',
    ARRAY[8],
    ARRAY['vip','newletter'],
    '{"preferencias": "email", "idioma": "pt-BR", "aceita_promocoes": true}'
);
```