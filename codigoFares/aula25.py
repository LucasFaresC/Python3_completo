'''
Inter polação de caracteres 
- %inicialDoTipo % (nome_da_variavel)
-  p/ float %.quantidadeDeCasasf
'''

nome = "Gigante da colina"
gols_em_media = 3.55

variavel = "%s, fez em média %f gols esta temporada. " % (nome, gols_em_media)

print(variavel) # pode ser direto no print