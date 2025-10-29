## ***[[O que é chave Primária?]]***
 - Um Atributo (ou conjunto de atributos) que identifica unicamente cada tupla (linha) em uma tabela;
 - Não pode conter valores nulos;
 - ***Deve ser única*** em todos os registros;
 - ***Exemplo***: CPF, Matricula, ID_cliente.

### ***[[Por que é Importante?]]***
- Garante a integridade dos dados.
- Permite busca eficiente e atualizações seguras;
- Base para relacionamentos entre tabelas (referência em chaves estrangeiras)
- É usada para indexação automática em muito SGBDs.

### ***[[Critérios para uma Boa Chave Primária]]***
- ***Unicidade***: não se repetelmutabilidade: não deve mudar como o tempo;
- ***Não nula***: obrigatório para cada registro
- ***Estabilidade***: valor confiável ao longo do tempo.
- ***Simplicidade***: idealmente curto e fácil de indexar;
- Naturalidade ou substituição consciente,

### ***[[Nomenclatura]]***
- Tipos de nomes para a chave primaria: ***PK,ID,SKU***

###  ***[[Tipos de Chave]]***

#### *Chave Natural:*
- Já existe nos dados reais;
- ***Exemplo:*** CPF, Email ,matrícula escolar
- ***Vantagens:*** significa, fácil de entender
- ***Desvantagens:*** pode mudar, nem sempre é  única universalmente

#### *Chave Substitutiva:*
- Criada artificialmente pelo sistema(ex:ID)
- ***Exemplo:*** id_aluno=1,2,3...
- ***Vantagens:*** estabilidade, simplicidade, controle;
- ***Desvantagens***: não tem significado para o usuário

