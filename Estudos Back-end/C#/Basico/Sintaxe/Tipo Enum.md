
```
namespace EstudosC;

class Program
{
    enum NivelDeDificuldade
    {
        Baixo = 0,
        Medio = 1,
        Alto = 2,
    }
    static void Main(string[] args)
    {
        NivelDeDificuldade nivel = NivelDeDificuldade.Alto;

        int nivelInteiro = (int)nivel;
        
        Console.WriteLine(nivelInteiro);
        Console.WriteLine(nivel);
    }
}

```

### 🎯 Vantagens de usar `enum`:

|Vantagem|Explicação|
|---|---|
|✅ Clareza|Fica claro o que aquele valor representa (ex: `Alto`, `Medio`, `Baixo`).|
|✅ Sem erros de digitação|Diferente de usar strings (`"Baixo"`), que são mais fáceis de errar.|
|✅ Validação automática|Só é possível usar os valores definidos no `enum`.|
|✅ Mais fácil de manter|Se mudar os nomes no `enum`, muda tudo onde ele for usado.|
|✅ Pode converter pra número ou texto|