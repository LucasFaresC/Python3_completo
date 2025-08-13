

while True:
    
    n1 = input("Digite um número: ")
    n2 = input("Digite outro número: ")
    
    operador = input("Digite o operador (+, -, *, /): ")
    
    operadores_validos = '+-/*'
    op_validos = None
    
    if operador not in operadores_validos:
        print('Operador Digitado invalido! ')
        continue #pula pro prox loop, até validar
    
    n_validados = None
    
    try:
        n1 = float(n1)
        n2 = float(n2)
        n_validados = True
        
    except:
        n_validados = False
        
        
    if n_validados == False:
        print('Um ou mais numeros numeros digitados são invalidos.')
        continue #pula pro prox loop
    
    sair = input('Deseja (s)air ? ').lower().startswith('s')
    
    if sair == True:
        break