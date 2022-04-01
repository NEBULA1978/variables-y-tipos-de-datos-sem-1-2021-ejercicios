x=float(input("Ingrese x: "))
# operaciones logicas y condicionales
condicion1= x >= 1 and x <= 3 #[i...3]

y=float(input("Ingree y: "))
condiciion2= y >= 1 and y <= 5 #[i...5]

# Lacordenada x y esta dentro del rectangulo
totalCondicion= condicion1 and condiciion2

print("El punto (x,y) es interno:",totalCondicion)