from conexionpostgres import conectar

def crear_pedido():

    id_mesa = int(input("ID Mesa: "))

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    INSERT INTO pedidos
    (id_mesa)
    VALUES (%s)
    """,(id_mesa,))

    conexion.commit()

    print("Pedido registrado")

    cursor.close()
    conexion.close()


def listar_pedidos():

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    SELECT * FROM pedidos
    """)

    for pedido in cursor.fetchall():
        print(pedido)

    cursor.close()
    conexion.close()