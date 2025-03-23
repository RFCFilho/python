#4. Escreva um programa em Python que verifique se um número é par ou ímpar..

num_Par_Ou_Impar = int(input( "Escreva um numero aqui: "))

def par_Ou_Impar(num_Par_Ou_Impar):
    if (num_Par_Ou_Impar % 2 == 0):
        print(f"O numero {num_Par_Ou_Impar} é par")
    else:
        print(f"O numero {num_Par_Ou_Impar} é impar")

par_Ou_Impar(num_Par_Ou_Impar)
