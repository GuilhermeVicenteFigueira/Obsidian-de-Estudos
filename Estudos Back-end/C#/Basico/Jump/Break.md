```
using System;
					
public class Program
{
	public static void Main()
	{
		var numero = 0;
		while (numero < 100)
		{
			if (numero == 10)
			{
				break;
			}
			
			Console.WriteLine(numero);
			
			numero++;
		}
		
		Console.WriteLine("aqui");
		
	}
}
```