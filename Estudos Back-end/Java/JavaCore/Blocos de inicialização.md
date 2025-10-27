### ✅ O que são **blocos de inicialização** em Java?

**Blocos de inicialização** são trechos de código **entre chaves `{}` fora de métodos**, usados para **executar lógica de inicialização** quando:

- Uma **classe é carregada** (`static`)
    
- Ou um **objeto é criado** (bloco de instância)
    

---

### 📘 Tipos:

#### 1. 🔹 **Bloco de inicialização de instância**

- Executado **toda vez que um objeto é criado**
    
- É executado **antes do construtor**
    

```
`public class Exemplo {     {         System.out.println("Bloco de instância executado");     }      public Exemplo() {         System.out.println("Construtor executado");     }      public static void main(String[] args) {         new Exemplo();         new Exemplo();     } }`
```



**Saída:**



`Bloco de instância executado Construtor executado Bloco de instância executado Construtor executado`

---

#### 2. 🔸 **Bloco de inicialização estático (`static`)**

- Executado **somente uma vez**, quando a **classe é carregada**
    
- Usado para **inicializar atributos estáticos**
    



```
public class Exemplo {     
	static {         
	System.out.println("Bloco estático executado");    
		}     
	public static void main(String[] args) {         System.out.println("Método main executado");     } }`
```

**Saída:**


`Bloco estático executado Método main executado`

---

### 🧠 Para que serve?

|Situação|Use bloco de inicialização quando:|
|---|---|
|Atributos precisam ser configurados|Antes do construtor ou sem criar vários construtores|
|Código de setup que pertence à classe|Ex: carregar arquivos, configurar sistema|
|Inicialização complexa de atributos estáticos|Mais que simples atribuição (`static { ... }`)|

---

### ⚠️ Cuidados:

- **Não substitui o construtor**, apenas o complementa.
    
- **Evite abusar**, pois pode prejudicar a legibilidade.
    
- Para lógica simples, prefira inicializar direto no atributo ou usar construtores.