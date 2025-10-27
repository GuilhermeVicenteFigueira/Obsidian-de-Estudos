
```
using System;

class Program
{
    static void Main()
    {
        // CHAR: representa um único caractere
        char letra = 'V';
        Console.WriteLine("Letra: " + letra);

        // STRING: representa uma sequência de caracteres
        string nome = "  Vicente  ";
        Console.WriteLine("Nome original: '" + nome + "'");

        // TRIM: remove espaços no início e fim
        string nomeLimpo = nome.Trim();
        Console.WriteLine("Nome com Trim: '" + nomeLimpo + "'");

        // EQUALS: verifica se duas strings são iguais
        string entrada = "vicente";
        bool nomesIguais = nomeLimpo.Equals(entrada, StringComparison.OrdinalIgnoreCase);
        Console.WriteLine("Nomes iguais (ignorando maiúsculas/minúsculas)? " + nomesIguais);

        // CONTAINS: verifica se contém um pedaço de texto
        string frase = "Olá, meu nome é Vicente!";
        bool contemNome = frase.Contains("Vicente");
        Console.WriteLine("A frase contém 'Vicente'? " + contemNome);

        // STARTSWITH: verifica se começa com algo
        bool comecaComOla = frase.StartsWith("Olá");
        Console.WriteLine("Frase começa com 'Olá'? " + comecaComOla);

        // ENDSWITH: verifica se termina com algo
        bool terminaComExclamacao = frase.EndsWith("!");
        Console.WriteLine("Frase termina com '!'? " + terminaComExclamacao);

        // REPLACE: substitui partes do texto
        string novaFrase = frase.Replace("Vicente", "Guilherme");
        Console.WriteLine("Frase modificada: " + novaFrase);
    }
}

```

```
using System;
using System.Text;

class Program
{
    static void Main()
    {
        // Simples concatenação de strings
        string text1 = "abcd";
        string text2 = "efgh";
        string paragrafo = text1 + " " + 7 + " " + true + " " + text2;
        Console.WriteLine("Parágrafo (concatenação): " + paragrafo);

        // Verbatim string (aceita barra invertida sem precisar escapar)
        string caminho = @"C:\teste\outrapast\mechupa\aizedamanga";
        Console.WriteLine("Caminho: " + caminho);

        // Interpolação de string usando $
        string paragrafo2 = $"A primeira frase é: {text1} {text2} {7} {true} {text2}";
        Console.WriteLine("Parágrafo 2 (interpolação): " + paragrafo2);

        // StringBuilder é mais performático para juntar muitas strings
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.Append(paragrafo);
        stringBuilder.Append("\n"); // Quebra de linha
        stringBuilder.Append(paragrafo2);

        string resultado = stringBuilder.ToString();
        Console.WriteLine("Resultado do StringBuilder:\n" + resultado);

        // String.Format substitui placeholders {0}, {1}, etc.
        string texto = "O usuário {0} gosta do número {1}";
        string formatado = string.Format(texto, "Vicente", 15);
        Console.WriteLine("Formatado com string.Format: " + formatado);
    }
}

```