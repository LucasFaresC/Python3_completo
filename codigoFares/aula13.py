'''
f-string - Formatação de string
- delimitado pelo f (minusculo) no começo da string
- nome da variavel entre chaves => {}
- após o nome da variavel dois pontos seguido de ponto o numero de casas decimais que se quer mostrar e f no final => :.2f | arredonda
- 
'''
nome = "Lucas Fares"
altura_metros = 1.8
peso = 117.5
imc = peso/(altura_metros**2)

print(nome, "tem", altura_metros, "metros de altura, pesa", peso, "kg, e portanto tem imc de:", imc, "kg/m²")
print(f"{nome} tem {altura_metros} metros de altura, pesa {peso} kg, e portanto tem imc de: {imc:.2f} kg/m²")
