a= int(input("a: "))
b= int(input("b: "))
c= int(input("c: "))

s= (a + b + c)/2
print(s)

# Para hacer raizes cuadradas
# A = (s*(s-a)*(s-b)*(s-c) ) ** (1/2)
A = (s*(s-a)*(s-b)*(s-c) ) ** (0.5)

print(A)