### Como funciona:

- Divide os dados em **K partes iguais (folds)**.
    
- Treina o modelo **K vezes**:
    
    - Cada vez, um fold diferente é usado como teste.
        
    - Os outros K-1 folds são usados como treino.
        
- A performance final é a **média das métricas** em todos os folds.
    

### Exemplo prático:

- Dataset: 1000 registros, K=5.
    
- Folds: 200 registros cada.
    
- Iterações:
    
    1. Treino: 800, Teste: 200
        
    2. Treino: 800, Teste: 200 (outro fold)  
        … até percorrer todos os folds.
        

### Vantagens:

- Avaliação mais **robusta e confiável** que hold-out.
    
- Reduz variabilidade devido à divisão do dataset.
    

### Desvantagens:

- Mais **computacionalmente custoso**, porque o modelo precisa ser treinado K vezes.
    
- Ainda não considera balanceamento de classes se houver desbalanceamento.


## Presentação grafica de K-Fold
![[img representação grafica de K-Fold.png]]