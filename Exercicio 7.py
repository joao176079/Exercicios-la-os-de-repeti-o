'''
Crie um programa que solicite ao usuário criar uma senha.
O programa deve então pedir para confirmar a senha e garantir que ambas as senhas coincidam
. Se as senhas não coincidirem, o programa deve continuar pedindo para o usuário inserir e confirmar a  tenha até que ambas sejam iguais.
'''

import os
os.system("cls || clear")


novologin = input("Digite seu novo login: ")

novasenha = input("Digite sua nova senha: ")

login = input("Digite seu login: ")

senha = input("Digite sua senha: ")

while login != novologin and novasenha != senha:
      
      print("senha ou login incorretos")
      
      login = input("Digite seu login: ")
      
      senha = input("Digite sua senha: ")
      
      print('Bem vindo !')
      break