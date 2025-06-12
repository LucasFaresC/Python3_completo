# ex1
def ex1():
    numero_int = input('Digite um numero inteiro: ')

    try:
        numero_int = int(numero_int)
        
        if (numero_int%2 == 0):
            print(f'{numero_int} é par!')

        else:
            print(f'{numero_int} é ímpar!')



    except:  
        print('Você não digitou um numero inteiro')
        
#ex2

def ex2():
    
    horario = input('Que horas são ?\n>>>')
    
    horario = int(horario)
    if (horario >= 0 and horario <= 11):
        print("Bom dia!")
        
    elif(horario >= 12 and horario <= 17):
        print('Boa Tarde!')
    
    elif(horario >= 18 and horario >= 23):
        print('Boa Noite!')
        
        

#ex3

def ex3():
    
    nome = input('Qual é o seu nome ')
    caracteres = len(nome)
    
    if(caracteres <= 4):
        print(f'{nome} é um nome curto')
        
    elif(caracteres >=5 and caracteres <= 6):
        print(f'{nome} é um nome normal')
    
    elif(caracteres > 6):
        print(f'{nome} é um nome grande')
        
        
ex1()