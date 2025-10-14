### Como funciona:

- Divide o dataset em **dois conjuntos principais**:
    
    - **Treino** (training set) → usado para treinar o modelo.
        
    - **Teste** (test set) → usado para avaliar a performance do modelo em dados que ele **nunca viu**.
        
- Exemplo: 70% treino e 30% teste.
    

### Exemplo prático:

- Dataset: 1000 registros.
    
- Treino: 700 registros → modelo aprende padrões.
    
- Teste: 300 registros → modelo é avaliado.
    

### Vantagens:

- Muito simples de implementar.
    
- Rápido para datasets grandes.
    

### Desvantagens:

- A performance pode **variar dependendo de como os dados foram divididos**.
    
- Um único hold-out pode não representar bem a população inteira, especialmente em datasets pequenos.
## Representação grafica 

![[img representação grafica Hold-out.png]]