Em Java, a declaração de arrays tem uma estrutura específica. Primeiro, define-se o tipo dos elementos, como `int`, seguido pelos colchetes `[]`, e então o nome da variável. Por exemplo: `int[] numeros`.

Para criar o array, utiliza-se a palavra-chave `new` seguida do tipo e do tamanho desejado entre colchetes. Exemplo: `numeros = new int[3];` — isso cria um array com três posições (índices 0, 1 e 2), todas inicialmente com o valor padrão para `int`, que é 0.



```
public class aula07Arrays {  
    public static void main(String[] args) {  
        int [] ages = new int[3];  
        ages[0]=1;  
        ages[1]=2;  
        ages[2]=3;  
        System.out.println(ages[0]);  
        System.out.println(ages[1]);  
        System.out.println(ages[2]);  
    }  
}
```

Exemplo de um percorrer uma lista:

```
String[] sex = new String[4];  
sex[0]="aarongar";  
sex[1]="Morgel";  
sex[2]="Yukimo";  
  
for (int i = 0; i < sex.length; i++) {  
      
    System.out.println(sex[i]);  
}
```