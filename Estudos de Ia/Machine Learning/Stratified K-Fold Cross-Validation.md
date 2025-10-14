
### Como funciona:

- É uma variação do K-Fold.
    
- Mantém **a proporção das classes em cada fold**, útil para problemas de classificação **desbalanceada**.
    
- Por exemplo, se 70% dos dados são da classe A e 30% da classe B, cada fold manterá aproximadamente essa proporção.
    

### Exemplo prático:

- Dataset: 1000 registros (700 A, 300 B), K=5.
    
- Cada fold terá 140 A e 60 B.
    
- Treino e teste mantém a proporção original, evitando que algum fold fique só com uma classe.
    

### Vantagens:

- Evita **folds desproporcionais**, garantindo uma avaliação mais realista.
    
- Mantém a confiabilidade do K-Fold, mas com equilíbrio de classes.
    

### Desvantagens:

- Computacionalmente custoso.
    
- Mais complexo de implementar que o K-Fold simples.

## Representação grafica de K-Fold Cross-Validation
![[img K-Fold Cross-Validation.png]]