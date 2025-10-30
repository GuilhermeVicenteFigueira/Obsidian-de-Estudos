TCL engloba os comandos que controlam o fluxo de transações no banco de dados, garantindo automaticidade, consistência, isolamento  e durabilidade (ACID).
Permite confirmar (commit ) ou defazer (Rollback) uma séria de operações

### *BEGIN (ou STAR TRANSACTION)*:
- Iniciar uma transação explicita.
- A partir desse ponto, todas as operações DML (INSERT, UPDATE, DELETE), fazem parte de uma transação atômica.

``` 
BEGIN;

-- dentro da trnasação, várias operações:
UPDATE contas SET saldo = saldo - 100.00 WHERE id = 1;
UPDATE contas SET saldo = saldo + 100.00 WHERE id = 2;
```

### *COMMIT*
- Confirmar definitivamente todas as alterações realizadas desde o último BEGIN
-  Após o COMMIT, as mudanças tornam-se permanentes e visíveis para outra transações
```
-- comfirmar as alterações feitas
COMMIT;
```

### Rollback
- Desfazer todas as alterações realizadas desde o último BEGIN(ou deste o último ponto de salvamento).
- Último para garantir a integridade quando ocorre em um erro ou condições inesperadas 

```
--  desfazer tudo que foi feito na transação
ROLLBACK;
```

### SAVEPOINT
- Criar pontos intermediários dentro de uma transação que permitem ROLLBACK  parcial até esse ponto, sem descartar tudo.

```
BEGIN;

-- operação A

INSER INTO contas(cliente, saldo) VALUS ('Alice', 1000);

SAVEPOINT sp1;

--operaçãob (pode Falhar)
UPDATE contas SET saldo = 200 WHERE cliente = 'bob';

-- se falhar a opreção b, basta voltar para sp1

ROLLBACK TO SAVE sp1;

INSERT INTO contas (cliente, saldo) VALUES ('Carlos', 500);

COMMIT;
```


### SET TRANSACTION
- Define propriedades da transação, como nível de isolamento (READ COMMITTED, REPEATABLE READ, SERIALIZABLE).

```
SET TRANSACTION ISOLATION LEVEL REAPEATABLE READ;
```