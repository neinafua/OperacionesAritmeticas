#input
x= int (input("Ingrese el valor de x: "))
y= int (input("Ingrese el valor de y: "))

# prosesing
S= x+y
R= x-y
M= x*y
D= x/y
DE= x//y
MOD= x%y
P= x**y

# Output
print("resultado")
print("La suma de " + str(x) + " + " + str(y) + " es " + str(S))
print("La resta de " + str(x) + " - " + str(y) + " es " + str(R))
print("La multiplicacion de " + str(x) + " * " + str(y) + " es " + str(M))
print("La division de " + str(x) + " / " + str(y) + " es " + str(D))
print("La division entera de " + str(x) + " // " + str(y) + " es " + str(DE))
print("El modulo de " + str(x) + " % " + str(y) + " es " + str(MOD))
print("La potencia de " + str(x) + " ** " + str(y) + " es " + str(P))
