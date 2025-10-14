### 🌌 O que é a maldição da dimensionalidade?

É um conjunto de problemas que surgem quando trabalhamos com dados em **muitas dimensões (variáveis/features)**. Quanto mais dimensões você adiciona, mais difícil se torna analisar, visualizar e modelar os dados, porque o espaço cresce de forma exponencial.

---

### ⚠️ Principais consequências

1. **Sparsidade (esparsidade dos dados)**
    
    - Em altas dimensões, os pontos ficam muito espalhados.
        
    - Isso faz com que os dados se tornem "raros", dificultando encontrar padrões.
        
2. **Distâncias perdem significado**
    
    - Em 2D ou 3D, faz sentido falar que um ponto está "próximo" de outro.
        
    - Em altas dimensões, a diferença entre as distâncias mínimas e máximas tende a diminuir, ou seja, **todos os pontos ficam quase igualmente distantes**.
        
3. **Explosão combinatória**
    
    - A quantidade de dados necessária para cobrir bem o espaço cresce exponencialmente com o número de dimensões.
        
    - Isso causa problemas de **overfitting** e dificulta treinar modelos de Machine Learning.
        
4. **Visualização impossível**
    
    - A partir de 4 dimensões já não conseguimos visualizar diretamente.
        
    - Dependemos de projeções ou técnicas de redução de dimensionalidade.
        

---

### 📉 Como lidar com isso?

- **Redução de dimensionalidade** (PCA, t-SNE, UMAP).
    
- **Seleção de features** (eliminar variáveis irrelevantes ou redundantes).
    
- **Regularização** em modelos para evitar overfitting.
    
- **Aumento de dados** para compensar a dispersão.
    

---

👉 Em resumo:  
A **maldição da dimensionalidade** mostra que, em espaços de alta dimensão, os dados ficam esparsos, distâncias perdem sentido e precisamos de muito mais dados para manter a mesma densidade de informação. Por isso, **menos pode ser mais** em ciência de dados: escolher boas variáveis é mais importante do que ter muitas.

---

![[Img a maldição de dimensionalidade.png]]