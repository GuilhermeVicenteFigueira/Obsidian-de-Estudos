
## ***Mapeamentos das Entidades***

- Toda entidade terna-se uma tabela levando todos os atributos definidos na entidade que tornam-se colunas na tabela criada;

-  O identificador da entidade torna-se  a chave primaria da tabela que permitirá repetição de valores e nem valores nulos

## ***Regras Gerais***

- Atributos derivados não são mapeados
-  atributos mult-valorados podem ser mapeado de duas maneiras
	- Como n Colunas, onde n é o numero máximo de valores do atributo.
	- Criando-se uma nova relação

## ***Mapeamento de Relacionamentos***

#### *Relacionamento 1 para muito(1: N)*
- A entidade cuja a cardinalidade seja N, ela vai receber o atributo identificado da entidade que a cardinalidade seja 1 se tornando um FK para o a entidade com cardinalidade N.

#### *Relacionamento 1 para 1(1: 1)*
- Em resumo  qualquer uma pode ter o Fk da outra basta ela não repetir na outra entidade. 

#### *Relacionamento muitos para muitos (N: N)*
- Em casos de muitos para muitos é necessário criar uma nova tabela, está nova tabela haverá dois Fk das duas entidades e o Pk dessa entidade.

#### *Auto Relacionamento*
- Incluir um Pk da entidade na própria entidade como um FK.

Ilustração abaixo:
![[Auto Relacionamento.png]]
