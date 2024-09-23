lista_de_notas = []

for i in range (4):
    notas = int (input (f"Digite a sua {i+1}ª nota : "))
    lista_de_notas.append(notas)

for i , notas in enumerate (lista_de_notas):
    print (f"A sua {i+1}ª nota foi : {notas}")
    
    soma_das_notas = sum(lista_de_notas)


media_das_notas = soma_das_notas / len(lista_de_notas)


print(f"A soma das suas notas é: {soma_das_notas}")
print(f"A média das suas notas é: {media_das_notas:.2f}")