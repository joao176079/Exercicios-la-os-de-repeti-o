'''''
Escreva um programa que multiplique um número inicial por um fator dado pelo usuário até que o produto exceda 100.
Exiba o produto final e o número de multiplicações realizadas.

Dica: Use uma variável para o produto e outra para contar as multiplicações. 
Continue multiplicando o número pelo fator até que o produto seja maior que 100.
'''
numero_inicial= 2
produto = 0 
contador_multiplicacao= 100

while True :
    produto = int (input ("Digite o seu número : "))
    
    contador_multiplicacao += 1
    resultado = produto* numero_inicial
    if resultado < 100:
        print (f"O seu produto foi {resultado}")
        break


