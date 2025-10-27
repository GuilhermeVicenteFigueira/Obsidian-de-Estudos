### **Classe**

> É o **molde** ou **modelo** que define como os objetos serão. Dentro dela ficam os **atributos** (características) e os **métodos** (ações que o objeto pode fazer).

**Exemplo em Java:**

```
public class Pessoa {
    String nome;
    void falar() {
        System.out.println("Olá!");
    }
}
```

### 🔹 **Método**

> É uma **função dentro da classe** que define um comportamento ou ação que o objeto pode realizar. Pode ou não retornar um valor.

**Exemplo:**

```
void falar() {
    System.out.println("Oi");
}
```
### 🔹 **Instância**

> É o **ato de criar um objeto** a partir de uma classe usando a palavra-chave `new`. Quando você instancia uma classe, está criando uma "versão real" dela na memória.

**Exemplo:**
```
Pessoa p1 = new Pessoa(); // instanciando a classe Pessoa
```
### 🔹 **Objeto**

> É a **cópia real da classe**, com seus próprios valores. Um objeto pode acessar os métodos e atributos definidos na classe.

**Exemplo:**

```
Pessoa p1 = new Pessoa();
p1.nome = "Vicente";
p1.falar();

```

### 🔹 **Atributo**

> É uma **variável declarada dentro da classe**, que representa uma **característica** do objeto.

**Exemplo:**
```
String nome;
int idade;
```