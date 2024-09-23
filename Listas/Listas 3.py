import os 
os.system("cls || clear ")

media = 0
nota = 0
listas_de_notas = []

for i in range (5):
    nota = float (input ("Digite a sua nota : "))
    listas_de_notas.append(nota)

maior_numero = max(listas_de_notas)
menor_numero = min(listas_de_notas)

# SÁIDA DE DADOS 

for contador , nota in enumerate (listas_de_notas):
    print (f"{contador + 1}ª nota {nota}")

print (f"Menor número : {menor_numero}")
print (f"Maior número : {maior_numero}")
