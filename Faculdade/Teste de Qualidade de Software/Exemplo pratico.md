
# App: Software de cursos

## Objetivos: 
Garantir o funcionamento correto das funcionalidade(Login, matricula, cursos comprados, realização de compra, busca de cursos, adição de aulas e adição cursos)
## Escopo:
 - Testar: (Login, matricula, cursos comprados, realização de compra, busca de cursos, adição de aulas e adição cursos).
 - Não testar: Comentários do videos, avalição das aulas


## Tipo de testes:

Funcional, integração, usabilidade, sobrecarga do sistema com usuários, segurança.
## Critérios de aceitação:

- Entrada: Requisitos completos e documentados, ambiente estável, versão mais recente para todos os usarios(web, desktop, android, aios).
- Saida: Relatório completo dos testes com as fragilidade do sistema junto ao melhorias documentadas e aprovado.

## Recursos:  
Equipe de Qa, devs, Ux, Po/PM, Engenheiro de software

## Cronograma: 
Planeamento 2d, preparação 3d, execução  7d, correções 4d, Gordura 3d, encerramento 2d

## Risco de mitigação:
Instabilidades, insatisfação de clientes, prazos curtos, incompatibilidades, cursos fora do ar, desconexão de clientes, lentidão -> mitigar com o alinhamento rápido, ambientes, redundantes, prioridade e teste preventivos.

---

# Id:  CT-1000

## Descrição: 

- Buscar Curso

## Pré-condições:

- Usuário precisa já estar logado ou se estiver na web pode verificar os cursos antes de cadastrar
## Passos para execução: 

1. Estar ou não Logado.
2. Clicar na aba de Pesquisa.
3. *Pesquisar.*

## Dados de entrada:

- Estar logado ou não
## Resultado esperado:

- Encontrar o curso se houver ou os mais próximos ou da mesma categoria 

## Criterio de aceitação  (Pass/Fail):

- Pass: Cliente tem acesso aos cursos que tiver na plataforma.
- Fail: Erro volta erro de 404

---

# Id:  CT-001

## Descrição: 

- Logar no app/ Site

## Pré-condições:

- Usuário precisa esta cadastrado no sistema
## Passos para execução: 

1. Entrar no app ou entrar no site.
2. Colocar Email or Nome da conta.
3. Colocar a senha.
4. Clicar no botão e entrar.
5. Fazer o captcha.
6. *Logar*.

## Dados de entrada:

- Email or Nome da conta
- Senha

## Resultado esperado:

- Entrar no site or app;

## Criterio de aceitação  (Pass/Fail):

- Pass: Cliente tem acesso aos cursos comprados ou pode buscar cursos.
- Fail: Erro de Atenticação tentativo novamente.
---

# Comprar curso

- Entrar no site 
- fazer login
- ir na aba principal
- clicar na aba de busca
- pesquisar curso
- clicar no botão de comprar curso
- escolher forma de pagamento
- usufruir do curso


