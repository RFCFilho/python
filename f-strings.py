nome = 'Roberto'
sobrenome = 'Fernandes'
idade = 38

print(f'Meu nome é {nome} {sobrenome} e eu tenho {idade} anos de idade')

# f string formata e concatena o texto: 
#sintax print(f'Tudo aui dentro')

#SEQUENCIAS DE ESCAPE

mensagem = "Aprender python \né muito simples"
print(mensagem)
#Aprender python 
#é muito simples

mensagem_coluna = 'coluna1\tcoluna2\tcoluna3' #mensagem em tabulação
print(mensagem_coluna)
#coluna1 coluna2 coluna3

mensagem_barra_invertida = "Aprender \"python\" é muito divertido"
print(mensagem_barra_invertida)
#Aprender "python" é muito divertido

#tabulando 
mensagem_tabulada = 'Nome:\tRoberto\nIdade:\t38 anos\nPais:\tBrasil'
print(mensagem_tabulada)
#Nome:   Roberto
#Idade:  38 anos
#Pais:   Brasil