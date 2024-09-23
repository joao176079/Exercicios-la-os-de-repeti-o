import os 
os.system("cls || clear")

def soma (num1 , num2):
    valor  = num1 + num2
    return valor

num1 = int (input("Digite o seu primeiro numero : "))
num2 = int (input("Digite o seu segundo numero : "))

valor = soma(num1 , num2)

print (f"O seu valor foi : {valor}")