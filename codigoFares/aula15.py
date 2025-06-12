'''
Input - Pegar dados do usuario
- pega e tem que armazenar em uma variavel

'''

nome = input("Qual é o seu nome ? ") # lembra do espaço no final da string
print(f"Olá {nome}")

primeiro_numero = input("Digite um numero: ")
segundo_numero = input("Digite um numero: ")

primeiro_numero = int(primeiro_numero)
segundo_numero = int(segundo_numero)

print(f"a soma dos numeros é: {primeiro_numero + segundo_numero}")