[This]
[Vaargs]
[main]

Métodos são função / Perecimentos que são definidos dentro de uma classe que realiza um comportamento devido pelo programador.

inicialmente todo método tem seu motificador de acesso:

- Public
- Private

Logo após a declaração de um método, ele pode ser do tipo `void` ou ter um tipo de retorno (como `int`, `double`, `String`, ou até um objeto), e **cada um tem uma aplicação diferente**:

- **Métodos `void`** são usados quando o método **executa uma ação**, mas **não precisa devolver nenhum valor** para quem o chamou. Eles apenas fazem algo (como imprimir, alterar o estado de um objeto, salvar no banco de dados etc.) e **não retornam resultado**.


- Métodos com `return` são usados quando você quer que o método **realize um cálculo, busque ou processe algo** e **devolva um resultado** para quem o chamou. Esse resultado pode ser de **qualquer tipo**, como `int`, `double`, `String`, `boolean`, ou até um objeto.

O `return` **encerra o método** e **entrega um valor de volta**.

### 🚨Exemplo:

```
public int somar(int a, int b) {
    return a + b;
}
```
- Esse método soma dois números e **retorna o resultado**.
    
- Você pode armazenar esse resultado ou usá-lo diretamente:
```
int resultado = somar(5, 3);
System.out.println("Resultado: " + resultado); // imprime 8

```

### 🧠 Dica importante:

- Um método com `return` **sempre precisa retornar algo compatível com o tipo declarado**.
    
- Se você declarar `public String getNome()`, ele **deve retornar uma `String`**, senão o código nem compila.


### Comparando com void:

| Tipo de método | Objetivo Principal     | Retonar valor? | Exemplo                            |
| -------------- | ---------------------- | -------------- | ---------------------------------- |
| void           | Fazer uma ação         | ❌Não           | Mostra mensagem, salva dados etc.. |
| Com Return     | Calcular ou busca Algo | ✅Sim           | Somar números, pegar nome          |

---

## 📌 **Parâmetros de Tipo Primitivo**

Quando passamos **variáveis de tipos primitivos** (como `int`, `double`, `char`, `boolean`, etc.) para um método, o que acontece é que o **valor é copiado**.  
Ou seja, o método recebe **uma cópia da variável original**, e **qualquer alteração feita dentro do método não afeta a variável original**.

```
public class Teste {
    public static void alterarValor(int numero) {
        numero = 99;
    }

    public static void main(String[] args) {
        int x = 10;
        alterarValor(x);
        System.out.println(x); // Vai imprimir 10
    }
}
```

- Mesmo que `numero` tenha sido alterado para `99`, **a variável `x` continua sendo 10**, porque foi passada **uma cópia**, não uma referência.
### ✅ Conclusão:

> Tipos primitivos em Java são passados **por valor**, e **não afetam a variável original** fora do método.

![[Pasted image 20250705191937.png]]

---

### Parâmetros tipo Referencia

### ✅ **Parâmetro por referência — Definição correta:**

**Passagem por referência** significa que **o método ou classe recebe uma **referência direta ao objeto original**, e **não uma cópia**. Com isso, **qualquer alteração feita no objeto dentro do método/classe afeta o objeto original** fora dele.

---

### 🔍 Exemplo em pseudocódigo (parecido com Java):

```
class Produto {
    String nome;
}

void alterarNome(Produto p) {
    p.nome = "Espada Lendária"; // altera o original!
}

Produto minhaArma = new Produto();
minhaArma.nome = "Espada de Ferro";

alterarNome(minhaArma);

System.out.println(minhaArma.nome); // Saída: "Espada Lendária"

```


➡️ **Aqui o objeto `minhaArma` foi passado por referência.** O método **não criou uma cópia**, apenas manipulou diretamente o mesmo objeto.

---

### ❌ O que seria passagem por valor?

No caso de **tipos primitivos** (int, float, etc.), normalmente é **passado por valor** — ou seja, uma **cópia** do dado é enviada para o método.

```
void alterarValor(int numero) {
    numero = 10;
}

int x = 5;
alterarValor(x);
System.out.println(x); // Saída: 5 — o valor original NÃO foi alterado

```

---

### ✅ Resumo simples:

|Tipo de dado|Forma comum de passagem|O que acontece?|
|---|---|---|
|Objeto (classes)|Referência|Método altera o original|
|Primitivo (int, etc)|Valor|Método NÃO altera o original|

---

### 🎯 **Por que um objeto é alterado ao ser passado por referência?**

Quando você passa um **objeto** como parâmetro para um método ou o usa em outra classe, **você está passando o endereço de memória onde ele está armazenado** — e não uma cópia dele.

