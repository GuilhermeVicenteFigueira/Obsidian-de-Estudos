O que é Coesão em POO?
Coesão (ou coerência) é uma medida de quanto as partes internas de uma classe estão relacionadas entre si e com o propósito da classe.

Em outras palavras: uma classe coesa faz só uma coisa — e faz bem feito.

### 🧱 Exemplo de boa coesão
Uma classe chamada Relogio:

```
public class Relogio {
    private int horas;
    private int minutos;

    public void ajustarHora(int h, int m) { ... }
    public void mostrarHora() { ... }
}
```

Tudo aqui tem a ver com o funcionamento de um relógio. Alta coesão.

### ❌ Exemplo de má coesão
Imagine uma classe chamada Utilitarios que mistura funções aleatórias:

```
public class Utilitarios {
    public void calcularIdade() { ... }
    public void enviarEmail() { ... }
    public void salvarArquivo() { ... }
}
```

Essa classe faz várias coisas não relacionadas entre si. Isso é baixa coesão.

### 🧠 Por que a coesão é importante?
Facilita a manutenção: código mais organizado e fácil de entender.

Evita efeitos colaterais: menos chances de um método afetar algo que não deveria.

Facilita testes: mais simples testar unidades específicas.

Ajuda no reuso: classes com um único propósito podem ser reaproveitadas com mais segurança.

### ✅ Boa prática: "Uma classe = uma responsabilidade"
Esse princípio é chamado de SRP (Single Responsibility Principle), e está ligado diretamente à ideia de alta coesão.

