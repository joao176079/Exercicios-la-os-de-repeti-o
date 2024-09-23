import time
import os 
os.system("cls || clear")


def soma(numero1, numero2):
    valor = numero1 + numero2
    return valor


numero1 = int(input("Digite o seu primeiro valor: "))
time.sleep(2)  

numero2 = int(input("Digite o seu segundo valor: "))




valor = soma(numero1, numero2)


print(f"O seu valor foi: {valor}")



lista_de_numeros = []


for i in range(5):
    numero = int(input(f"Digite o {i+1}º número para a lista: "))
    lista_de_numeros.append(numero)


soma_lista = sum(lista_de_numeros)


print(f"A lista de números é: {lista_de_numeros}")
print(f"A soma dos números na lista é: {soma_lista}")
