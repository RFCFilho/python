#6. Crie uma lista(vetor) de 5 números inteiros e exiba a soma de todos os elementos.
#nome da lista.apend = adiciona um item no ultimo indice da lista;
# A lista precisa está vazia e ser colocada antes do while
numerosVetor = []
# O input também precisa ficar antes do loop
numeroEntrada = input("Insira um número aqui ou pressione enter para terminar: ")
# O loop precisa solicitar algo deferente de uma resposta para podre parar    
while numeroEntrada!="":
    numerosVetor.append(int(numeroEntrada))
    numeroEntrada = input("insira um numero aqui ou pressione enter para terminar :")

def soma_vetor(numerosVetor):
    soma = 0
    for numero in numerosVetor:
        soma += numero
    return soma

resultado = soma_vetor(numerosVetor)
print(f'A soma dos numeros da lista é:  {resultado}.')
    