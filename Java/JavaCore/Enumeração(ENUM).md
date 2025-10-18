Um `enum` (abreviação de _enumeration_) é uma estrutura especial que representa um **conjunto fixo de constantes**. Ele é muito útil quando queremos restringir os valores possíveis de uma variável, **evitando erros de entrada de dados** como letras minúsculas, números indevidos ou abreviações inconsistentes.

### Por que usar `enum`?

- **Evita erros de digitação** ou variações inesperadas (ex: "ativo", "Ativo", "ATIVO").
    
- Facilita o controle e a validação de valores.
    
- Deixa o código mais legível e organizado.
    
- Pode ser usado diretamente no banco de dados como um valor padronizado.
    

### Onde usar?

`Enum` pode ser utilizado:

- Como uma **classe separada**, quando precisa ser reutilizado em vários lugares.
    
- Como um **tipo dentro de outra classe**, se for algo específico dela.
    

### Como utilizar?

Um `enum` geralmente é combinado com:

- **Construtores**, caso cada constante tenha atributos adicionais.
    
- **Getters** para acessar dados internos.
    
- **Métodos sobrescritos**, se for necessário personalizar o comportamento de cada constante.
    

> ⚠️ Se o objetivo for apenas representar um conjunto fixo de valores que **não devem ser modificados**, o ideal é manter o `enum` imutável, evitando `setters`.

# Exemplo:

```
public enum Status {
    ATIVO,
    INATIVO,
    PENDENTE;
}

```

# Uso:
```
Status status = Status.ATIVO;
```

# Exemplo atribuído em Construtores:

```
public enum TipoCliente {
    PESSOA_FISICA("PF"),
    PESSOA_JURIDICA("PJ");

    private String codigo;

    TipoCliente(String codigo) {
        this.codigo = codigo;
    }

    public String getCodigo() {
        return codigo;
    }
}

```