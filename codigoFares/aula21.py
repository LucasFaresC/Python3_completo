'''
Operadores Lógicos
- and => Todas as condições precisam ser verdadeiras
- tipo none => representa o não valor
'''

entrada = input("[E]ntrar [S]air \n>>> ")
senha = input("Senha: ")

senha_permitida = "link"

if entrada == "E" and senha == senha_permitida: 
    print("Entrar")

elif entrada == "S":
    
    print("Sair")

else: 
    print("Senha Incorreta!")    
    
    
print(True and True) #True
print(False and True) #False
print(True and False) #False
print(False and False) #False