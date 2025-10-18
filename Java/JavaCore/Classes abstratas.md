### 🧩 O que é uma Classe Abstrata?

Uma **classe abstrata** é uma **classe base incompleta** que **não pode ser instanciada diretamente**. Ela é usada como um **molde** para outras classes, permitindo:

- **definir métodos com ou sem corpo** (concretos ou abstratos)
    
- **forçar subclasses a implementar certos comportamentos**
    
- **compartilhar código comum entre várias classes filhas**
    

---

### ✅ Regras sobre Classe Abstrata em Java:

1. Use `abstract` na declaração da classe:
    
    `abstract class Animal { ... }`
    
2. Uma classe abstrata **pode ter métodos normais** com corpo (implementação) e também **métodos abstratos** (sem corpo):
    
    `abstract void emitirSom(); // método abstrato`
    
3. Se uma classe herda uma classe abstrata, ela **deve sobrescrever todos os métodos abstratos** ou também ser abstrata.
    
4. **Não é possível criar objetos diretamente** de uma classe abstrata:
    
    `Animal a = new Animal(); // ❌ Erro`
    
5. Uma classe abstrata **pode estender outra classe abstrata.**
    

---

### 📦 Exemplo básico:

```
abstract class Animal {
    abstract void emitirSom(); // método obrigatório nas subclasses

    void respirar() {
        System.out.println("Respirando...");
    }
}

class Cachorro extends Animal {
    @Override
    void emitirSom() {
        System.out.println("O cachorro late");
    }
}

```



```
**public class Main {
    public static void main(String[] args) {
        // Animal a = new Animal(); // ❌ Erro
        Animal c = new Cachorro();
        c.emitirSom(); // O cachorro late
        c.respirar();  // Respirando...
    }
}
**
```


---

### 🧠 Dica importante:

Use classes abstratas quando:

- Você quer **fornecer um padrão de estrutura**, mas com liberdade para subclasses decidirem detalhes;
    
- Precisa de **métodos compartilhados + métodos obrigatórios** nas filhas.