#Operadores logicos 
# o operador "and" precisa que as primissas sejam verdadeiras para ser aceito o pedido 
#o operador "or" precisa de uma ou outra verdadeira

# Caso 1 - financiamento de crédito

renda_acima_perm = True 
nome_limpo =  True

if renda_acima_perm and nome_limpo: # Crédidto aprovado, uma e a outra são verdadeiras
    print("Crédito aprovado!")
else:
    print("Crédito negado!")

# Caso 2 - financiamento de crédito
renda_acima_perm1 = True 
nome_limpo1 =  False

if renda_acima_perm1 or nome_limpo1: # Credito aprovado, uma ou outra são verdadeiras
    print("Crédito aprovado!")
else:
    print("Crédito negado!")

operator = "banana" == 'Banana'
print(operator)

bissexto = int(input("Digite aqui o ano"))

if bissexto % 4 == 0 or bissexto != 100 and bissexto % 400 == 0:
    print("Este ano é bisseto")
else:
    print("Este ano não é bissexto")

