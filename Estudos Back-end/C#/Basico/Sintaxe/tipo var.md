```
using System.Globalization;  
using System.Text;  
  
namespace EstudosC;  
  
class Program  
{  
  
    static void Main(string[] args)  
    {       
	   string nome = "Guilherme";  
       int meuNumero = 15;  
       var nome2 = "Guilherme";  
       string meuSobrenome ;  
       var variavel  = "vicente";  
       var variavel2 = DateTime.Now;  
    }}
```

### ✅ **Vantagens de usar `var` em C#**

|Vantagem|Explicação|
|---|---|
|✅ **Código mais limpo**|Evita repetições desnecessárias. Ex: `Dictionary<string, List<int>>` vira só `var`.|
|✅ **Menos digitação**|O compilador deduz o tipo, então você escreve menos.|
|✅ **Facilita com tipos longos**|Útil com tipos genéricos ou anônimos, tipo: `var pessoa = new { Nome = "Vicente", Idade = 20 };`|
|✅ **Boa com LINQ**|Com LINQ, os tipos retornados são complexos, e `var` é quase necessário.|
|✅ **Evita redundância**|Já que o compilador sabe o tipo, repetir ele pode ser desnecessário.|

---

### ⚠️ **Mas atenção...**

| Cuidados ao usar `var`                     | Por que?                                                                        |
| ------------------------------------------ | ------------------------------------------------------------------------------- |
| ❌ **Não usar quando o tipo não for óbvio** | Pode deixar o código confuso. Ex: `var x = MetodoQualquer();` — que tipo é `x`? |
| ❌ **Não ajuda muito em leitura futura**    | Às vezes, olhar e entender o tipo é mais difícil sem o nome explícito.          |