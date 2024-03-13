bandas=[]


#Construyendo la interfaz
print("***ALTAVOZ ES TU VOZ***")
print("***********************")

opcion=100
while(opcion!=5):

    print("1. Registrar Banda")
    print("2. Buscar Informacion de una Banda")
    print("3. Agenda del evento")
    print("4. Modificar una banda")
    print("5. SALIR")

    opcion=int(input("Digita una opcion: "))

    if opcion==1:
        banda={}
        #creando los datos del diccionario
        banda["id"]=int(input("Digita el id: "))
        banda["nombre"]=input("Nombre de la banda: ")
        banda["genero"]=input("Genero: ")
        banda["clasificacion"]=input("Clasificacion: ")
        banda["tiempo"]=int(input("Tiempo: "))
        banda["costo"]=int(input("Costo: $"))
        
        #Agregando un diccioanrio a una lista
        bandas.append(banda)

    elif opcion==2:
        
        bandaBuscada=input("Digita el nombre de la banda que estas buscando: ")
        for bandAuxiliar in bandas:
            if bandAuxiliar["nombre"]==bandaBuscada:
               #como lo encontre muestro los datos de bandAuxiliar
                print(f"id: {bandAuxiliar["id"]} --- nombre: {bandAuxiliar["nombre"]} ")
            else:
               print("parce siga buscando....")

    elif opcion==3:
        print(bandas)
    elif opcion==4:
        pass
    elif opcion==5:
        pass
    else:
        pass