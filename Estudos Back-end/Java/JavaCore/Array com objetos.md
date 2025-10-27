### ✅ O que são **arrays com objetos**?

Em Java, você pode criar **arrays que armazenam objetos** em vez de tipos primitivos. Isso é útil para trabalhar com **coleções de instâncias** de uma classe.

---

### 📘 Exemplo simples:

Imagine uma classe `Produto`:

```
public class Produto {
    String nome;
    double preco;

    Produto(String nome, double preco) {
        this.nome = nome;
        this.preco = preco;
    }

    void exibir() {
        System.out.println(nome + " - R$ " + preco);
    }
}

```

Agora, vamos criar um array com **vários objetos `Produto`**:

```
public class Loja {
    public static void main(String[] args) {
        // Criando um array de objetos Produto
        Produto[] produtos = new Produto[3];

        // Instanciando objetos e colocando no array
        produtos[0] = new Produto("Café", 9.99);
        produtos[1] = new Produto("Leite", 4.50);
        produtos[2] = new Produto("Pão", 2.30);

        // Percorrendo o array
        for (Produto p : produtos) {
            p.exibir();
        }
    }
}

```

**Saída:**

```
Café - R$ 9.99  
Leite - R$ 4.5  
Pão - R$ 2.3  

```

---

### 🧠 Para que serve?

- Organizar vários objetos do mesmo tipo
    
- Passar múltiplos objetos para métodos
    
- Armazenar listas fixas (para listas variáveis, use `ArrayList`)
    

---

### 📌 Dicas:

- Arrays têm tamanho fixo. Use `ArrayList` para tamanhos dinâmicos.
    
- Sempre inicialize os objetos **antes de usar**, senão ocorre `NullPointerException`.
    

---

### 💡 Exemplo com método que recebe array:

```
public static void listarProdutos(Produto[] produtos) {
    for (Produto p : produtos) {
        p.exibir();
    }
}

```