Ou seja:

> A variável do método aponta para o **mesmo objeto** que a variável original.

---

### 🧠 Imagine assim:

1. Você tem um objeto chamado `espada`.
    
2. Esse objeto está guardado na memória, por exemplo, no "armário A".
    
3. Quando você passa esse objeto para um método, **você entrega a chave do armário A**, e **não uma cópia da espada**.
    
4. Se o método abrir o armário e pintar a espada de vermelho... quando você for olhar depois, a sua espada está vermelha!
    

---

### 📦 Exemplo visual (em pseudocódigo):

```
`Produto espada = new Produto();  espada.nome = "Espada de Ferro";`

```


- O objeto `espada` está em um endereço de memória: por exemplo, `0xA123`.
    

java

```
`alterarNome(espada);`
```



- O método `alterarNome` recebe a **referência para o mesmo endereço** `0xA123`.
    

```
void alterarNome(Produto item) {
    item.nome = "Espada de Fogo"; // Altera o conteúdo do mesmo local (0xA123)
}

```


➡️ Então, **não é cópia**. O método acessa e modifica **o mesmo objeto** na memória.

---

### ⚠️ Em contrapartida:

Se fosse um **tipo primitivo** (como `int`), o valor seria copiado, e a alteração só existiria dentro do método.

---

### ✅ Conclusão:

- Um objeto é alterado porque você está **manipulando a mesma referência** na memória.
    
- Ou seja, **várias variáveis podem apontar para o mesmo objeto**, e mudar por uma muda para todas.

---
### 🚨Representação Visual

![[Pasted image 20250708192811.png]]


---
Metodo De Referencia This:


### ✅ Definição correta de `this` em POO:

**`this`** é uma **referência ao próprio objeto atual** — ou seja, **ao objeto que está executando o método** naquele momento.

---

### 🧠 De forma simples:

> "`this` é como dizer: ‘**eu mesmo**’, dentro do próprio objeto."

---

### ✍️ Quando usamos `this`?

1. **Para acessar atributos e métodos do próprio objeto atual.**
    
2. **Para diferenciar atributos de parâmetros (quando têm o mesmo nome).**
    
3. **Para encadear construtores** (em linguagens que permitem isso, como Java).
    
4. **Para retornar o próprio objeto** (muito comum em _method chaining_).
    

---

### 📌 Exemplo em pseudocódigo:

```
class Pessoa {
    String nome;

    // Construtor
    Pessoa(String nome) {
        this.nome = nome; // aqui, 'this.nome' é o atributo e 'nome' é o parâmetro
    }

    void falar() {
        System.out.println(this.nome + " está falando"); // acessando o próprio nome
    }
}
```


Sem o `this`, o código ainda **poderia funcionar**, mas **se os nomes forem iguais**, ele **não saberia se está usando o parâmetro ou o atributo**.

---

### 🧠 Analogia:

Imagine que você está escrevendo um bilhete:

> "_Vicente está estudando POO com afinco._"

Se fosse o objeto "Vicente" escrevendo sobre si mesmo, ele usaria:

> "_**Eu mesmo** estou estudando POO com afinco._"

➡️ Isso é o papel de `this`.

---

### ✅ Resumo rápido:

|Uso do `this`|Serve para...|
|---|---|
|`this.atributo`|Diferenciar entre atributo e parâmetro|
|`this.metodo()`|Chamar métodos do próprio objeto|
|`return this;`|Retornar o próprio objeto (útil em encadeamento)|
|`this()`|Chamar outro construtor da mesma classe|

![[Pasted image 20250708195357.png]]

---

### Métodos Varargs

**Métodos Varargs** são uma funcionalidade do Java que permite passar uma quantidade variável de argumentos para um método, sem precisar criar um array manualmente. Eles são declarados usando `...` após o tipo do parâmetro. Um exemplo disso é o método `main(String... args)`, onde os argumentos da linha de comando são recebidos como um array de forma simplificada.

A sintaxe usa `...` depois do tipo, como neste exemplo:

```
public static void imprimirNomes(String... nomes) {
    for (String nome : nomes) {
        System.out.println(nome);
    }
}

```

Você pode chamar esse método assim:

```
`imprimirNomes("Ana", "João", "Carlos");`

```


O Java automaticamente transforma os parâmetros em um array (`String[] nomes`) dentro do método.

---

### 💡 Sobre o `main`:

O método `main` também usa **varargs**:

```
`public static void main(String... args)`
```

Essa forma é **equivalente** a:
```
`public static void main(String[] args)`
```

Ou seja, no `main`, o `String... args` é só uma forma simplificada de dizer que ele pode receber vários argumentos da linha de comando.

-------