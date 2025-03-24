#programa para saber se um motorista está acima da velocidade permitida

velocidade = int(input('Qual a velocidade?'))

if velocidade > 110: 
    print("Você está acima da velocidade permitida. ")
    print("Favor reduzir a velocidade!")
elif velocidade < 60:
    print("Favor dirigir acima dos 80km H")
else: 
    print('velocidade ok')

