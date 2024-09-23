import os 

os.system("cls || clear ")

media = 0
nota = 0
media = []
listas_de_notas = []

for i in range (3):
    nota = float (input ("Digite a sua nota : "))
    listas_de_notas.append(nota)
    nota += nota
    media = nota / 3

# SÁIDA DE DADOS 
    while True :
        if nota > 0 or nota < 10 :
            print ("Por favor digite entre 0 e 10")
            break
if media >= 7:
    print (f"A sua media foi parabens passou !  : {media:.0f}")
else :
    print (f"Você perdeu com a media : {media:.0f}")



