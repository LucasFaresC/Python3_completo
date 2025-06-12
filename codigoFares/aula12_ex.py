'''
Calculo de imc 
- peso/altura²
- pode colocar 3 pontos pra colocar as variaveis dps =>  ...
'''

nome = "Lucas Fares"
altura_metros = 1.8
peso = 117.5
imc = peso/(altura_metros**2)

print(nome, "tem", altura_metros, "metros de altura, pesa", peso, "kg, e portanto tem imc de:", imc, "kg/m²")