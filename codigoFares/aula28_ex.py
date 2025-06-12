'''
nome
nome invertido
nome tem ou nao espaços
numero de letras no nome
primeira letra do nome
ultima letra do nome

'''

nome = input("Qual é o seu nome: ")
idade = input("Qual é sua idade: ")


if not nome or not idade: #conferindo se os campos estão vazios  
    
    print("Desculpa você deixou campos vazios. ")
    
else:
    
    quantidade_de_caracteres_do_nome = len(nome) # conferindo tamanho do nome
    
    print(f"Seu nome é {nome}. ")
    print(f"Seu nome invertido é {nome[::-1]}. ")
    
    if " " in nome: #Conferindo se o espaço está contido na string
        print("Seu nome tem espaços. ")
    else:
        print("Seu nome não tem espaço. ")    
    
    
    print(f"A quantidade de caracteres (contando espaço) do seu nome é {quantidade_de_caracteres_do_nome}. ")
    print(f"Sua primeira letra do nome é {nome[0]}. ")
    print(f"Sua primeira letra do nome é {nome[quantidade_de_caracteres_do_nome - 1]}. ")
    
    
'''
RESOLUÇÃO DO PROFESSOR
nome = input('Digite o seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome NÃO contém espaços')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print("Desculpe, você deixou campos vazios.")
'''