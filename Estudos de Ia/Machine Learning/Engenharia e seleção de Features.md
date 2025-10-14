
- **O que é:** Criar ou transformar variáveis para melhorar o desempenho de modelos de Machine Learning.
    
- **Exemplos:**
    
    - Transformações matemáticas (log, raiz quadrada).
        
    - Combinar variáveis (ex.: `idade * renda`).
        
    - Extrair informações de datas, textos ou categorias.
        
- **Objetivo:** Deixar os dados mais **informativos e interpretáveis** para o modelo.
    

---

## ✂️ Seleção de Features

- **O que é:** Escolher apenas as variáveis mais relevantes para o modelo.
    
- **Métodos:**
    
    - **Filtro:** Estatísticas (correlação, chi-square).
        
    - **Wrapper:** Testa combinações de features usando o modelo.
        
    - **Embedded:** A seleção acontece durante o treinamento (ex.: Lasso, árvores).
        
- **Objetivo:** Reduzir dimensionalidade, **evitar overfitting** e aumentar a eficiência do modelo.
    

---
## 💡 **Resumo rápido:**

- Engenharia = criar e transformar features.
    
- Seleção = escolher apenas as importantes.
    
- Ambas ajudam a **melhorar desempenho e simplificar modelos**.


| Seleção                                                                                                                                                                                                           | Transoformação                                                                                                                                                      | Criação                                                                                                                               | Extração                                                                                                                                                                |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Processo de selecionar um subconjunto de features extraidas. A potuação de importancia de features e a matriz de correlação podem ser fatores na seleção de features mais relevantes para o treinamento do modelo | Pode incluir normalizações codificações de variaveis categoricas ou transformações matematicas. Além disso tratar features ausentes ou features que não são validas | Criar novas features a partir dos dados existentes, usando tecnicas como cobinação de variaveis , decomposição e calculos matematicos | Reduiz a quantidade de dados a ser tecnicas de redução de dimensionalidade. Diferente de um processo de transformação , é utilizando um modelo de ML para este processo |
