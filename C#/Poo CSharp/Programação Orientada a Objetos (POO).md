A Programação Orientada a Objetos é um paradigma que organiza o código em **classes** e **objetos**, promovendo reuso, organização e encapsulamento de dados e comportamentos.

## **Os 4 Pilares da POO**

1. **Abstração**  
    → Focar apenas nos detalhes importantes do objeto, ocultando complexidades.  
    Ex: Um bolo tem sabor, cobertura e valor. Não precisamos saber como ele é feito, apenas usar seus dados.
    
2. **Encapsulamento**  
    → Esconder os detalhes internos de implementação e proteger os dados.  
    Ex: Usar propriedades (get/set) em vez de acessar diretamente os atributos.
    
3. **Herança**  
    → Permite criar novas classes com base em classes existentes.  
    Ex: Uma classe `BoloDeAniversario` pode herdar de `Bolo`.
    
4. **Polimorfismo**  
    → Permite que um mesmo método tenha comportamentos diferentes dependendo do objeto.  
    Ex: Um método `Assar()` pode ter implementações diferentes para `Bolo`, `Pão`, `Pizza`.
    

---

## **Onde está o objeto no código?**

### **Classe**

A **classe** é o **molde** para criar objetos. Ela define quais **atributos** (dados) e **métodos** (comportamentos) os objetos terão.

csharp

Copiar código

`namespace Aula1_Poo;  public class Bolo {     public string Sabor;     public int Kilos;     public string Cobertura;     public bool Recheio;     public int Camada;     public DateTime DataFabricacao;     public decimal Valor; }`

---

### **Instância**

Instanciar uma classe é **criar um objeto real a partir do molde**.

csharp

Copiar código

```
using Aula1_Poo;
using static System.Console;

public class Program
{
    public static void Main(string[] args)
    {
        // 1. Criando o primeiro objeto
        var boloCenoura = new Bolo();
        boloCenoura.Sabor = "Cenoura";
        boloCenoura.Cobertura = "Chocolate";
        boloCenoura.Kilos = 1;
        boloCenoura.Valor = 20.0M;
        boloCenoura.DataFabricacao = new DateTime(2025, 06, 01);

        // 2. Exibindo dados
        Console.WriteLine("Sabor: " + boloCenoura.Sabor);
        Console.WriteLine("Cobertura: " + boloCenoura.Cobertura);
        Console.WriteLine("Peso: " + boloCenoura.Kilos + " kg");
        Console.WriteLine("Valor: R$" + boloCenoura.Valor);
        Console.WriteLine("Data de fabricação: " + boloCenoura.DataFabricacao);

        // 3. Segundo objeto
        var boloChocolate = new Bolo();
        boloChocolate.Sabor = "Chocolate";
        boloChocolate.Cobertura = "Chocolate";
        boloChocolate.Kilos = 1;
        boloChocolate.Valor = 20.0M;
        boloChocolate.DataFabricacao = new DateTime(2025, 06, 01);

        // 4. Lista de bolos
        List<Bolo> vitrineBolos = new List<Bolo>();
        vitrineBolos.Add(boloCenoura);
        vitrineBolos.Add(boloChocolate);
        vitrineBolos.Add(boloChocolate); // repetido propositalmente

        // 5. Listando todos os bolos
        foreach (Bolo bolo in vitrineBolos)
        {
            Console.WriteLine("\n--- Bolo na vitrine ---");
            Console.WriteLine("Sabor: " + bolo.Sabor);
            Console.WriteLine("Cobertura: " + bolo.Cobertura);
            Console.WriteLine("Peso: " + bolo.Kilos + " kg");
            Console.WriteLine("Valor: R$" + bolo.Valor);
            Console.WriteLine("Data de fabricação: " + bolo.DataFabricacao);
        }
    }
}

```
---

## **Métodos**

### **Com `return`**

Métodos que **executam uma ação e retornam um valor**.

### **Sem retorno (void)**

Métodos que **executam algo**, mas **não retornam valores**.

### **Invocação de métodos**

Criar um método **não é suficiente**. Você precisa **chamá-lo** (invocá-lo) para que ele seja executado.

