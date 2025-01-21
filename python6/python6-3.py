#Programa continuar: 
"""
Escriba un programa que pregunte una y otra vez si desea continuar con el programa, 
siempre que se conteste exactamente sí (en minúsculas y con tilde).
"""

r = input("¿Desea continuar? ")

while (r == "sí") :
    r = (input("¿Desea continuar? "))
print("¡Vale!")