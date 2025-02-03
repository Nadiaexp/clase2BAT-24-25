"""
n1 = 5
n2 = 6
n3 = 7
n4 = 8
n5 = 9

datos = [5, 6, 7, 8, 9]
datos.append(15)
datos.append(20)

print("Imprimimos la primera y la tercera")
print(datos[0])
print(datos[2])

print("Imprimimos todo el array")
for i in range(0,len(datos)):
    print(datos[i])

print("Imprimimos todo el array pero al revés")
for i in range(len(datos))-1,-1,-1:
    print(datos[i])

"""

#Declaro el vector datos
datos = []


for i in range (0,5):
    datos.append(int(input("Dame un dato: ")))

datos[0] = 500
for i in range (0,5):
    print(datos[i])