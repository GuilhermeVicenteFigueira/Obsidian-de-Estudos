## 1. Associação **Unidirecional Um-para-Muitos**

> Uma classe **conhece várias instâncias** de outra, mas o contrário **não acontece**.

### 📘 Exemplo: `Escola` conhece vários `Alunos`, mas o `Aluno` **não conhece a Escola**.

```
public class Aluno {
    private String nome;

    public Aluno(String nome) {
        this.nome = nome;
    }
}

```

```
import java.util.List;

public class Escola {
    private String nome;
    private List<Aluno> alunos;

    public Escola(String nome, List<Aluno> alunos) {
        this.nome = nome;
        this.alunos = alunos;
    }
}

```

✔ A navegação só é possível de `Escola → Alunos`.

---

## 🔹 2. Associação **Unidirecional Muitos-para-Um**

> Muitas instâncias de uma classe conhecem **uma única instância de outra**, mas o contrário **não ocorre**.

### 📘 Exemplo: Vários `Aluno` conhecem um `Professor`, mas o `Professor` não conhece os alunos.

```
public class Professor {
    private String nome;

    public Professor(String nome) {
        this.nome = nome;
    }
}

```

```
public class Aluno {
    private String nome;
    private Professor professor; // Muitos alunos para um professor

    public Aluno(String nome, Professor professor) {
        this.nome = nome;
        this.professor = professor;
    }
}

```

✔ Navegação de `Aluno → Professor`, mas o professor **não tem lista de alunos**.

---

## 🔁 3. Associação **Bidirecional**

> Ambas as classes **se conhecem**. A navegação é possível nos **dois sentidos**.

### 📘 Exemplo: `Curso` conhece vários `Alunos`, e `Aluno` conhece seu `Curso`.

```
import java.util.List;

public class Curso {
    private String nome;
    private List<Aluno> alunos;

    public Curso(String nome, List<Aluno> alunos) {
        this.nome = nome;
        this.alunos = alunos;
    }
}

```

```
public class Aluno {
    private String nome;
    private Curso curso;

    public Aluno(String nome, Curso curso) {
        this.nome = nome;
        this.curso = curso;
    }
}

```

✔ Agora tanto `Curso` conhece os `Alunos`, quanto cada `Aluno` conhece seu `Curso`.

---

## 🧠 Resumo:

|Tipo|Classe A conhece B?|Classe B conhece A?|
|---|---|---|
|Unidirecional 1 → muitos|✅|❌|
|Unidirecional muitos → 1|✅|❌|
|Bidirecional|✅|✅|