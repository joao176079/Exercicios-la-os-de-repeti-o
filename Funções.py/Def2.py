import time
import os 
os.system('cls || clear')


def soma (numero1 ,  numero2 ):
    valor = numero1 + numero2 
    return valor 

numero1 = int (input ("Digite o seu primeiro valor : "))
time.sleep(2)
numero2 = int (input ("Digite o seu segundo valor : "))

valor = soma (numero1 , numero2)


print (valor)