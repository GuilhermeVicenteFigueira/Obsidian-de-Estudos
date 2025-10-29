## ***O que é chave estrangeira?***
- Um campo (ou conjunto de campos) que faz referencia à chave primária de outra tabela.
- Estabelece relacionamentos entre tabelas.
- Garante a consistência dos dados.
- ***Exemplo:*** Matricula_aluno na tabela matriz faz referência  à tabela Aluno .

## ***Papel na Integridade Referencial***
- Integridade referencial garante que não existam registro órfãos.
- ***Exemplo:*** Não é possível registrar uma matricula de um aluno inexistente.
- Banco de dados impera automaticamente inserções ou exclusões inválidas.
- Fundamental para manter os dados coerentes e confiáveis .

## ***Restrições ON DELETE e ON UPDATE***
- Permite definir comportamentos automáticos quando o dado é referenciado for alterado ou excluído.

#### *ON DELETE*
- *RESTRICT* 
	- impede a exclusão se houver dependência
- *CASCADE* 
	- apaga tambem os registros
- *SET NULL*
	- define valor nulo na FK
- *NO ACTION* 
	- comportamento padrão (erro se houver dependência)
#### ON UPDATE
- Mesmo raciocínio, mas para mudanças de chave primária