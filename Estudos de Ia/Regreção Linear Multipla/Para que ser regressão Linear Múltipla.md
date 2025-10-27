### 1. Para que serve a **Regressão Linear Múltipla**:

A **regressão linear múltipla** é usada quando você quer **prever um valor contínuo (y)** com base em **duas ou mais variáveis independentes (x₁, x₂, x₃...)**.

**Exemplos:**

- Prever o preço de uma casa (y) com base em metragem (x₁), número de quartos (x₂) e idade do imóvel (x₃).
    
- Estimar vendas de um produto (y) considerando gastos em marketing online (x₁), offline (x₂) e preço do produto (x₃).
    
- Prever consumo de energia (y) baseado em temperatura (x₁), número de pessoas na casa (x₂) e horas de uso de eletrodomésticos (x₃).
    

A fórmula geral é:

y=b0+b1x1+b2x2+...+bnxny = b_0 + b_1 x_1 + b_2 x_2 + ... + b_n x_ny=b0​+b1​x1​+b2​x2​+...+bn​xn​

- b0b_0b0​ = intercepto (valor de y quando todas as x = 0)
    
- b1,b2,...bnb_1, b_2, ... b_nb1​,b2​,...bn​ = coeficientes que mostram o impacto de cada variável sobre y
    

O objetivo continua sendo **encontrar a “linha” (ou hiperplano) que melhor se ajusta aos dados**.

---

### 2. Melhor tipo de **ML** para regressão linear múltipla:

- **Aprendizado supervisionado** ✅  
    Porque você tem entradas (x₁, x₂, …) e saídas conhecidas (y).
    
- Dentro do supervisionado, **tipo: regressão** ✅  
    Pois o objetivo é prever valores contínuos, e não categorias.
    

**Resumo rápido:**

|Tipo de problema|Variáveis|ML adequado|
|---|---|---|
|Linear simples|1|Regressão supervisionada|
|Linear múltipla|≥2|Regressão supervisionada|

---
