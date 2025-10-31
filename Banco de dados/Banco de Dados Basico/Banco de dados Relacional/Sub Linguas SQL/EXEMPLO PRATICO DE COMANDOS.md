
> [!NOTE] ***COMANDOS DE WHERE (FILTRO)***

```
-- JUNTA O PRIMEIRO NOME  E O SEGUDO NOME, EM UMA COLUNA TEMPORARIA CHAMDA DE FUL_NAME E CONCATE OS DOIS DENTRO DELA, EM SEGUIDA FILTRA AS CIDADES POR SÃO PAULO

-- SELECT customer_id, first_name || ' ' || last_name AS full_name, city FROM customers -- Concatena , primeiro nome + segundo nome e transorma em full_name
-- WHERE  city = 'São Paulo'; -- Filtra por cidade

-- FILTRA POR CATEGORIA 3

-- SELECT product_id, product_name, category_id FROM products
--  WHERE category_id = 3;


-- FILTRA PARA TUDO MENOS DELIVERED

-- SELECT order_id, status
-- FROM orders
-- WHERE  status <> 'SHIPPED';


-- FILTRA PARA MENOR DO QUE A DATA DE 01-06-2024

-- SELECT customer_id, created_at FROM customers
-- WHERE created_at < '2024-06-01';

-- FILTRA POR PRICE <= 20;
    
-- SELECT product_id, price
-- FROM products
-- WHERE price <= 20;

-- IINSERE UM NOVO CUSTOMER COM UM CAMPO EM NULO, E DEPOIS SELECIONAMOS O QUE ESTÁ COM O CAMPO VAZIO (LAST_NAME) E DEPOIS SELECIONAMOS TODOS QUE ESTÁ COM O CAMPO NÃO NULO  

-- INSERT INTO  customers(customer_id, first_name, last_name, email, city, created_at)  
-- VALUES (333, 'João', NULL, 'joão.silva1@exempli.com', 'São Paulo', '2024-05-17');  
-- SELECT * FROM customers WHERE last_name IS NULL;  
-- SELECT * FROM customers WHERE last_name IS NOT NULL;

```

---

> [!NOTE] ***COMANDOS AND E OR***

```
-- FILTRA A BUSCA PARA CLIENTE QUE MORAM EM SP JUNTO AO CADASTRO MAIOR QUE 01-01-2024: 

-- SELECT customer_id, first_name, last_name, city  
-- FROM customers  
-- WHERE city = 'São Paulo'  
--   AND created_at >= '2024-01-01';  
  
-- FILTRA O STATUS POR SHIPPED OU PENDING:
  
-- SELECT customer_id,  status from orders  
-- WHERE status = 'SHIPPED' OR status ='PENDING';  
  
  
--  FILTRA O OS STATUS E O TOTAL VENDIDO, ONDE O STATUS PODE SER SHIPPED OU DELIVERID, MAS SÓ VAI MOSTRAR OS VALORES ACIMA DE 600: 

-- SELECT order_id, total_amount, status  
-- FROM orders  
-- WHERE(status = 'SHIPPED' OR status ='DELIVERED')  
-- AND total_amount > 600;  
-- primeiro avalia parentes (status), depois total_mout > 600
```

---

> [!NOTE] ***COMANDOS: IN, NOT IN***

```
-- FAZ A FILTRAGEM DE TODOS OS STATUS QUE SÃO PENDING E SHIPPED: 
  
-- SELECT order_id, status  
-- FROM orders  
-- WHERE status IN ('PENDING', 'SHIPPED');  
  
--  FAZ A FILTRAGEM DAS CETEGORIAS POR ID 1,3,5: 
  
-- SELECT product_id, category_id  
-- FROM products  
-- WHERE category_id IN (1,3,5);  
  
-- FILTRA OS CUSTOMERS POR CIDADE MANAUS OU REFICE OU FORTALEZA:

-- SELECT customer_id, city  
-- FROM customers  
-- WHERE  city = 'Manaus' or city = 'Recifie' or city = 'Fortaleza';  
  
  
-- FILTRA OS PRODUTOS  POR TODOS MENOS  2 , 4, 6: 

-- SELECT product_id, product_name , category_id FROM products  
-- WHERE category_id NOT IN (2,4,6)
```

---

> [!NOTE] ***COMANDOS BETWEEN***
> 
> Não é recomendado utilizar BETWEEN com String, ela tem margem de erro, use apenas para data e numero

 ```
 -- FILTRAR PRODUTOS COM O PREÇO ENTRE 150 ATÉ 300 NADA ALÉM DISSO  
  
-- SELECT  product_id, price  
-- FROM products  
-- WHERE price BETWEEN 150 AND 300;  
  
-- FILTRAR OS CUSTOMERS CIDADE SP OU  RJ E QUE FOI CRIADO ENTRE 2024 01 01 ATÉ  2024 12 01  
-- Jeito 1:  
    -- SELECT customer_id, city, created_at::DATE  
-- FROM customers  
-- WHERE (city = 'Rio de Janeiro' or city = 'São Paulo')  
-- AND created_at::DATE BETWEEN '2024-01-01' AND '2024-12-01';  
    --  jeito 2  
    --  AND created_at::DATE >= '2024-01-01'  
--  AND created_at::DATE <= '2024-12-01';
 ```
 
