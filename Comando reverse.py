import os 
os.system("cls || clear")

QUANTIDADE_DE_NUMEROS = int (input ("Digite a sua quantidade de números : "))
lista_de_numeros = []

for i in range (QUANTIDADE_DE_NUMEROS):
    numeros = int (input (f"Digite o seu número {i+1} : "))
    lista_de_numeros.append(numeros)

for numeros in reversed(lista_de_numeros):
    print (f"Seus números ao contrário são : {numeros}")


if QUANTIDADE_DE_NUMEROS < 0 or QUANTIDADE_DE_NUMEROS > 10 :
    input ("\nPor favor repita a sua pergunta , pois a quantidade de números é muito grande ! ")


