# Aprendizado Supervisionado:


É um **tipo de aprendizado de máquina (Machine Learning)** em que o modelo é treinado com **dados rotulados**.  
Ou seja: para cada **entrada (X)**, já sabemos a **saída correta (Y)**, e o modelo aprende a mapear a relação entre elas.

---

### 📌 Como funciona?

1. **Conjunto de treino**: você fornece exemplos (inputs) e suas respostas (labels).
    
    - Exemplo: imagens de gatos e cachorros (entrada) + a classificação correta ("gato" ou "cachorro").
        
2. **Treinamento do modelo**: o algoritmo tenta aprender uma função que relacione entradas → saídas.
    
    - Em outras palavras: "Se eu vejo essa entrada X, qual saída Y devo dar?"
        
3. **Predição**: depois de treinado, o modelo recebe novos dados (sem rótulos) e tenta prever a saída correta.
---
### 📊 Tipos principais de problemas em aprendizado supervisionado:

1. **Classificação**
    
    - Saída é uma **categoria**.
        
    - Exemplo:
        
        - Detectar spam ou não spam em emails.
            
        - Reconhecer dígitos de 0 a 9 em imagens.
            
2. **Regressão**
    
    - Saída é um **valor numérico contínuo**.
        
    - Exemplo:
        
        - Prever o preço de uma casa com base em tamanho e localização.
            
        - Estimar a nota de um aluno pela quantidade de horas de estudo.
            

---
### ⚙️ Exemplos de algoritmos usados:

- **Classificação**: Regressão Logística, Árvores de Decisão, Random Forest, SVM, Redes Neurais.
    
- **Regressão**: Regressão Linear, Ridge, Lasso, SVR, Redes Neural.
---
## 👉 Resumindo:  
**Aprendizado supervisionado = aprender com exemplos já resolvidos, para prever resultados de novos casos.**

![[Img Aprendizado Supervisionado.png]]