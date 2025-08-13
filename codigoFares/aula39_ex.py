
nome = 'Lucas Fares'
contador = 0
novo_nome = '' #inicializando variavel com string vazia

while contador < len(nome):
    print(nome[contador]) #só to mostrando a letra
    
    letra = nome[contador]
    novo_nome += f'*{letra}'
    contador += 1
    
    if contador == len(nome): #quando estiver no ultimo caracter
        novo_nome += "*"
    
print(f'\n{novo_nome}')