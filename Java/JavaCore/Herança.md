**Herança** é um dos pilares da **Programação Orientada a Objetos (POO)**. Ela permite que uma **classe filha (ou subclasse)** **herde** atributos e métodos de uma **classe pai (ou superclasse)**. Isso promove **reutilização de código** e facilita a **extensão de funcionalidades**.

### Correção e detalhes:

- **Métodos públicos** e **protegidos (protected)** são herdados pela classe filha.
    
- **Métodos privados** **não são herdados** diretamente; eles pertencem apenas à classe pai.
    
- A classe filha pode:
    
    - **Usar** os métodos herdados.
        
    - **Sobrescrever (@override)** os métodos da classe pai, para adaptar seu comportamento.
        
    - **Adicionar** seus próprios métodos e atributos.
        

---

### Exemplo:

```
// Superclasse
public class Animal {
    public void fazerSom() {
        System.out.println("O animal faz um som");
    }

    private void respirar() {
        System.out.println("Respirando...");
    }

    protected void dormir() {
        System.out.println("Animal dormindo");
    }
}

// Subclasse
public class Cachorro extends Animal {
    @Override
    public void fazerSom() {
        System.out.println("O cachorro late");
    }

    public void correr() {
        System.out.println("O cachorro está correndo");
    }
}

// Classe principal
public class Main {
    public static void main(String[] args) {
        Cachorro dog = new Cachorro();
        dog.fazerSom();    // "O cachorro late" (sobrescrito)
        dog.dormir();      // "Animal dormindo" (herdado)
        dog.correr();      // "O cachorro está correndo" (definido na subclasse)

        // dog.respirar(); // Erro: método é privado na superclasse
    }
}

```

