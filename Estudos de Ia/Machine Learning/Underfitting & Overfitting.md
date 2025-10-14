## 🎯 Underfitting

- **O que é:** O modelo **não aprende bem os padrões** dos dados.
    
- **Causa:** Modelo muito simples ou poucos dados.
    
- **Sintomas:**
    
    - Alto erro no treino e no teste.
        
    - Não consegue capturar tendências dos dados.
        
- **Exemplo:** Ajustar uma linha reta a dados que têm uma curva complexa.
    

---

## 🎯 Overfitting

- **O que é:** O modelo **aprende demais os dados de treino**, incluindo ruídos.
    
- **Causa:** Modelo muito complexo ou dados insuficientes.
    
- **Sintomas:**
    
    - Baixo erro no treino, mas alto erro no teste.
        
    - Não generaliza para novos dados.
        
- **Exemplo:** Uma curva que passa exatamente por todos os pontos de treino, mas falha em novos dados.
    

---

## ⚖️ Como evitar

- **Regularização:** L1, L2, dropout.
    
- **Mais dados de treino.**
    
- **Simplificar o modelo.**
    
- **Cross-validation** para avaliar generalização.
    

---
## 💡 **Resumo rápido:**

- **Underfitting:** modelo simples demais → não aprende.
    
- **Overfitting:** modelo complexo demais → aprende demais, mas não generaliza.

# Visualização em gráfico 
![[Img Underfit , Overfit e optium.png]]