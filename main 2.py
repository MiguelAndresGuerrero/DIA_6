#le damos la bienvenida al usuario
nombre = input("Dame tu nombre: ")
print("Bienvenido,", nombre)

Lista = []
Secuencia = int(input("Ingresa la cantidad de números que deseas ingresar: "))

# Solicitar al usuario que ingrese los números y almacenarlos en la lista
for i in range(1, Secuencia + 1):
    numero = int(input(f"Ingresa el número {i}: "))
    Lista.append(numero)

# Solicitar al usuario que ingrese el resultado deseado
Resul = int(input("Ingresa el resultado que deseas obtener: "))

# Función para encontrar las posiciones de los números que sumados dan el resultado deseado
def encontrar_posiciones_para_suma(Lista, objetivo):
    num_posiciones = {}
    for idx, num in enumerate(Lista):
        complemento = objetivo - num
        if complemento in num_posiciones:
            return [num_posiciones[complemento], idx]
        num_posiciones[num] = idx
    return None

# Encontrar las posiciones de los números que sumados dan el resultado deseado
posiciones = encontrar_posiciones_para_suma(Lista, Resul)

# Mostrar el resultado
if posiciones:
    num1, num2 = posiciones
    print(f"Los números que sumados dan {Resul} son {Lista[num1]} y {Lista[num2]}")
    print(f"Posiciones en la lista original: {num1} y {num2}")
else:
    print(f"No se encontraron dos números en la lista que sumen {Resul}.")

#Creado por Miguel Andres C.C 1090381839