
## *Consulta de dados*
- O comando SELECT permite buscar informações armazenadas em uma tabela

Sintaxe:
```
SELECT coluna1, coluna2  FROM nome_tabela;
```

---

> [!NOTE] 
> ### Dicas:
> - SELECT * FROM nome_tabela
>  - Busque trazer somente os dados necessário em casa consulta, pois cada solicitação gera um custo de hardware.

---

Comando:
```
SELECT
    id,
    nome,
    idade,
    estado,
    informacoes_extras
FROM
    clientes;
```