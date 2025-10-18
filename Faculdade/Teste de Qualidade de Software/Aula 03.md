# BDD

## Funcionalidade: Cancelar compra

Como cliente do site 
Quero ter a possibilidade de cancelar uma compra que esteja
em meu carrinho.

## Cenário:  Cancelar compra no carrinho

Dado que o usuário  esteja na pagina do carrinho
Quando ele clicar no botão de excluir compra
Então o produto deve ser excluído do carrinho
E o valor do carrinho é atualizado


## Funcionalidade: Cancelar compra que já foi feita

Como cliente do site 
Quero ter a possibilidade de cancelar uma compra que já tenha pago

## Cenário: Cancelar compra após ter pago
Dado que o usuário já tenha comprado
E a compra tenha compensado no sistema
Quando ele clicar no botão de solicitar estorno
Então o sistema vai enviar o estorno para a bandeira do cartão que o cliente fez a compra 
E após o sistema fazer o estorno deve mostrar na tela do cliente um PopUp "Estorno enviado"
E enviar um comprovante de estorno no email cadastrado.


