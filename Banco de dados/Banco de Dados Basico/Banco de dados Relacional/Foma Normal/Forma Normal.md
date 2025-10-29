
## ***Normalização***

> [!NOTE] 
> ***Da onde Sugiu?***
> - A normalização foi Criada em 1970 por E.F Codd, ela foi baseada em um processo matemático formal fundamentado em teoria do conjuntos 
> - Foi motivado em função de anomalias gravas relação à atualização, inclusão e deleção de elemento no modelo

 
#### *Como isso surgem as formas normais;*
- São tratamentos de decomposição de novas relações de forma a não perder conteúdo e evitar os problemas nos tratamento das informações da tabela.


#### *Exemplo da teoria com base em um gráfico*:

![[Imagem demosntrativa de forma Normal.png]]

#### *Objetivo da normalização:*

- O principal objetivo é purificar gradativamente um conjunto de entidades e relacionamento por  outro, 

-  ***Os problemas que  podem ser eliminados por isso:***
	- Grupo repetido de dados.
	- Dependências parciais em relações a uma chave concatenada.
	- Redundância de dados desnecessário.
	- Perdas de informação dificuldade na representação de fatos de realidade observada.
	- Dependências transitivas entre atributos.

## ***Dependência Funcional***

- Uma dependência funcional é um relacionamento entre dois ou mais atributos de forma que o valor de um atributo identifique o valor para cada um dos outros atributos, ou seja, um atributo está relacionado a outro.

- A->B : atributo B Depende de A(funcionalmente) do atributo A, Isso significa que para descobrirmos o valor de B, preciso saber antes o valor de A

## ***Dependência Funcional Parcial***

- Ocorre quando os atributos não chave não dependem funcionalmente de toda a chave primária quando está for composta;

- Assim, nas tabelas onde a chave primária for composta, todos os atributos dever depender de toda a chave primária.

- Caso a dependência seja a parte da chave, verificamos a existência de pendencia funcional parcial 

## ***Dependência Funcional Transitiva***

- Na definição dos campos de uma entidade podem ocorrer casos em que o campo não seja dependente diretamente da chave primaria ou da parte dela, mas caracteriza a dependência funcional transitiva 

## ***Dependência Funcional Multivalorada***

- Ocorre quando, para cada valor de atributo A, há um conjunto de valores para outros atributos B e C estão associados a eles, mas são independentes entre si.