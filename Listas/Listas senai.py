import os 
os.system ("clear")
numeros_armazenados = []
numeros_negativos = []
numeros_postivos = []

for i in range (5):
    numero = int (input ("Digite o seu número : "))
    numeros_armazenados.append (numero)

    if numero < 0 :
        numeros_negativos.append(numero)
    else:
        numeros_postivos.append(numero)

    
print (f"O seus números armazenados : {numeros_armazenados}")    
print (f"O seus números postivos : {numeros_postivos}")    
print (f"O seus números negativos : {numeros_negativos}")