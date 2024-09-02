'''''
Crie um programa que ajude um usuário a controlar seus gastos mensais.
O programa deve permitir que o usuário insira gastos diários até que o total gasto no mês exceda um orçamento inicial fornecido.
O programa deve exibir o total gasto e o valor  excedente.
orcamento = float(input("Digite o seu orçamento inicial: "))
'''
orcamento = int (input ("Digite o seu orçamento : "))
total_gasto = 0.0
valor_excedente = 0

while total_gasto <= orcamento:

    gasto_diario = float(input("Digite o valor do gasto diário: "))
    
    total_gasto += gasto_diario
    
    if total_gasto > orcamento:
        valor_excedente = total_gasto - orcamento
        print(f"Você excedeu o orçamento.")
        print(f"Total gasto: R${total_gasto}")
        print(f"Valor excedente: R${valor_excedente}")
    else:
        saldo_restante = orcamento - total_gasto
        print(f"Você pode gastar mais {saldo_restante} reais antes de exceder o orçamento.")
