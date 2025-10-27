```
using System;

namespace EstudosC
{
    class Program
    {
        static void Main(string[] args)
        {
            // int é um tipo de valor (value type) e por padrão NÃO aceita null
            int numero = 10;
            // numero = null; // ❌ erro: int não aceita null diretamente

            // Mas podemos usar "nullable" com ?
            int? idade = null; // Agora pode ser null

            // Verificando se tem valor com HasValue
            if (idade.HasValue)
            {
                // Pegando o valor com .Value
                Console.WriteLine("Idade tem valor: " + idade.Value);
            }
            else
            {
                Console.WriteLine("Idade está nula.");
            }

            // Atribuindo um valor depois
            idade = 25;

            if (idade.HasValue)
            {
                Console.WriteLine("Idade agora tem valor: " + idade.Value);
            }

            // Podemos também usar o operador null-coalescing (??)
            int resultado = idade ?? 0; // Se idade for null, usa 0
            Console.WriteLine("Resultado com ?? : " + resultado);

            // Outros tipos também funcionam como nullable
            bool? ativo = null;

            if (ativo.HasValue)
            {
                Console.WriteLine("Está ativo? " + ativo.Value);
            }
            else
            {
                Console.WriteLine("Ativo está nulo.");
            }
        }
    }
}

```

### 🧠 Resumo:

| Conceito        | Explicação                                                   |
| --------------- | ------------------------------------------------------------ |
| `int`, `bool`   | Tipos **de valor**, não aceitam `null` por padrão            |
| `int?`, `bool?` | Versão **nullable** dos tipos de valor                       |
| `.HasValue`     | Retorna `true` se a variável **tem valor**                   |
| `.Value`        | Acessa o valor real da variável (só se `HasValue` for true!) |
| `??`            | Operador para fornecer valor padrão se for `null`            |