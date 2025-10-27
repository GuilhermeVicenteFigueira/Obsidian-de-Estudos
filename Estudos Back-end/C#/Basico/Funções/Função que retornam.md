```
using System;
using System.Collections.Generic;

namespace EstudosC
{
    // Classe que contém métodos de operações matemáticas
    public class OperacoesMatematicas
    {
        // Função que retorna uma tupla com dois valores:
        // o resultado da adição e o nome de quem executou
        public (int resultadoDaAdicao, string atorDaFuncao) Adicionar(int numero1, int numero2)
        {
            var resultado = numero1 + numero2;
            return (resultado, "gui"); // retorna uma tupla (int, string)
        }

        // Função que retorna apenas o resultado da subtração
        public int Subtrair(int numero1, int numero2)
        {
            return numero1 - numero2;
        }

        // Função que multiplica dois números e retorna o resultado
        public int Multiplicar(int numero1, int numero2)
        {
            return numero1 * numero2;
        }

        // Função que divide dois números e retorna um double
        public double Dividir(int numero1, int numero2)
        {
            // Tratamento para evitar divisão por zero
            if (numero2 == 0)
            {
                Console.WriteLine("Não é possível dividir por zero.");
                return 0;
            }

            return (double)numero1 / numero2;
        }

        // Função expressa com => (lambda expression), apenas exibe no console
        public void MostrarSoma(int numero1, int numero2) => 
            Console.WriteLine($"Soma rápida: {numero1 + numero2}");
    }

    // Classe principal com o ponto de entrada do programa
    class Program
    {
        static void Main(string[] args)
        {
            var matematica = new OperacoesMatematicas();

            // Exemplo com tupla: retorna dois valores
            (int resultado, string nome) = matematica.Adicionar(1, 7);
            Console.WriteLine($"Resultado da adição: {resultado}");
            Console.WriteLine($"Feito por: {nome}");

            // Exemplo de subtração
            int subtracao = matematica.Subtrair(10, 3);
            Console.WriteLine($"Resultado da subtração: {subtracao}");

            // Exemplo de multiplicação
            int multiplicacao = matematica.Multiplicar(4, 5);
            Console.WriteLine($"Resultado da multiplicação: {multiplicacao}");

            // Exemplo de divisão
            double divisao = matematica.Dividir(10, 2);
            Console.WriteLine($"Resultado da divisão: {divisao}");

            // Exemplo com lambda expression
            matematica.MostrarSoma(2, 3);
        }
    }
}

```