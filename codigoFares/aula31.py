'''
None => não há valor
variavel flag => ajuda a ver se uma condição foi atendida ou nn
'''

condicao = False

passou_no_if = None # essa é a nossa flag

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo') 
    
    
if passou_no_if is None:
    print('Não passou no if')       
    