## **1️⃣ Divisão do Conjunto de Dados (supervisionado)**

### Conceito:

- Em problemas **supervisionados**, o modelo aprende com dados que possuem **entrada (features) e saída (rótulo/target)**.
    
- Para avaliar corretamente o desempenho, os dados precisam ser **divididos** em conjuntos diferentes:
    
    1. **Treino (Training Set)** → usado para treinar o modelo.
        
    2. **Validação (Validation Set)** → usado para ajustar hiperparâmetros e evitar overfitting.
        
    3. **Teste (Test Set)** → usado para avaliar a performance final em dados **não vistos**.
        

### Métodos de divisão:

- **Hold-Out:** divisão simples (ex.: 70% treino, 15% validação, 15% teste).
    
- **K-Fold Cross-Validation:** dados divididos em K partes, cada parte serve de teste em uma rodada.
    
- **Stratified K-Fold:** mesma ideia do K-Fold, mas mantém proporção das classes para evitar desbalanceamento.
    

💡 **Dica:** Para problemas de classificação com classes desbalanceadas, sempre prefira **Stratified K-Fold**.

---

## **2️⃣ Métricas de Desempenho**

### Conceito:

- Avaliam **o quão bem o modelo aprendeu os padrões dos dados**.
    
- Dependem do tipo de problema:
    
    - **Classificação:** acurácia, precisão, recall, F1-score, AUC-ROC.
        
    - **Regressão:** RMSE, MAE, R².
        

### Importância:

- Permitem comparar modelos e escolher aquele que **melhor generaliza**.
    
- São métricas técnicas, ligadas diretamente à performance estatística do modelo.
    

---

## **3️⃣ Métricas de Negócio**

### Conceito:

- Avaliam **o impacto do modelo na realidade do negócio**, ou seja, se o modelo realmente traz **valor**.
    
- Exemplo:
    
    - Reduzir churn de clientes em X%.
        
    - Aumentar conversão de vendas em Y%.
        
    - Minimizar custo de falsos positivos ou falsos negativos.
        

### Importância:

- Um modelo pode ter ótima acurácia, mas **não gerar valor real** para o negócio.
    
- Essas métricas ajudam a **alinhar o modelo com objetivos estratégicos**.
    

---

## **4️⃣ Questões Não Funcionais**

### Conceito:

- Avaliam características **operacionais ou de qualidade** do modelo, não diretamente relacionadas à acurácia.
    
- Exemplos:
    
    - **Performance:** tempo de inferência, capacidade de processar grandes volumes de dados.
        
    - **Robustez:** resistência a ruído ou dados incompletos.
        
    - **Manutenibilidade:** facilidade de atualização e manutenção do modelo.
        
    - **Explicabilidade:** transparência e capacidade de explicar decisões (importante para setores regulados).
        

### Importância:

- Garantem que o modelo seja **eficiente, confiável e utilizável** em produção, além de apenas preciso.
    

---

## **📌 Resumo Integrado**

|Requisito|O que avalia|Exemplos / Observações|
|---|---|---|
|Divisão de dados|Avalia generalização|Hold-out, K-Fold, Stratified K-Fold|
|Métricas de desempenho|Avalia aprendizado do modelo|Acurácia, F1-score, RMSE, R²|
|Métricas de negócio|Avalia valor real|Redução de churn, aumento de vendas, ROI|
|Questões não funcionais|Avalia operação e qualidade|Tempo de inferência, robustez, explicabilidade|

💡 **Dica prática:**  
Um bom processo de validação **combina todos esses requisitos**:

- Divide os dados corretamente,
    
- Mede o desempenho técnico,
    
- Verifica impacto real no negócio,
    
- E garante que o modelo funcione bem em produção.
    

---

# Validações dos Modelos de treino

## [[Hold-Out]]
---
## [[K-Fold Cross-Validation]]
---
## [[Stratified K-Fold Cross-Validation]]
---
### 💡 Resumo Comparativo

|Método|Quando usar|Vantagens|Desvantagens|
|---|---|---|---|
|**Hold-Out**|Dados grandes e simples|Rápido, fácil de implementar|Alta variabilidade na avaliação|
|**K-Fold**|Dados pequenos ou médios|Avaliação robusta|Mais lento, não garante balanceamento de classes|
|**Stratified K-Fold**|Classificação com classes desbalanceadas|Avaliação robusta e balanceada|Mais lento e mais complexo|
