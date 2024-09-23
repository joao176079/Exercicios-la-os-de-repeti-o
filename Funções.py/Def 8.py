import os 
os.system("cls || clear ")

def aplicar_inflacao(preco):
  
    if preco < 100:
        inflacao = 0.01
    else:
        inflacao = 0.20
    
    preco_inflacionado = preco * (1 + inflacao)
    return preco_inflacionado

def main():
    
    preco = float(input("Digite o preço do produto: R$ "))
    
    
    preco_inflacionado = aplicar_inflacao(preco)
    
    
    print(f"O preço após a inflação é: R$ {preco_inflacionado:.2f}")


if __name__ == "__main__":
    main()
