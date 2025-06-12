'''
Capturar erros 
- try => tenta executar um bloco de código
- except => ocorre algum erro ao tentar executar, e roda o códifo identado abaixo -> estoura o erro
'''

numero_str = input("Digite um numero pra ser dobrado: ") # input sempre retorna string

try: # try precisa ter linha de codigo dentro se nao fica puto
    
    print(f"Str: {numero_str}")
    
    numero_float = float(numero_str)

    print(f"Float: {numero_float}")
    print(f"{numero_float * 2} = 2 x {numero_float}")
    
except: # bloco de código que roda quando um erro é detectado
    print("Isso não é o numero")

print(numero_str.isdigit())