---

> [!NOTE] COMANDO WHERE COM LIKE

```
-- FILTRAR CUSTOMERS COM BASE NO PRIMEIRO NOME QUE COMEÇA COM "JU"  
--  
-- SELECT customer_id, first_name  
-- FROM customers  
-- WHERE first_name LIKE 'Ju%'  
  
  
-- FILTRAR CUSTOMERS COM BASE NO PRIMEIRO NOME QUE COMEÇA COM "Lherme"  
  
-- SELECT customer_id, first_name  
-- FROM customers  
-- WHERE first_name LIKE '%lherme'  
  
-- FILTRAR CUSTOMERS COM BASE NO ULTIMO NOME COM "Silva"  
  
-- SELECT customer_id, first_name, last_name  
-- FROM customers  
-- WHERE last_name LIKE '%Silva'  
  
-- FILTRAR CUSTOMERS COM BASE NO ULTIMO NOME COM "Silva"  
  
-- SELECT customer_id, first_name, last_name  
-- FROM customers  
-- WHERE last_name LIKE '%il%'  
  
-- FILTRA PRODUTOS COM O NOME QUE CORRESPONDE "RODUTO 1%" , PODENDO SER "PRODUTO 1%" OU "ZRODUTO 1%"  
--  
-- SELECT products.product_id, products.product_name  
-- FROM products  
-- WHERE product_name LIKE '_roduto 1%'
```

---

> [!NOTE] COMANDO COUNT

```
-- 1.1 COUNT(*) CONTA TODAS AS LINHAS, MESMO COM NULL:

-- SELECT COUNT(*) AS total_pedidos  
--  FROM orders; 
-- total de pedidos (inclui todos os registros)

-- 1.2 COUNT(coluna) conta somente valores não nulos na coluna:

-- SELECT COUNT(*)--customers.last_name) --AS total_customers_nao_nulos  
-- FROM customers;  

-- SELECT * FROM customers  

-- SELECT DISTINCT customers.last_name 
 
-- FROM customers;  
-- SELECT * FROM customers  
  
-- 1.3 CONT(DISTINCT coluna) conta valores distintos  
-- Quantos clientes  únicos fizeram pedidos:
  
-- SELECT count( DISTINCT o customers_id) AS clientes_unicos  
--    FROM orders o
```

---

> [!NOTE] ***COMANDOS SUM, AVG, MIN E MAX***
> - SUM: SOMA
> - AVG: MEDIA
> - MIN: MINIMO
> - MAX: MAXIMO

```

-- 3.1 MAX(coluna) RETORNA MAIOR VALOR; MIN(COLINA) RETORNAR O MENOR VALOR  
-- ENCONTRAR O PREÇO MAXIMO E O PREÇO MINIMO ENTRE PRODUTOS  
  
-- SELECT MAX(price) AS produto_maximo,  
--     MIN(price) AS produto_minimo  
-- FROM products;  
  
-- -- 3.3 EXEMPLO: "DATA MINIMA DE REGISTRO" EM CUSTOMERS (PRIMEIRO CLIENTE CADASTRO)  
-- SELECT MAX(customers.created_at) as primeira_data_cadastro  
--     FROM customers

```

---

> [!NOTE] ***ORDER BY***

```
-- 1.1 SINTAXE BÁSICA: ORDENAR PRODUTOS PELO PREÇO EM ORDEM ASCENDENTE  

-- SELECT products.product_id, products.product_name, products.price  
-- from products  
-- ORDER BY  PRICE DESC;--ASC; -- MENOR AO MAIOR  
  
-- SELECT *  
-- FROM customers  
-- ORDER BY first_name DESC  
  
  
-- 1.3 ORDENAÇÃO POR MULTIPLAS COLUNAS: PEDIDOS POR STATUSE DEPOIS POR DATA (ASCENTE)  

-- SELECT order_id, status, order_date  
-- FROM orders  
-- ORDER BY status ASC, order_date ASC; -- PRIMEIRA ORDENA POR STATUS, DEPOIS POR DATA

```

---


> [!NOTE] ***GROUP BY***

```
EXEPLO BASICO: AGRUPAR ITENS PEDIDOS POR PRODUCT_ID E CONTAR QUANTAS VEZES CADA PRODUTO FOI VENDIDO  
  
-- SELECT product_id,  
--        SUM(quantity) AS total_vendas  
-- FROM order_items  
-- GROUP BY  product_id ;  
  
-- AGRUPAR PEDIDOS POR STATUS E CONTAR QUANTOS PEDIDOS EXISTEM EM CADA STATUS  
  
-- SELECT status,  
-- COUNT(*) AS qtde_pedidos  
-- FROM orders  
-- GROUP BY status;  
--  
-- SELECT DISTINCT  status FROM orders  
  
-- AGRUPAR USUARIOS POR CIDADE E VER O TOTAL_CLIENTES  
  
-- SELECT customers.city,  
-- count(*) AS total_clientes  
-- FROM customers  
-- GROUP BY city;  
  
-- AGRUPAR USUARIOS POR DATA DE CRIAÇÃO  
  
-- SELECT customers.created_at,  
-- count(*) AS total_clientes  
-- FROM customers  
-- GROUP BY created_at

```

---