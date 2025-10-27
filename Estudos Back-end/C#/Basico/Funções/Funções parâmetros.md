```
using System;
using System.Collections.Generic;

namespace EstudosC
{
    // Definindo uma classe que realizará operações matemáticas simples
    public class OperacoesMatematicas
    {
        // Método para adicionar dois números
        public void Adicionar(int numero1, int numero2)
        {
            // Calcula a soma dos dois números passados como argumento
            var resultado = numero1 + numero2;
            // Exibe o resultado no console
            Console.WriteLine("Resultado da soma: " + resultado);
        }
        
        // Método para subtrair dois números
        public void Subtracao(int numero1, int numero2)
        {
            // Calcula a subtração dos dois números passados como argumento
            var resultado = numero2 - numero1;
            // Exibe o resultado no console
            Console.WriteLine("Resultado da subtração: " + resultado);
        }
    }

    // Classe principal que vai executar o programa
    class Program
    {
        static void Main(string[] args)
        {
            // Criando uma instância da classe OperacoesMatematicas
            var matematica = new OperacoesMatematicas();
            // Chamando o método Adicionar para somar 1 e 7
            matematica.Adicionar(numero1: 1, numero2: 7);
            
            // Criando outra instância da classe OperacoesMatematicas
            var matematica2 = new OperacoesMatematicas();
            // Chamando o método Subtracao para subtrair 1 de 7
            matematica2.Subtracao(numero1: 1, numero2: 7);
        }
    }
}

```

### 📍 **Conclusões e Observações:**

- **Reusabilidade**: A classe `OperacoesMatematicas` pode ser reutilizada sempre que precisarmos realizar operações matemáticas, como soma e subtração, em diferentes partes do código.
    
- **Uso de Instâncias**: Usamos duas instâncias da classe para realizar as operações. Isso ajuda a manter o código organizado e permite realizar diferentes operações independentemente.
    
- **Métodos Simples**: Os métodos são simples e objetivos, demonstrando como passar parâmetros para um método e como exibir resultados.