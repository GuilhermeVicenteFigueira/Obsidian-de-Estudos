**O construtor** (`constructor`) é um método especial usado para **inicializar objetos** de uma classe. Ele é chamado **automaticamente** no momento em que o objeto é criado com `new`.

Se a classe precisa de certos valores (como nome, idade, etc.) para funcionar corretamente, você pode **exigir esses valores no construtor**. Assim, **nenhum objeto será criado sem essas informações**.

```
public class Produto {
    private String nome;
    private double preco;

    // Construtor da classe Produto
    public Produto(String nome, double preco) {
        this.nome = nome;
        this.preco = preco;
    }

    public void exibir() {
        System.out.println("Produto: " + nome + " - R$ " + preco);
    }

    public static void main(String[] args) {
        // Criando um objeto já com os dados obrigatórios
        Produto p1 = new Produto("Mouse", 79.90);
        p1.exibir();

        // Produto p2 = new Produto(); ❌ Isso daria erro, pois o construtor exige 2 parâmetros
    }
}
```
### Resumo:

- O **construtor** tem o mesmo nome da **classe**.
    
- **Não tem tipo de retorno** (nem `void`).
    
- Pode ter **parâmetros obrigatórios** para garantir que o objeto só seja criado com os dados corretos.
    
- Se nenhum construtor for definido, o Java cria um construtor **padrão vazio** automaticamente.
---
### 🔄 **O que é sobrecarga de construtor?**

**Sobrecarga** significa criar **vários construtores** dentro da mesma classe, mas com **diferentes quantidades ou tipos de parâmetros**.

Isso permite que um objeto possa ser criado de **várias formas**, dependendo das informações disponíveis no momento da criação.

```
public class Produto {
    private String nome;
    private double preco;

    // Construtor 1: recebe nome e preço
    public Produto(String nome, double preco) {
        this.nome = nome;
        this.preco = preco;
    }

    // Construtor 2: recebe apenas nome (preço padrão será 0.0)
    public Produto(String nome) {
        this.nome = nome;
        this.preco = 0.0;
    }

    // Construtor 3: sem parâmetros (nome e preço padrão)
    public Produto() {
        this.nome = "Desconhecido";
        this.preco = 0.0;
    }

    public void exibir() {
        System.out.println("Produto: " + nome + " - R$ " + preco);
    }

    public static void main(String[] args) {
        Produto p1 = new Produto("Mouse", 79.90);
        Produto p2 = new Produto("Teclado");
        Produto p3 = new Produto();

        p1.exibir(); // Produto: Mouse - R$ 79.9
        p2.exibir(); // Produto: Teclado - R$ 0.0
        p3.exibir(); // Produto: Desconhecido - R$ 0.0
    }
}

```

### 🧠 **Resumo rápido:**

- A sobrecarga permite ter **vários construtores com parâmetros diferentes**.
    
- O Java escolhe **automaticamente o construtor correto** com base nos argumentos passados na criação do objeto.
    
- Você pode definir **valores padrão** em construtores mais simples, se desejar.