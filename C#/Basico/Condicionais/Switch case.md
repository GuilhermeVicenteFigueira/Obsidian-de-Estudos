
```
using System;
using System.Collections.Generic;

public class Program
{
    public static void Main()
    {
        /*string player = "diero";   

        switch (player)
        {
            case "diero":
                Console.WriteLine("pai");
                break;

            case "mikaela":
                Console.WriteLine("não adotou");
                break;

            case "agnar":
                Console.WriteLine("broxa");
                break;

            default:
                Console.WriteLine("o norax não merece passar os genes de merda para frente.");
                break;*/
		
		int numero = 0;
		string resultado =  numero switch
		{
			7=> "vicetne",
			1=> "penis",
			_ => "desconhecido"
		};
			Console.WriteLine(resultado);
        }
    }
```
