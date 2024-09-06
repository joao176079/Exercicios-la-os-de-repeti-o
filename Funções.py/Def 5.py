import time
import os 
os.system('cls || clear')

def soma (numero1 , numero2):
    valor_de_soma = numero1 + numero2
    return valor_de_soma

def subtracao (numero1 , numero2):
    valor_de_subtracao = numero1 - numero2
    return valor_de_subtracao

def multiplicacao (numero1 , numero2 ):
    valor_de_multiplicacao = numero1 * numero2
    return valor_de_multiplicacao

def divisao(numero1 , numero2 ):
    valor_de_divisao = numero1 / numero2
    return valor_de_divisao

print ("Calculadora digital ")
numero1 = int (input ("Digite o seu primeiro número : "))
time.sleep(1)
numero2 = int (input ("Digite o seu segundo número : "))
time.sleep(1)


print ("""
Selecione o seu operador = + | - | / | * |       
       
       """)
opcao = input ("Digite a sua opção :  ").strip()

match (opcao):
    case '+':
       valor_de_soma = soma (numero1 , numero2)
       print(f"Soma: {valor_de_soma:.2f}")
    case '-':
        valor_de_subtracacao = subtracao (numero1 , numero2)
        print(f"Subtração: {valor_de_subtracacao:.1f}")
    case '/':
        valor_de_divisao = divisao (numero1 , numero2)
        print(f"Divisão: {valor_de_divisao:.1f}")
    case '*':
        valor_de_multiplicacao = multiplicacao (numero1 , numero2)
        print(f"Multiplicação: {valor_de_multiplicacao:.1f}")

