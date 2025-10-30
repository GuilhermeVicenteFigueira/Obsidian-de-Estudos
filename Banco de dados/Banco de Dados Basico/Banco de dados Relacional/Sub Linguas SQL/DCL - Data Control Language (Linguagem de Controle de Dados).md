
DCL envolve comandos relacionados ao controle de acesso e permissões no banco de dados. Service para conceder (grant) ou revogar (revoke) privilégiops de usuario/roles

###  *GRANT*
- concede privilégios (permissões ) sobre objetos (tabelas, views, sequences, etc.) ou até mesmo privilégios de sistema (ex: criar banco, criar tabelas)
- Pode contribuir permissões de leitura (SELECT). escrita (INSERT, UPDATE, DELETE), execução (EXECUTE em formações) e outras.

```
--Conceder permissões de SELECT e INSERT na tabela 'produtos' ao role 'vendedor'
GRANT SELECT, INSERT ON produtos TO vendedor;

--Conceder permissões de todas as ações (ALL PREVILEGIS) na base de dados "loja" ao role "adimin_loja"
GRANT ALL PRIVILEGES ON DATABASE loja TO admin_loga;

-- Conceder permissões de USAGE em um schema
GRANTE USAGE ON SCHEMA relátorio TO analista;
```

### REVOKE
- Revoga privilégios anteriormente concedidos
- O uso de REVOKE retira aceso a comandos específicos

````
--Revogar remissões de DELETE de "vendedor" sobre a tabela "produtos"
REVOKE DELETE ON products FROM vendedor;

--Revogar todas as permissões de um role espefico
REVOKE ALL PRIVILEGES ON DATABASE loja FROM admin_loja;
``` 
