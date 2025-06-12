'''
Conversão de dados ou coerção
- mudar um dado de um tipo pra outro
- coersion, typecasting, type conversion
- tipos primitivos são imutaveis => str, int, float, bool
- o python so vai mudar o tipo de variavel se isso puder ser feito
- classe int muda o tipo do dado pra int se possivel
'''

print('a'+ "b") # concatenação de string com o operador de mais (+)
print("1", type(1)) # output de 1 e de tipo string
print(int('1'), type(int("1")))

'''
- classe bool avalia se é True ou falso
- string vazia dá False
- se a string não é vazia então vai dar True
'''

print(bool("")) # vai dar False
print(bool("como tem algo na string vai dar bom")) # vai dar True
print(bool(10)) # True
print(bool(0)) # False => 0 é falso em binário

stringcomnumero = str(11) + 'b'
print(stringcomnumero) #output: 11b