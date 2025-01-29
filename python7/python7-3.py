"""
 Pide al usuario un número entero (por ejemplo, 58) y nos dé todos los
múltiplos de 7 que hay entre el número 1 y ese número (incluido)

"""

n = int(input("Dime un número entero: "))

for x in range (1,n) : 
    print(n, "x", 7, n * x)