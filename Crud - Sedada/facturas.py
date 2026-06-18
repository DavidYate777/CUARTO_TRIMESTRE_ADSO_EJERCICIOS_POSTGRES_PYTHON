from conexionpostgres import conectar

def crear_factura():

    subtotal = float(input("Subtotal: "))
    impuesto = float(input("Impuesto: "))
    total = float(input("Total: "))
    metodo = input("Método pago: ")
    id_pedido = int(input("ID Pedido: "))

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    INSERT INTO facturas
    (subtotal, impuesto, total,
    metodo_pago, id_pedido)

    VALUES (%s,%s,%s,%s,%s)
    """,(subtotal,
         impuesto,
         total,
         metodo,
         id_pedido))

    conexion.commit()

    print("Factura registrada")

    cursor.close()
    conexion.close()


def listar_facturas():

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    SELECT * FROM facturas
    """)

    for factura in cursor.fetchall():
        print(factura)

    cursor.close()
    conexion.close()