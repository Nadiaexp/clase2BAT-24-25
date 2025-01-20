#Programa usuario-clave
code = input("Escribe el código/usuario: ")
clave = input("Escribe la clave: ")

while (clave != "0987") or (code != "admin") :
    print("Incorrecto, inténtalo de nuevo: ")
    code = input("Escribe el código: ")
    clave = input("Escribe la clave: ")
print("Correcto!")