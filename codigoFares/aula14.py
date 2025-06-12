'''
Formatação de strings com o metodo Format
- metodo  => ações de objetos
- inserir variaveis na string via metodo => uso de {}
- a formatação de casas decimais funciona aqui também 
- demarcação por indice
- demarcação de parametro nomeado precisa ser nomeado
'''
a = 'A'
b = 'B'
c = 12.345

linha = 'a = {1}, b = {0}, c = {2:.2f}, d = {caso:.1f}'
formato = linha. format(a, b, c, caso=1.5) # indice 0, 1 e 2

print(formato)