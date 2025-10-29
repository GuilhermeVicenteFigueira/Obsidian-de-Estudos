## _**Requisitos:**_

- A tabela deve já estar na **4ª Forma Normal (4FN)**;
    
- Todas as **dependências de junção (join dependencies)** precisam ser eliminadas;
    
- Cada informação deve estar **dividida ao máximo**, sem perda de dados ao recombinar as tabelas.
    

---

## _**Instruções:**_

- Analise se **a tabela pode ser dividida em várias outras** sem perder informações quando for refeita por _JOIN_;
    
- **Cada tabela deve representar apenas uma relação direta e única** entre as entidades envolvidas;
    
- A decomposição deve ser **sem redundância e sem perda de informação**.
    

---

## _**Observações Importantes:**_

- A 5FN também é chamada de **Forma Normal de Projeção–Junção (PJNF)**;
    
- É usada para resolver **dependências complexas de junção**, geralmente em bancos com múltiplas relações entre entidades;
    
- Na prática, é **rara de ser aplicada** — pois a maioria dos bancos bem modelados já está normalizada até a 3FN ou 4FN.
    

---

## _**Exemplo Simplificado:**_

Suponha uma tabela que armazena **quais professores ensinam quais matérias em quais turmas**.  
Se ela puder ser dividida em três tabelas independentes:

- Professores ↔ Matérias
    
- Matérias ↔ Turmas
    
- Professores ↔ Turmas
    

E ainda assim for possível reconstruir todas as informações originais por _JOIN_,  
então ela está na **5ª Forma Normal**.