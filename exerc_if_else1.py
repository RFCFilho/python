hora = int(input("Digite a hora aqui: "))

if hora >= 6 and hora < 12:
    print("Bom Dia ")
elif hora >= 12 and hora < 18:
    print("Boa Tarde")
else: 
    print("Boa Noite!")