"""
 Pide al usuario su nombre y un número. Después de esto, muestra por
pantalla, su nombre el número de veces que haya elegido. Comprueba y evita
que se produzcan errores.

"""

x = input("Escribe tu nombre: ")
n = int(input("Escribe un número: "))

while n > 0 :
    print(x)
    n = (n - 1)
print("Adiós")
    