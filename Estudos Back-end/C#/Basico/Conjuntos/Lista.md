```
using System;
using System.Collections.Generic;
using System.Linq;

namespace EstudosC
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> numeros = new List<int>();

            numeros.Add(10);           // Lista: [10]
            numeros.Add(20);           // Lista: [10, 20]
            numeros.Add(30);           // Lista: [10, 20, 30]

            Console.WriteLine(numeros[0]);       // 10
            Console.WriteLine(numeros[1]);       // 20
            Console.WriteLine(numeros[2]);       // 30

            Console.WriteLine(numeros.First());  // 10
            Console.WriteLine(numeros.Last());   // 30
            Console.WriteLine(numeros.ElementAt(1)); // 20

            numeros.Remove(20);      // Remove o valor 20 → [10, 30]
            Console.WriteLine(numeros[0]);       // 10
            Console.WriteLine(numeros[1]);       // 30

            numeros.RemoveAt(0);     // Remove o valor na posição 0 → [30]
            Console.WriteLine(numeros[0]);       // 30

            numeros.Clear();         // Limpa a lista → []

            Console.WriteLine(numeros.Count);    // 0
        }
    }
}

```
```
using System;
using System.Collections.Generic;

namespace EstudosC
{
    class Program
    {
        static void Main(string[] args)
        {
            // Criando uma lista de strings e adicionando elementos (nomes de lojas ou plataformas)
            List<string> strings = new List<string>();
            strings.Add("Pichau");
            strings.Add("Kabum");
            strings.Add("Marcado livre");
            strings.Add("Facebook");

            // Transformando a lista em uma única string separada por vírgulas
            string result = string.Join(",", strings);

            // Criando uma lista de inteiros
            List<int> ints = new List<int>();
            ints.Add(42);

            // Criando uma lista de números decimais (com M para indicar tipo decimal)
            List<decimal> decimals = new List<decimal>();
            decimals.Add(123.45M);

            // Criando uma lista de datas e adicionando a data atual
            List<DateTime> dates = new List<DateTime>();
            dates.Add(DateTime.Now);

            // Lista de booleanos (verdadeiro/falso)
            List<bool> bools = new List<bool>();
            bools.Add(true);

            // Lista de números do tipo double
            List<double> doubles = new List<double>();
            doubles.Add(123.45);

            // Lista de números do tipo float (com f para indicar float)
            List<float> floats = new List<float>();
            floats.Add(123.45f);

            // Lista de inteiros curtos (short)
            List<short> shorts = new List<short>();
            shorts.Add(123);

            // Lista de inteiros curtos sem sinal (ushort)
            List<ushort> ushorts = new List<ushort>();
            ushorts.Add(123);

            // Lista de inteiros pequenos com sinal (sbyte vai de -128 a 127)
            List<sbyte> sbytes = new List<sbyte>();
            sbytes.Add(100);

            // Lista de inteiros pequenos sem sinal (byte vai de 0 a 255)
            List<byte> bytes = new List<byte>();
            bytes.Add(200);

            // Lista de inteiros que podem aceitar valores nulos
            List<Nullable<int>> nullableInts = new List<Nullable<int>>();
            nullableInts.Add(123);

            // Lista de caracteres
            List<char> chars = new List<char>();
            chars.Add('a');

            // Lista de objetos (pode conter qualquer tipo de dado)
            List<object> objects = new List<object>();
            objects.Add("ola");    // string
            objects.Add(123);      // inteiro
            objects.Add(true);     // booleano
            objects.Add(false);    // booleano
            objects.Add(null);     // valor nulo

            // Exibindo o primeiro item de cada lista
            Console.WriteLine(strings[0]);       // Pichau
            Console.WriteLine(ints[0]);          // 42
            Console.WriteLine(decimals[0]);      // 123.45
            Console.WriteLine(dates[0]);         // Data e hora atual
            Console.WriteLine(bools[0]);         // True
            Console.WriteLine(doubles[0]);       // 123.45
            Console.WriteLine(floats[0]);        // 123.45
            Console.WriteLine(shorts[0]);        // 123
            Console.WriteLine(ushorts[0]);       // 123
            Console.WriteLine(sbytes[0]);        // 100
            Console.WriteLine(bytes[0]);         // 200
            Console.WriteLine(nullableInts[0]);  // 123
            Console.WriteLine(chars[0]);         // a
            Console.WriteLine(objects[0]);       // ola

            // Mostra quantos elementos tem na lista de objetos
            Console.WriteLine(objects.Count);    // 5

            // Mostra a string com os nomes separados por vírgula
            Console.WriteLine(result);           // Pichau,Kabum,Marcado livre,Facebook
        }
    }
}

```
### O que você aprende com esse código:

- A usar `List<T>` com tipos diferentes.
    
- A adicionar elementos com `.Add()`.
    
- A acessar valores com `lista[indice]`.
    
- A transformar uma lista de strings em uma única string (`string.Join()`).
    
- A contar elementos com `.Count`.