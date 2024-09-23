import os 
os.system ("cls || clear")

lista_de_numeros = []

for i in range (6):
    numeros = int (input (f"Digite o seu {i+1}ª número : "))
    lista_de_numeros.append(numeros)
    
numeros_pares = []
numeros_impares = []

for numeros in lista_de_numeros:
    if numeros % 2 == 0:
        numeros_pares.append(numeros)
    else:
        numeros_impares.append(numeros)
    
print (f"Os seus números pares : {numeros_pares}")
print (f"Os seus números impares : {numeros_impares}")

quantidade_de_pares = len(numeros_pares)
quantidade_de_impares = len(numeros_impares)

print(f"A quantidade de números pares : {numeros_pares}")
print(f"A quantidade de números impares : {numeros_impares}")