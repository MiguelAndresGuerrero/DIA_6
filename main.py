#Le damos la bienvenida al usuario
Nombre=input("Dame tu nombre: ")
print("Bienvenido ", Nombre)
Dicci={"001":["manzanas",3500], "002":["peras",3000], "003":["sandias",5000], "004":["banano",2000], "005":["limones",3000]}

list={}


#menu interactivo por parte del usuario
ver=True
while ver==True:
    print("========MENU========")
    print("1. Agregar productos ")
    print("2. Contenido del carrito ")
    print("3. Calcular el total ")
    print("4. Finalizar programa ")
    
    
    print("--------------------------------")
    print(" 001:manzanas,3500")
    print("002 :peras,3000")
    print("003:sandias,5000")
    print("004:banano,2000")
    print("005 :limones,3000")
    print("--------------------------------")
    
    opc=int(input("escoje tu opcion\n"))
    if opc==1:
        print(Dicci)
        var=input("escoje tu producto\n")
        print(Dicci.get(var,"no tenemos este producto"))
        
        if var=="001":
            print(input("cuantas desea llevar?"))
            list=Dicci("001")*3500
            print(list)
        
        if var=="002":
            print(input("cuantas desea llevar?"))
            list=Dicci.get("002")*3000
            print(list)
            
        if var=="003":
            print(input("cuantas desea llevar?"))
            list=Dicci.get("003")*5000
            print(list)
            
        if var=="004":
            print(input("cuantas desea llevar?"))
            list=Dicci.get("004")*2000
            print(list)
            
        if var=="005":
            print(input("cuantas desea llevar?"))
            list=Dicci.get("005")*3000
            print(list)
            
    if opc==2:
        print(list)
        
    if opc== 4:
        break
    
#Creado por Miguel Guerrero C.C 1090381839, Luis Bautista C.C 1091356439, Luis Miguel  C.C 1090381345