### 🔁 O que é Sobrescrita (Override)?

A **sobrescrita** ocorre quando **uma classe filha** (subclasse) **redefine** um **método herdado da classe pai** com uma **implementação diferente**, mantendo:

- **o mesmo nome do método**
    
- **os mesmos parâmetros**
    
- **o mesmo tipo de retorno (ou compatível)**
    

Isso permite **personalizar ou alterar o comportamento herdado**.

---

### ✅ Regras para sobrescrita em Java:

1. O método na superclasse **deve ser `public` ou `protected`** (não pode ser `private`, pois não é herdado).
    
2. O método sobrescrito **deve ter a mesma assinatura** (nome e parâmetros).
    
3. Use a anotação `@Override` para deixar claro que está sobrescrevendo (não é obrigatório, mas é recomendado).
    
4. O método sobrescrito **não pode ter uma visibilidade mais restrita** (ex: não pode rebaixar de `public` para `protected`).

```
class Animal {
    public void fazerSom() {
        System.out.println("O animal faz um som");
    }
}

class Gato extends Animal {
    @Override
    public void fazerSom() {
        System.out.println("O gato mia");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal a = new Animal();
        a.fazerSom(); // "O animal faz um som"

        Gato g = new Gato();
        g.fazerSom(); // "O gato mia" - sobrescrita do método da classe Animal
    }
}
```

## 🧠 Dica importante:
Se você quiser chamar o método da classe pai mesmo após sobrescrever, use super:

```
class Gato extends Animal {
    @Override
    public void fazerSom() {
        super.fazerSom(); // Chama o método da classe pai
        System.out.println("Mas o gato também mia");
    }
}
```