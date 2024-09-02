'''''
Escreva um programa que use um laço while para encontrar o primeiro número maior que 50 que seja divisível por 7. Exiba esse número.

Dica: Inicie com uma variável em 51 e use o operador % para verificar divisibilidade por 7. Continue até encontrar um número que satisfaça a condição.
'''
numero = 51

while  True :
    numero = int (input("Digite um número : "))
    numero +=1
    if numero % 7 == 1 :
        print ("Tudo certo !")
    else :
        print ("Digite novamente um número compativel.")
        break





