''''
Desenvolva um programa que solicite ao usuário inserir um código de promoção para obter um desconto.
O código correto é "PROMO2024". O usuário tem 3 tentativas para acertar o código. Se o código estiver correto, exiba uma mensagem de "Código aceito" e o desconto.
Se o usuário errar o código nas 3 tentativas, exiba uma mensagem de "Código inválido".
'''''
valor = False 
codigo = 'PROMO2024'

for i in range (3):
    while True :
        codigo = input ("Digite o seu codigo : ")

        if codigo == 'PROMO2024' :
            print ("Bem vindo ")
            valor  = True 
            break
        else :
            print ("Codigo inválido")
            break 
    if valor :
        break 