import os 
os.system ('cls || clear')

def calculo_idade(ano_de_nascimento):
    resultado =  2024 - ano_de_nascimento 
    return resultado
    
# Entrada 

ano_de_nascimento = int (input ("Digite o seu ano de nascimento : "))

# Processamento

resultado = calculo_idade(ano_de_nascimento)

# Resultado 
print (f'Resultado : {resultado}')






