Array multidimencionais são arrays que dentro de cada locação de memoria possui um array interno sendo ele com um tamanha variado para cada locação de memoria a escolha do programamador

```
public class aula08arrayMultidimensionais {
    public static void main(String[] args) {
        int[][] arrayInt = new int[3][];

            arrayInt[0] = new int[2];
            arrayInt[1] = new int[6];
            arrayInt[2] = new int[9];

        for (int [] arrayBase : arrayInt) {
            System.out.println("--------");
            for(int num: arrayBase){
                System.out.println(num);
            }
        }



        /*for (int i = 0; i < days.length; i++) {
            for (int j = 0; j < days[i].length; j++) {
                System.out.println(days[i][j]);
                System.out.println("----------------------------");
            }
        }*/
        /*System.out.println("------------------------");
        for(int[] slot : days){
            for(int num: slot) {
                System.out.println(num);
            }
        }*/
    }

}
```