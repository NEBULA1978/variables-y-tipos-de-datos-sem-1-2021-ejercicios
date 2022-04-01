
s1 = input("s1: ") #retorna string
# s1 = input("Ingresa una cadena caracteres: ").lower() 
s2 = input("s2: ")
a = int(input("Ingresa a: "))
b = int(input("Ingresa b: ")) #Para hacer operaciones matematicas
print(type(s1))
print(type(a))

cadena1 = s1.lower() * a
# Para separar por espacio algo concadenando
# cadena2 = (s2.lower() + " ")* b
# Para separar por -- algo concadenando
cadena2 = (s2.lower() + "--")* b

concadenacion= cadena1 +" "+ cadena2 #concadeno los resultados
print(concadenacion)
# Abajo Es lo mismo que arriba
# print(cadena1 + cadena2)
