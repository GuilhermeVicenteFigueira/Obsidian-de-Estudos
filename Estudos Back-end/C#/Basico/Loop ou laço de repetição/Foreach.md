```
using System;
using System.Collections.Generic;

public class Program
{
    public static void Main()
    {
 		var lista = new List<string> { "agnar", "diero", "mikaela", "yorik", "norax", "astro", "sean"};
		var dicionario = new Dictionary<string, string>();
		
		dicionario.Add("player1","diero");
		dicionario.Add("player2","Agnar");
		dicionario.Add("player3","Mikaela");
		dicionario.Add("player4","Yorik");
		dicionario.Add("player5","Norax");
		
		foreach (var nomes in dicionario)
		{
			Console.WriteLine(nomes.Key);
			Console.WriteLine(nomes.Value);
			Console.WriteLine("--------------------------------------------");
		}
	}
}
```