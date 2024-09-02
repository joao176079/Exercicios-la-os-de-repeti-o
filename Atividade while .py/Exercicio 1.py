'''''
Desenvolva um programa que conte quantos números negativos foram inseridos pelo usuário usando um laço while. 
O programa deve parar quando o usuário inserir 0 ou um número positivo
    . Mostre a quantidade de números negativos.
'''
contagem = 0
contador = 0
while True :
    contador -= 1
    contagem = int (input ("Digite o seu número :"))
    
    if contagem <= -1 :
        print ("Tudo certo até aqui")
    else :
        print ("Tente novamente ")
        break 
    print (f"Você digitou {contagem} números negativos!")
    