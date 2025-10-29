## ***Regras de integridade - Integridade de Identidade***

- A chave primaria não pode conter valores nulos;

- Como toda informações em um banco de dados relacional precisa ter uma identidade exclusiva, a chave primaria deve ser obrigatoriamente preenchida.

- Além disso, a chave primaria não ser deve ter valores repetidos em uma tabela, de forma a garantir que exista apenas uma linha  parra cada valor definido para a chave primária.


## ***Regras de integridade - Integridade de Referencia***

- Se  uma determinada tabela A possui uma chave estrangeira que estabelece relacionamento com uma tabela B, então o valor da chave estrangeira da tabela A deve ser igual a um valor de chave primária na tabela B.

- Esta regra garante que as referencias  de uma tabela  apara outra tabela sejam válidas, de forma que os relacionamentos sejam consistentes e não ocorra inconsistência no dados.
## ***Regras de integridade - Integridade de Domínio***

- Restringe o conjunto de valores que pode ser gravados em uma coluna de uma tabela, Desta forma, somente os valores que pertencem ao domínio podem ser gravados na coluna da tabela. Outros valores não são permitidos e a atualização é desfeita pelo gerenciador de banco de dados