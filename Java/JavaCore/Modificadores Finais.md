
O modificador `final` em Java é utilizado para **impedir alterações**. Ele pode ser aplicado a **variáveis**, **métodos** e **classes**, e tem significados diferentes dependendo de onde for usado:

---

### 📌 1. `final` em variáveis

Quando usado em variáveis, significa que **o valor não pode ser alterado** após ser atribuído.

```
public class Exemplo {
    public static final int VELOCIDADE_MAXIMA = 120;

    public static void main(String[] args) {
        // VELOCIDADE_MAXIMA = 100; // ERRO: não pode ser reatribuída
        System.out.println(VELOCIDADE_MAXIMA);
    }
}

```

🟡 **Boas práticas:**

- Variáveis `final` e `static` geralmente são **constantes globais**.
    
- O nome delas segue a convenção: **letras maiúsculas com underlines** (`SNAKE_CASE`), ex: `PI`, `TAXA_JUROS`, `MAX_USERS`.
    

---

### 📌 2. `final` em métodos

Um método `final` **não pode ser sobrescrito** por subclasses.

```
class Animal {
    public final void respirar() {
        System.out.println("Animal respirando...");
    }
}

class Cachorro extends Animal {
    // public void respirar() {} // ERRO: método não pode ser sobrescrito
}

```
---

### 📌 3. `final` em classes

Uma classe `final` **não pode ser estendida** (herdada).
```
public final class Util {
    public static void imprimir(String texto) {
        System.out.println(texto);
    }
}

// class MinhaUtil extends Util {} // ERRO: classe final não pode ser estendida
```


---

## 🧩 `final`, `static` e constantes

- `final`: valor não muda
    
- `static`: pertence à classe, e não à instância
    
- Juntos (`static final`): criam uma **constante global**.

```
public class Configuracoes {
    public static final double PI = 3.14159;
    public static final String VERSAO = "1.0.0";
}

```


---

## 👑 Padrão de Projeto: **Singleton**

Você mencionou corretamente: o **Singleton** é um **padrão criacional** que garante que **uma classe tenha apenas uma instância** no sistema, e fornece **um ponto global de acesso a ela**.

---

### 🛠️ Exemplo de Singleton em Java:

```
public final class ConexaoBanco {
    private static ConexaoBanco instancia;

    // Construtor privado impede instância externa
    private ConexaoBanco() {}

    // Método público e estático de acesso à instância única
    public static ConexaoBanco getInstancia() {
        if (instancia == null) {
            instancia = new ConexaoBanco();
        }
        return instancia;
    }

    public void conectar() {
        System.out.println("Conectado ao banco de dados!");
    }
}

```


### 🧪 Uso:

```
public class Main {
    public static void main(String[] args) {
        ConexaoBanco conexao = ConexaoBanco.getInstancia();
        conexao.conectar();
    }
}

```


---

### 🧠 Dica:

- O `final` na classe impede que o Singleton seja estendido.
    
- O construtor privado impede múltiplas instâncias.
    
- A instância única é armazenada em uma variável `static`.