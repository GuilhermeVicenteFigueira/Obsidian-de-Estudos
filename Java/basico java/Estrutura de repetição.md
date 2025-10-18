
### While:

```
int count = 0;  
while(count < 10){  
    count += 1;    System.out.println(++count);}
```
### Do While:

```
do{  
    System.out.println("dentro do do-while"+count);   
     count++;
}while (count<10);
```
### For:
```
for(count=0; count<10 ;count++){  
    System.out.println("for"+count);}-
```

### Exercicios:

```
           /*for(int i=0; i< 100000; i++){
            if(i % 2 == 0){
                System.out.println(i);
            }
        }*/

        /*for (int i = 0; i < 50; i++) {
            if (i > 25) {
                break;
            }
            System.out.println(i);
        }*/

       /* double carValue = 40000;
        for (int installment  = 1 ; installment  <= carValue ; installment ++) {
            double carInstallment = carValue / installment;
            if(carInstallment < 1000){
                break;
            }
            System.out.println("parcela " + installment + " R$ "+ carInstallment);
        }*/
    }
```