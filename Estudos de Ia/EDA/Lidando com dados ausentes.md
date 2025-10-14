### 🔎 Tipos de dados ausentes

1. **MCAR (Missing Completely At Random)**
    
    - Os valores ausentes ocorrem **completamente ao acaso**, sem relação com outras variáveis ou com o próprio dado faltante.
        
    - Exemplo: um sensor que falhou em registrar a temperatura em um dia específico por defeito técnico.
        
    - Impacto: estatisticamente menos problemático, pois não introduz viés.
        
2. **MAR (Missing At Random)**
    
    - Os valores ausentes estão relacionados a **outras variáveis observadas**, mas não ao próprio valor faltante.
        
    - Exemplo: em uma pesquisa de saúde, pessoas mais jovens podem pular perguntas sobre medicamentos, mas a ausência depende da idade (que está registrada).
        
    - Impacto: é possível tratar com técnicas como imputação baseada em variáveis correlacionadas.
        
3. **MNAR (Missing Not At Random)**
    
    - Os valores ausentes dependem **do próprio valor não observado**.
        
    - Exemplo: pessoas com renda muito alta ou muito baixa podem se recusar a responder sobre salário.
        
    - Impacto: mais difícil de corrigir, pois há viés sistemático.
        

---

👉 Em resumo:

- **MCAR** = totalmente aleatório.
    
- **MAR** = relacionado a outra variável.
    
- **MNAR** = relacionado ao próprio dado faltante.