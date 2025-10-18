```
using System;
using System.Collections.Generic;

namespace EstudosC
{
    class Program
    {
        static void Main(string[] args)
        {
            // Criando um dicionário que relaciona um número inteiro com um texto (string)
            Dictionary<int, string> dic = new Dictionary<int, string>();

            // Adicionando pares chave-valor no dicionário
            dic.Add(0, "Guilherme");   // chave 0 com valor "Guilherme"
            dic.Add(1, "Emanuelly");   // chave 1 com valor "Emanuelly"
            dic.Add(7, "Forconi");     // chave 7 com valor "Forconi"

            // A linha abaixo geraria erro se fosse descomentada, 
            // pois já existe a chave 0 no dicionário:
            // dic.Add(0, "Garage");

            // Pegando o valor da chave 1
            string value = dic[1]; // value será "Emanuelly"

            // Mostrando o valor no console
            Console.WriteLine(value); // Saída: Emanuelly
        }
    }
}

```

