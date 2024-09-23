import time
import os 
os.system('cls || clear')


def soma (numero1 ,  numero2 ):
    valor = numero1 + numero2 
    return valor 

numero1 = int (input ("Digite o seu primeiro valor : "))

numero2 = int (input ("Digite o seu segundo valor : "))

valor = soma (numero1 , numero2)
time.sleep(2)

print (f"O seu valor foi : {valor}")