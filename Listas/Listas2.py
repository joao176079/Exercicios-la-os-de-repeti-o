import os 
os.system("cls || clear ")

media = 0
nota = 0
media = []
listas_de_notas = []

for i in range (5):
    nota = float (input ("Digite a sua nota : "))
    listas_de_notas.append(nota)
    nota += nota
    media = nota / 5

# SÁIDA DE DADOS 
    
if media >= 7:
    print (f"A sua media foi parabens passou !  : {media:.0f}")
elif media >= 5 :
    print (f"Você está de recuperação pois a sua nota foi de : {media:.0f}")
else :
    print (f"Você perdeu com a media : {media:.0f}")