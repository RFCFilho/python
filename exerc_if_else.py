#condições:
#se a idade for menor que 18 = menor de idade 
#Se maior ou igual a 18 e menor que 60 igua a adulto
#se a idade for maior que 60 anos = idoso

idade = int(input("Digite aqui a sua idade:  "))

if idade < 12:
    print("você é uma criança, menor de idade!")
elif idade >= 12 and idade < 18:
    print("Você é um adolescente - menor de idade!")  
elif idade >= 18 and idade < 60:
    print("você é adulto! ")  
else:
    print("IDOSO")
