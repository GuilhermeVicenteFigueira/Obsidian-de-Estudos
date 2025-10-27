```
using System.Globalization;  
using System.Text;  
  
namespace EstudosC;  
  
class Program  
{  
  
    static void Main(string[] args)  
    {  
        int[,,,] inteiros = new int[10, 10, 10, 10];  
                inteiros[0, 0, 0, 0] = 1;  
        inteiros[0, 0, 0, 1] = 2;  
        inteiros[0, 0, 1, 2] = 3;  
        inteiros[0, 1, 2, 3] = 4;  
        inteiros[1, 2, 3, 4] = 5;  
        Console.WriteLine(inteiros[0, 0, 0, 0]);  
        Console.WriteLine(inteiros[0, 0, 0, 1]);  
        Console.WriteLine(inteiros[0, 0, 1, 2]);  
        Console.WriteLine(inteiros[0, 1, 2, 3]);  
        Console.WriteLine(inteiros[1, 2, 3, 4]);  
  
  
        int[] inteiro = [1, 10, 7];  
        Console.WriteLine(inteiro[0]);  
        Console.WriteLine(inteiro[1]);  
        Console.WriteLine(inteiro[2]);  
        Console.WriteLine(inteiro.Length);  
  
        int[] inteiross = new int[10];  
        inteiross[0] = 1;  
        inteiross[1] = 2;  
        inteiross[2] = 3;  
        inteiross[3] = 4;  
        Console.WriteLine(inteiross.Length);  
        Console.WriteLine(inteiross[0]);  
        Console.WriteLine(inteiross[1]);  
        Console.WriteLine(inteiross[2]);  
        Console.WriteLine(inteiross[3]);  
  
    }}
```