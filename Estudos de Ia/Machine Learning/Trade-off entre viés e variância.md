
## 🎯 Conceito

O **trade-off viés-variância** é o equilíbrio entre **dois tipos de erro** que um modelo de Machine Learning pode ter:

1. **Viés (Bias)**
    
    - Erro devido a suposições **simplificadas demais** no modelo.
        
    - Alto viés → underfitting (modelo não aprende bem os padrões).
        
    - Sintoma: alto erro no treino **e** no teste.
        
2. **Variância (Variance)**
    
    - Erro devido à **sensibilidade do modelo aos dados de treino**.
        
    - Alta variância → overfitting (modelo aprende detalhes e ruídos).
        
    - Sintoma: baixo erro no treino, mas alto erro no teste.
        

---

## ⚖️ Trade-off

- Diminuir viés → modelo mais complexo → aumenta variância.
    
- Diminuir variância → modelo mais simples → aumenta viés.
    
- O objetivo é encontrar um **equilíbrio**, com **erro total mínimo** (somatório de viés² + variância + ruído).
    

---

## 💡 Resumo rápido

- **Underfitting** → alto viés, baixa variância.
    
- **Overfitting** → baixo viés, alta variância.
    
- **Trade-off** → ajustar o modelo para não sofrer nem de underfitting nem de overfitting.

---
## Representação por alvos
![[img Trade-off entre Vies e variancia exemplo em alvos.png]]

---
## Representação Grafica em um gráfico
![[img Trade-off entre Vies e variancia exemplo em graficos.png]]
