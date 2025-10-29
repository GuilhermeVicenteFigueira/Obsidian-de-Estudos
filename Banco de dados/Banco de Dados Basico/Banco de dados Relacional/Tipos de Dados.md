### *Os principais tipos de dados do banco de dados são:*

### **[[Dados Numéricos]]**

| Numericos                                                           | Exemplos de Uso                                                                                        | Descrição                                                                                                                                                                                           |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Integer {<br>INT,<br>INTEGER,<br>SMALLINT,<br>BIGINT,<br>}          | idade = SMALLINT(32,767 de unidade)<br>quantidade = INT<br>população = BIGINT                          |                                                                                                                                                                                                     |
| Decimal{<br>NUMERIC,<br>DECIMAL,<br>REAL,<br>DOUBLE PRECISION,<br>} | salario NUMERIC(10,2)<br>porcentual DECIMAL(5,3)<br>temperatura REAL<br>distancia DOUBLE PRECISION<br> | Numeric = Valores monetários (10,2 casa decimais).<br>Decimal = porcentagem com alta precisão<br>Real = Parea medições criticas (32 bits)<br>Double Prcision para medições de alta escala (64 bits) |

### **[[Dados de Texto]]**

| Texto   | Exemplos de Uso<br> | Descrição                              |
| ------- | ------------------- | -------------------------------------- |
| Char    | sigla Char(3)       | taxto de tamanho fixo.                 |
| VarChar | nome Varchar(100)   | Texto com tamanho variável com limite. |
| Text    | descricao Text      | Texto de tamanho ilimitado.            |

### **[[Dados do tipo Boolean]]**

#### BOOLEAN
-  Armazena valores lógicos: True, False, NULL
- Ideal para status, flags de ativação, verificações binárias.

| Tipo    | Exemplo de Uso | Descrição                                                        |
| ------- | -------------- | ---------------------------------------------------------------- |
| BOOLEAN | ativo BOOLEAN  | Representa verdadeiro falso.<br>Ex: usuario ativo, visivel, etc. |

### **[[Dados do tipo DATA e HORA]]**


| Tipo        | Exemplo de Uso            | Descrição                                                            |
| ----------- | ------------------------- | -------------------------------------------------------------------- |
| DATE        | nascimento DATE           | apenas a data(ano,mês,dia)                                           |
| TIME        | hora-abertura TIME        | apenas o horarios(hora, minuto, segundo)                             |
| TIMESTAMP   | criado_em TIMESTAMP       | Data e hora (sem fuso horário).                                      |
| TIMESTAMPTZ | evento_inicio TIMESTAMPTZ | Data e hora com **fuso horario**. <br>Ideal para **sistema globais** |


### **[[Dados  UUID/ Serial]]**

| tipo   | Exemplo               | Descrição                                                              |
| ------ | --------------------- | ---------------------------------------------------------------------- |
| SERIAL | id SERIAL PRIMARY KEY | Valor auto-incrementado<br>automaticamente a cada novo registro        |
| UUID   | id  UUID PRIMARY KEY  | Identificador único global. Precisa ser gerado via função ou aplicação |


> [!NOTE] 
> #### **Dicas**
> para que gere automático o incremental é necessário utilizar o comando:
> *uuid_gerete_v4()*



## **[[Dados do tipo ARRAY]]**

| tipos     | Exemplo de Uso  | Descrição         |
| --------- | --------------- | ----------------- |
| INTEGER[] | Notas INTEGER[] | Lista de Inteiros |
| TEXT[]    | tags TEXT[]     | Lista de Texto    |

## **[[Dados do tipo JSON  e JSONB]]**


| Tipos | Exemplo de Uso | Descrição                                                          |
| ----- | -------------- | ------------------------------------------------------------------ |
| JSON  | dados JSON     | armazena dados estruturados como texto.<br>Preserva a ordem.       |
| JSONB | dados JSONB    | **Armazena como Binário otimizado**. mais eficente para consultas. |

[^1]: 
