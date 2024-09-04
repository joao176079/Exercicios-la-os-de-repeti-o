'''
Crie um programa que ajude um estudante a calcular a média de suas notas.
O programa deve permitir que o usuário insira notas de provas até que o usuário insira um valor negativo.
O programa deve calcular e exibir a média das notas inseridas.
'''

soma_notas = 0
contador_notas = 0


while True:

    nota = float(input("Digite uma nota : "))
    

    if nota < 0:
        break
    

    if nota < 0 or nota > 10:
        print("Nota inválida. Digite uma nota entre 0 e 10.")
        continue
    

    soma_notas += nota
    contador_notas += 1


if contador_notas > 0:
    media = soma_notas / contador_notas
    print(f"A média das notas é: {media:.2f}")
else:
    print("Nenhuma nota válida foi inserida.")