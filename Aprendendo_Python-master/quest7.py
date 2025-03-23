#7. Dada lista criada pelo comando:
#lista=[1,2,3,4,11,22,44,56,80,2,3,4]
#Escreva um código que percorra toda esta lista e infome o maior número
#encontrado.

lista=[1,2,3,4,11,22,44,56,80,2,3,4]
i = 0
maiorNum = lista[0]

while i < len(lista):
    if lista[i] > maiorNum:
        maiorNum = lista[i]
    i += 1
print(f"O maior número da lista apresentada é: {maiorNum}")

#-----------------------//----------------------------------

maior = lista[0]  # Assume que o primeiro elemento é o maior

for num in lista:
    if num > maior:
        maior = num

print(f"O maior número encontrado pelo for é: {maior}")

#---------------------------//--------------------------

print(f"O maior número encontrado pelo max é: {max(lista)}")


## **1. Usando `while`**  
#Código:  
#python
#lista = [1, 2, 3, 4, 11, 22, 44, 56, 80, 2, 3, 4]

#i = 0  # Inicializa o índice
#maior = lista[0]  # Assume que o primeiro elemento é o maior

#while i < len(lista):  # Percorre a lista enquanto i for menor que o tamanho da lista
#    if lista[i] > maior:  # Se o elemento atual for maior que o maior encontrado até agora
#        maior = lista[i]  # Atualiza o maior número
#    i += 1  # Incrementa o índice para ir para o próximo elemento

#print(f"O maior número encontrado é: {maior}")

### **Explicação**
#- **`i = 0`** → Criamos uma variável `i` para acompanhar a posição atual na lista.
#- **`maior = lista[0]`** → Assumimos que o primeiro número da lista é o maior (inicialmente).
#- **`while i < len(lista):`** → Executamos o loop enquanto `i` for menor que o tamanho da lista.
#- **`if lista[i] > maior:`** → Verificamos se o número atual da lista é maior que o maior já encontrado.
#- **`maior = lista[i]`** → Se for maior, atualizamos a variável `maior`.
#- **`i += 1`** → Avançamos para o próximo elemento da lista.
#- Quando o `while` termina, o maior número encontrado será impresso.

## **2. Usando `for`**  
#Código:  
#python
#lista = [1, 2, 3, 4, 11, 22, 44, 56, 80, 2, 3, 4]

#maior = lista[0]  # Assume que o primeiro elemento é o maior

#for num in lista:  # Percorre cada número da lista
#    if num > maior:  # Se o número atual for maior que o maior encontrado até agora
#        maior = num  # Atualiza o maior número

#print(f"O maior número encontrado é: {maior}")

### **Explicação**
#- **`maior = lista[0]`** → Começamos assumindo que o primeiro elemento é o maior.
#- **`for num in lista:`** → O `for` percorre cada número da lista automaticamente.
#- **`if num > maior:`** → Se o número atual for maior que o maior encontrado até agora, atualizamos.
#- **`maior = num`** → O maior número encontrado até o momento é atualizado.
#- No final do loop, o maior número é impresso.

#✅ **Por que usar `for`?**  
#O `for` é mais simples e legível porque percorre a lista sem precisar de um índice manual (`i`).

## **3. Usando `max()` (mais simples e eficiente)**  
#Código:  
#python
#lista = [1, 2, 3, 4, 11, 22, 44, 56, 80, 2, 3, 4]

#print(f"O maior número encontrado é: {max(lista)}")

### **Explicação**
#- A função **`max(lista)`** retorna o maior número da lista automaticamente, sem precisar percorrer manualmente.
#- **Mais eficiente** porque o Python internamente otimiza essa busca.
#- **Menos código** e mais legível.

## **Qual usar?**
#| Método  | Facilidade | Eficiência |
#|---------|-----------|------------|
#| `while` | Médio (precisa controlar `i`) | Menos eficiente, mas útil se precisar manipular o índice |
#| `for`   | Fácil (percorre a lista automaticamente) | Mais eficiente que `while` |
#| `max()` | Muito fácil (1 linha de código) | Mais eficiente e rápido |

#Se precisar apenas do maior número, use `max(lista)`.  
#Se quiser praticar lógica de repetição, use `for`.  
#Se precisar de controle sobre o índice, use `while`. 

print(f"O maior numero da lista no max é {max(lista)}") 