'''
Crie um programa que peça ao usuário para inserir números inteiros até que a soma dos números ímpares inseridos seja maior que 200. 
O programa deve exibir o total de números ímpares inseridos e a soma desses números. 
'''

soma = 0
contador = 0

while True :
    inserir = int (input ("Digite o seu número:  "))

    if inserir % 2 != 0:
        soma+= inserir 
        contador += 1

    if soma > 200:
        break
        
print (f'\nQuantidade de números inseridos : {contador}')
print(f"soma: {soma}")