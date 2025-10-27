```
using System;
using System.Collections.Generic;

public class Program
{
    public static void Main()
    {
 		var lista = new List<string> { "agnar", "diero", "mikaela", "yorik", "norax", "astro", "sean"};
		
		for(int index = 0; index < lista.Count; index ++ )
		{
			Console.WriteLine(lista[index]);
		}
	}
}
```