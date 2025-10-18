# Error:
erro se consiste quando a jvm precisa ser parada para o erro ser corrigido, sendo inevitável a continuação do software até que ele seja corrigido, falta de memoria etcc.

![[Pasted image 20250906153951.png]]

# RunTimeExeption 
## Unchecked
Erro de RunTimeExeption é um erro que é gerado em tempo de execução vinda de um código que está fedendo ou um errado

# Exception
## Cheked
É quando o erro é gerado e ele não é nem compilado

## Bloco Finally

```
try {  
        System.out.println("Abrindo arquivo");  
        System.out.println("Escrevendo dados no arquivo");  
        return "Conexão aberta";  
    } catch (Exception e) {  
        e.printStackTrace();  
    } finally {  
        System.out.println("fechando recuso liberado pelo SO");  
    }  
    return null;  
}
```

### TRY CATCH

### TRY FINALLY

### TRY CATCH FINALLY


## capturando multiplas exeções:

```
  try {  
  
    } catch (ArrayIndexOutOfBoundsException e){  
        System.out.println("Dentro do ArrayIndexOutOfBoundsException ");  
    } catch (IndexOutOfBoundsException e){  
        System.out.println("Dentro do IndexOutOfBoundsException");  
    } catch (IllegalArgumentException e) {  
        System.out.println("Dentro do IllegalArgumentException ");  
    } catch (ArithmeticException e){  
        System.out.println("Dentro do  ArithmeticException");  
    } catch (RuntimeException e) {  
        System.out.println("Dentro do RuntimeException");  
    }  
}
```

## ==REGRAS:==
TODA EXEÇÃO/ ERRO DEVE SER DO MAIS ESPECIFICO AO MAIS GENERICO

