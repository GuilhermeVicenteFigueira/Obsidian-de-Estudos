```
using System;

namespace EstudosC
{
    class Program
    {
        static void Main(string[] args)
        {
            // Variáveis com tipo específico
            int idade = 25;
            string nome = "Vicente";
            bool ativo = true;

            // Variáveis do tipo object
            object valor1 = idade;   // int vira object
            object valor2 = nome;    // string vira object
            object valor3 = ativo;   // bool vira object

            Console.WriteLine("Valores armazenados em 'object':");
            Console.WriteLine(valor1); // 25
            Console.WriteLine(valor2); // Vicente
            Console.WriteLine(valor3); // True

            // Podemos armazenar qualquer tipo
            object qualquerCoisa = DateTime.Now;
            Console.WriteLine(qualquerCoisa);

            // A desvantagem: você precisa converter de volta se quiser usar como tipo original
            int idadeDeNovo = (int)valor1; // "unboxing" do object para int
            Console.WriteLine("Idade reconvertida: " + idadeDeNovo);
        }
    }
}

```

### ⚠️ Cuidados com `object`

- Requer **conversão (cast)** para voltar ao tipo original → pode dar erro se for errado.
    
- Evite usar `object` se você **sabe o tipo real** da variável.
    
- **`dynamic`** pode ser uma alternativa moderna ao `object`, com menos casting (se quiser te explico a diferença depois).