# numero decimal lo consideraos entero con float
# si es negativo consideramso su valor absoluto(positivo)
m= abs(int(float(input("Monto: "))))

# division normal
# cant20 = m / 20
# division entera
cant20 = m // 20
resto1 = m % 20

# division entera
cant10 = resto1 // 10
resto2 = resto1 % 10

# division entera
cant5 = resto2 // 5
cant1 = resto2 % 5


total = cant20 + cant10 + cant5 +cant1

print("Cantidad de billetes: ",total)

# print("cant20: ",cant20)
# print("cant10: ",cant10)
# print("cant5: ",cant5)
# print("cant1: ",cant1)
