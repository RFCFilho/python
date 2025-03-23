#Metodo para tornar todas a letras minusculas "print(nome da variável.lower())" eX.comer é muito bom
mensagem = "Comer é Muito Bom"
print(mensagem.lower())

#metodo para imprimir tudo maiúsculo "print(nome da variável.upper())" COMER É MUITO BOM
print(mensagem.upper())

#Metodo para imprimir a primeira letra maiúscula "print(nome da variável.capitalizer)" Comer é muito bom
print(mensagem.capitalize())

#Metodo para encontrar a posiçaõ de um caractere "print(nome da variável.find('caractere a ser encontrado'))" Retornou o index 0
print(mensagem.find('C'))
#Com o finde tambem pode ser encontrada uma palavra expecifica. neste caso a palvra muito está iniciando no indice 8
print(mensagem.find("Muito"))

#O metodo que troca um string por outra é o replace print(nome da variável.replace('Muito', 'Muitissímo')) = Comer é Muitissímo Bom
print(mensagem.replace('Muito', 'Muitissímo'))