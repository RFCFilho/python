

#Exercício 1
#Se a temperatura for menor que 10 graus = Muito frio!
#se menor que 20 graus = Ar fresco1
#O restante - Está quente

temperatura = int(input("Informe a temperatura aqui:  "))

if temperatura < 10:
    print("Está Muito Frio aqui!")
elif temperatura >= 10 and temperatura < 20:
    print("Está fresco aqui!")  
else:
    print("Está quente aqui!")
