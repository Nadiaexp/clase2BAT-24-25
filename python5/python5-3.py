#Programa años bisiestos
n = int(input("Dame un año: "))

if (n % 4 == 0) and (n % 400) :
    print("Año  bisiesto.")
else :
    print("Año no bisiesto.")