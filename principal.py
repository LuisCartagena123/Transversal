import funciones as fn

empleados = []
while True:

    print(fn.menu)
    try:
        opc = int(input("ingrese una opcion"))

        if opc == 1:
            
            print(fn.listatrabajadores)
            print(fn.asignarsueldos)

        elif opc == 2: 
            print()
        elif opc == 3: 
            print(fn.verestadísticas)
        elif opc == 4:
            print()
        elif opc == 5: 
            print("""Finalizando programa…
                    Desarrollado por Luis Cartagena
                    RUT 21.827.283-0""")
            break
        else: 
            print("opcion invalida, por vafor ingreseuna opcion correcta")
    except ValueError:
        print("La opcion debe ser un numero: ")