import os
os.system("cls || clear")

def calcular_media (numero_1 , numero_2):
    soma = numero_1 + numero_2
    resultado = soma /2    
    return resultado

numero_1 = int (input("Digite o seu primeiro número : "))
numero_2 = int (input ("Digite o seu segundo número : "))

media = calcular_media(numero_1 , numero_2)

print (media)
