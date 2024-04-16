#le damos la bienvenida al usuario
nombre= input("Dame tu nombre \n")
print("Bienvenido",nombre)

Lista= []
Secuencia= int(input("Ingresa la secuencia de numeros "))

for i in range(0, Secuencia):
    Lista.append(input("Ingresa los numeros "))
    
Numeros_iguales= list(set(Lista))
    
Numeros_iguales.sort()
print(Numeros_iguales)