---

### **Exemplo completo com método com `return`**

```
using Poo;
using static System.Console;

internal class Program
{
    public static void Main(string[] args)
    {
        Person person = new Person();
        person.name = "Vicente";

        Console.WriteLine("Digite a idade da pessoa:");
        int age = Convert.ToInt32(Console.ReadLine());

        string response = person.IfLegalPerson(age, person.name);
        Console.WriteLine(response);
    }
}

```

```
namespace Poo
{
    public class Person
    {
        public string name;
        public int age;

        public string IfLegalPerson(int age, string name)
        {
            if (age >= 18)
            {
                return $"O(a) {this.name} é maior de idade.";
            }
            else
            {
                return $"O(a) {this.name} é menor de idade.";
            }
        }
    }
}

```

```
namespace Poo;  
  
public class BankTerminal  
{  
    //instancia da classe bankoperations  
    BankOperation bank = new BankOperation();  
    public void Start()  
    {        var isExecution = true;  
        while (true)  
        {            DisplayMenu();  
            string option = Console.ReadLine();  
  
            switch (option)  
            {case "1":  
                    bank.CheckBalance();  
                    break;  
                case "2":  
                    bank.Deposit();  
                    break;  
                case "3":  
                    bank.withdraw();  
                    break;  
                case "4":  
                    isExecution = false;  
                    break;  
                default:  
                    Console.WriteLine("obrigado por usar, volte sempre");  
                    break;  
            }        }    }    public void DisplayMenu()  
    {        Console.WriteLine("-----------BANK TERMINAL---------");  
        Console.WriteLine("1 - Checar Saldo");  
        Console.WriteLine("2 - Deposito");  
        Console.WriteLine("3 - Sacar");  
        Console.WriteLine("4 - Sair");  
    }}
    
    
    
namespace Poo  
{  
    public class BankOperation  
    {  
        public decimal balance = 1000;  
  
        public void CheckBalance()  
        {            Console.WriteLine($"\nSeu saldo é de:{balance}");  
        }  
        public void Deposit()  
        {            Console.WriteLine("infomre o valor a ser depositado");  
  
            if (decimal.TryParse(Console.ReadLine(), out decimal amount) && amount > 0)  
            {                balance += amount;  
                Console.WriteLine($"seu saldo atualizado é de:{balance}");  
            }            else  
            {  
                Console.WriteLine("Valor invalido");  
            }        }  
        public void withdraw()  
        {            Console.WriteLine("infomre o valor a ser sacado");  
            if (decimal.TryParse(Console.ReadLine(), out decimal drawee) && drawee > 0)  
            {                if(drawee > balance)  
                {                    Console.WriteLine("saldo insuficinte");  
                }                else  
                {  
                    balance -= drawee;  
                    Console.WriteLine($"saldo atualizado após saque: {balance}");  
                }            }            else  
            {  
                Console.WriteLine("Valor invalido");  
            }            
        }    
        
    }
}

  
using Poo;  
using static System.Console;  
  
internal class Program  
{  
    public static void Main(string[] args)  
    {        BankTerminal terminal = new BankTerminal();  
        terminal.Start();  
    }}

```

![[Pasted image 20250601152244.png]]

```
namespace Poo;  
  
public class Cake  
{  
    public string Flavor;  
    public string Filling;  
    public string Coverage;  
    public int Layers;  
    public string Size;  
    public Cake()  
    {         Flavor = "Chocolate";  
         Filling = "Coconut";  
         Coverage = "Chocolate";  
         Layers = 1;  
         Size = "Small";  
    }
}
using System.Drawing;  
using Poo;  
using static System.Console;  
internal class Program  
{  

    public static void Main(string[] args)  
    {        Cake cake = new Cake();  
        Console.WriteLine($"Sabor: {cake.Flavor}");  
        Console.WriteLine($"Recheio: {cake.Filling}");  
        Console.WriteLine($"Cobertura: {cake.Coverage}");  
        Console.WriteLine($"Camadas: {cake.Layers}");  
        Console.WriteLine($"Tamanho: {cake.Size}");  
    }  
}


```