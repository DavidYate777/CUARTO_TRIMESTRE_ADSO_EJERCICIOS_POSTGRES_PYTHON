from productos import *

while True:

    print("\n====================")
    print("   SISTEMA SEDADA")
    print("====================")

    print("1. Crear producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Salir")

    opcion = input("Seleccione: ")

    if opcion == "1":
        crear_producto()

    elif opcion == "2":
        listar_productos()

    elif opcion == "3":
        buscar_producto()

    elif opcion == "4":
        actualizar_producto()

    elif opcion == "5":
        eliminar_producto()

    elif opcion == "6":
        print("Hasta luego")
        break

    else:
        print("Opción inválida")