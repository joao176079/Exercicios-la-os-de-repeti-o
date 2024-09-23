import os 
os.system("cls || clear")

valores_armazenados = []
valores_negativos = []
valores_positivos = []

for i in range (5):
    valor = int (input ("Digite o seu número : "))
    valores_armazenados.append(valor)

    if valor < 0 :
        valores_negativos.append(valor)
    else :
        valores_positivos.append(valor)
print (f"Valores armazenados {valores_armazenados}")
print (f"Valores negativos = {valores_negativos}")
print (f"Valores positivos = {valores_positivos}")
