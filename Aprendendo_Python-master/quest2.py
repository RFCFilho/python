#Escreva um programa em Python que calcule se um ano é bissexto e informe ao
#usuário. Um ano é bissexto se ele for divisível por 4 e não por 100. A excessão a
#essa regra é se ele for divisível por 400..

ano = int(input("Digite o ano aqui: "))
def bissexto(ano):
    if (ano % 4 == 0 or ano % 100 != 0 and ano % 400 == 0):
        print(f"O ano de {ano} é um ano bissexto.")
    else:
         print(f"O ano de {ano} não é um ano bissexto. ")

bissexto(ano)