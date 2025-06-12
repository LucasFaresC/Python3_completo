'''
Tipo str (string)
- tigagem dinâmica (Forte) do python => tipo defino na hora, não precisa necessáriamente declarar o tipo
- string -> texto
- pode ser aspas duplas ou só uma aspas, mas não pode misturar na mesma string
- pra exibir caracter de escape, começa antes da string com r
'''

print(1234)
print('Aluno qualquer')
print('Lucas \'Fares') ## contra barra é caracter de escape => o prox caracter sera ingorado | como se foosse parte da string

'''
output:
1234
Aluno qualquer
Lucas 'Fares
'''

print(r"Hoje \" serei feliz\"") # r começando exibe caracter de escape
