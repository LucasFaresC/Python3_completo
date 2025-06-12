'''
Fatiamento de strings
- index 012345678...
- index negativo -9-8-7-6-5.....
- Fatimento => [i:f:p]
- Função len => retorna quantidade | não retorna index max
'''


carro = "Wolkswagens Bora"

print(len(carro))


print(carro[-1:-17:-1]) # entre colchetes index, quantidades do index, passo
print(carro[::-1]) 