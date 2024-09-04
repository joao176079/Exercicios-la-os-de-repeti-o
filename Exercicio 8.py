'''
Crie um programa para ajudar o usuário a acompanhar suas metas de estudo.
O usuário define uma meta de horas de estudo e o programa deve permitir que o usuário insira o número de horas estudadas até que o total atinja ou exceda a meta.
O programa deve  exibir o total de horas estudadas e o valor excedente.
'''


horasdesejadas = int(input("Quantas horas você deseja estudar? "))
horastotaisdestudos = 0 
while True:
   
   horasestudadas = int(input("Quantas horas você estudou hoje ? "))
   
   horastotaisdestudos += horasestudadas
   if horasdesejadas > horastotaisdestudos:
      print("continue estudando")
   elif horastotaisdestudos <= horasdesejadas:
      print("você atingiu sua meta, continue estudando")
   elif  horastotaisdestudos > horasdesejadas :
    print("Agora descanse um pouco !")
   else: 
      print(None)