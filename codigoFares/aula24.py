'''
Operadores Logicos de Grupos
- IN => se está não está contido
- NOT IN => se não está contido
- strings são interaveis
'''

nome = input("Digite seu nome: ")
encontrar = input("Digite oque deseja encontrar: ")

if encontrar in nome: 
    print(f"{encontrar} está contido em {nome}")
else:
    print(f"{encontrar} não está contido em {nome}")

