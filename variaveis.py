#Variáveis: é a capacidade de armazenar um valor qualquer em uma menmória

#Ex. 
nomes = 'Roberto'


#Variáveis primitivas e variáveis compostas
#Primitivas:
#INT (números inteiros);
#FLOAT (números quebrados, decimais);
#STRING Caracteres (nomes, palavras);
#BOLEAN Valores lógicos(Flaso ou Verdadeiro);
#NONE Não tem valor(represnta ausência de valor).

idade = 56 # int  (para números inteiros)
peso = 80.4 # Float (para números decimais)
nome = 'Roberto' #String (caracteres)
ativo = True # Bolean (pode ser True ou false (valores lógicos)
resultado = None #None (representa ausência de valor)

#O comando "TYPE" mostra a tipagem da variável
print(type(idade))
print(type(peso))
print(type(nome))
print(type(ativo))
print(type(resultado))

#Retorno dos printes types acima
#<class 'int'>
#<class 'float'>
#<class 'str'>
#<class 'bool'>
#<class 'NoneType'>

print(f"`Meu nome é: {nome} e eu tenho {idade} anos de idade.")