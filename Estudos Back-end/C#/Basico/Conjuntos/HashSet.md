```
using System;
using System.Collections.Generic;

namespace EstudosC
{
    class Program
    {
        static void Main(string[] args)
        {
            // Criando um HashSet para armazenar números inteiros
            HashSet<int> sets = new HashSet<int>();

            // Adicionando elementos ao HashSet
            sets.Add(1);  // Adiciona o número 1
            sets.Add(2);  // Adiciona o número 2
            sets.Add(3);  // Adiciona o número 3
            sets.Add(3);  // Tenta adicionar o número 3 novamente, mas HashSet ignora duplicatas

            // Exibe o número de elementos no HashSet (não vai contar duplicados)
            Console.WriteLine(sets.Count);  // Saída: 3
        }
    }
}

```

### 📚 **Explicação:**

- **`HashSet<T>`** é uma coleção que **não permite elementos duplicados**. Ou seja, se você tentar adicionar um valor que já existe, ele será ignorado.
    
    - No código acima, o número `3` é adicionado duas vezes, mas no final, o `HashSet` vai **ignorar o segundo valor duplicado**, porque o valor `3` já está presente.
        
- **`sets.Add(valor)`**: adiciona um elemento ao `HashSet`. Quando você tenta adicionar um número que já existe na coleção, o `HashSet` **não permite duplicados**.
    
- **`sets.Count`**: mostra a quantidade de elementos únicos no `HashSet`.
    

### ⚠️ **Resultado:**

Mesmo com a tentativa de adicionar `3` duas vezes, o `HashSet` só vai contar uma vez, e o **resultado da execução será 3**, pois os elementos únicos são `{1, 2, 3}`.

---

### ✨ **Pontos Importantes sobre `HashSet`:**

1. **Não aceita duplicatas**: Como mostrado no exemplo, duplicados são automaticamente ignorados.
    
2. **Ordem não garantida**: A ordem em que os elementos são adicionados não é garantida no `HashSet`. Se precisar de uma ordem específica, considere usar uma lista (`List<T>`).
    
3. **Desempenho rápido**: A inserção e busca de elementos em um `HashSet` são rápidas, pois ele usa um mecanismo baseado em tabela de hash.
    

Se tiver mais dúvidas ou quiser ver mais exemplos de `HashSet`, estou à disposição!