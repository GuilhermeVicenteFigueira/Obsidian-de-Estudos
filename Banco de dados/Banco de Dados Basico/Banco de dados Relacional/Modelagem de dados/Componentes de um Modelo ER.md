## ***[[Entidade]]***
- Uma entidade consiste em um objeto/ conceito ou evento que é fundamental para um sistema, e para o seu banco de dados.
### *Tipos de entidade*;

#### *Entidade Forte/ independente;*
- Existe por conta própria;
- Exemplo: Cliente / Produto / Talonário / Multa 

#### *Entidade fraca/dependente*;
- Só existe por causa de outra entidade.
- Exemplo: ItemPedido( depende de Pedido e Produto);


## ***[[Atributos]]***
- Propriedade ou característica de entidade;
- Exemplo; Aluno->nome, matricula, data de nascimento
- representado por elipses ligadas as entidades.

### *Tipos de atributos*

#### *Simples/Âtomico;*
- Não pode ser dividido: Nome , Idade , cpf.

#### *Composto:*
- Pode ser dividido: endereço->rua , numero , cidade.

#### *Derivado:* 
- Pode ser calculado: idade(a partir da data de nascimento)

#### *Multivalorado:*
- Pode conter mais de um telefones;

## ***[[Relacionamento]]***
- Um relacionamento liga duas ou mais entidades;
- Representa uma associação lógica entre dados;
- Exemplo; Aluno se matricula em Cruso, Relacionamento é representado com um losango nos diagramas ER

### *Tipos de Relacionamento;*


> [!NOTE] 
> ### *Importante saber!*
>  ##### Grau = Quantidade de entidades envolvidas.

#### *Binário:*
- Duas entidades ***Mais Comum**.
- ***Exemplo:*** Funcionário trabalha em Departamento.
- Pode ter ***[[Cardinalidade]]***;

#### *Ternário:*
- Três entidades.
- Não pode ser modelado com três relacionamento binários
- ***DEVE*** ser representado com um único losango conectado a 3 entidades
#### *N-ário:*
- Mais de três entidades.

#### *Recursivo*:
- Entidade se relaciona com ela mesma.
- ***Exemplo***: Funcionário gerencia Funcionário.
- Exige papéis (***Ex:*** "Gerente", "Subordinado") no diagrama.
- ***Representado:*** com uma seta que volta para a mesma entidade.
#### *Atributos*:
- Alguns Relacionamentos possuem informações próprias.
- ***Exemplo:*** Aluno->Matricula->Curso;
- Atributo de relacionamento: Data de matricula, nota.
- ***Representado*** por elipse ligado ao Losango


---

## ***[[Cardinalidade]]***

### *Tipo de Cardinalidade*
- Define quantos registros de uma entidade se associam à outra;

#### *1:1 -> Um para Um*

#### *1:N -> Um para Muitos*

#### *N:N -> Um para Muitos*

