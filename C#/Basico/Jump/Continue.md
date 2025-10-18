```
using System;
					
public class Program
{
	public static void Main()
	{
		var numero = 0;
		while (numero < 10)
		{
			numero++;
			if (numero == 5)
			{
				continue;
			}
			Console.WriteLine(numero);
		}
		Console.WriteLine("aqui");
		
	}
}
```