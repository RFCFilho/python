#Dada a lista criada pelo comando:
#lista=[1,2,”pirulito”,4,11,”teste”,44,56,true]
#Escreva um código que multiplique o conteúdo por 5 e imprima apenas os que
#possuem como resultado um número. (Obs: A lista fornecida é apenas um
#exemplo, o seu código deve ser capaz de realizar a mesma tarefa com outras
#listas fornecidas).

lista=[1,2,"pirulito",4,11,"teste",44,56,"true"]

so_numeros = []
so_strings = []

for item in lista:
    if isinstance(item, (int, float)):
        so_numeros.append(item)
    elif isinstance(item, str):
        so_strings.append(item) 


print(f"Numeros da lista: {so_numeros}")
print(f"Estas são as strings:  {so_strings}")

for item in lista:
    if isinstance(item, (int, float)):
        print(f"Apenas os números vezes cinco: {item *5}")