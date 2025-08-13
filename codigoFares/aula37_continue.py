
contador = 0

while contador < 100:
    
    contador += 1
    
    if contador == 10 or contador == 50:
        
        continue
    
    print(contador)
    
qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=} {coluna=}')
        coluna += 1 
        
    linha += 1
    
print('cabou')