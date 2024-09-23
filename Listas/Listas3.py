
listas_produtos = []

for i in range (3):
    produtos = input ("Digite o seu produto: ")
    listas_produtos.append(produtos)

for i ,produtos in enumerate (listas_produtos) :
    print (f"O seu produto {i+1}ª : {produtos}")