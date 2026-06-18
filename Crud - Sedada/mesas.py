from conexionpostgres import conectar

def crear_mesa():

    numero = int(input("Número mesa: "))
    capacidad = int(input("Capacidad: "))

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    INSERT INTO mesas
    (numero_mesa, capacidad)
    VALUES (%s,%s)
    """,(numero, capacidad))

    conexion.commit()

    print("Mesa registrada")

    cursor.close()
    conexion.close()


def listar_mesas():

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    SELECT * FROM mesas
    """)

    for mesa in cursor.fetchall():
        print(mesa)

    cursor.close()
    conexion.close()