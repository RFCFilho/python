#Se compra qq valor - 5% desconto
#Se compras acima de 100 Reais 10%
#Se compras acima de 200 Reais 20% de desconto


valor_compra = float(input("Entre com o valor da sua compra para obter seu desconto:R$ "))

valor_compra5 = valor_compra * 1.05
#valor_compra100 = t
#valor_compra200 = b
if valor_compra <= 100:
    print(valor_compra - valor_compra5)
