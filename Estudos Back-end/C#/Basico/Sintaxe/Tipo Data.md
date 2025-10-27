```
using System.Globalization;
using System.Text;

namespace EstudosC
{
    class Program
    {
        static void Main(string[] args)
        {
            // Criação de uma data sem hora (DateOnly)
            DateOnly dia = new DateOnly(2025, 12, 1);

            // Formata a data para o formato brasileiro (ex: 01/dezembro/2025)
            string diaEmTexto = dia.ToString("dd/MMMM/yyyy", new CultureInfo("pt-BR"));  // Corrigido "bt-BR" → "pt-BR"

            // Criação de uma data completa com hora
            DateTime dia1 = new DateTime(2025, 12, 1, 20, 07, 50);

            // Pega o momento atual (com hora)
            DateTime hoje = DateTime.Now;

            // Pega o dia de hoje com hora zerada (00:00:00)
            DateTime hoje1 = DateTime.Today;

            // Hora atual no fuso UTC (padrão global)
            DateTime paratrablho = DateTime.UtcNow;

            // Soma 1 dia à data de hoje
            DateTime novaData = hoje1.AddDays(1);

            // Soma 1 hora à data de hoje
            DateTime novaData2 = hoje1.AddHours(1);

            // Impressão dos resultados
            Console.WriteLine("Agora: " + hoje);
            Console.WriteLine("Hoje (zerado): " + hoje1);
            Console.WriteLine("Dia em texto formatado: " + diaEmTexto);
            Console.WriteLine("Data com hora definida: " + dia1);
            Console.WriteLine("UTC Agora: " + paratrablho);
            Console.WriteLine("Amanhã: " + novaData);
            Console.WriteLine("Hoje + 1h: " + novaData2);
        }
    }
}

```