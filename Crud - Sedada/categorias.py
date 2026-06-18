from conexionpostgres import conectar

def crear_categoria():

    nombre = input("Nombre categoría: ")

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    INSERT INTO categorias(nombre)
    VALUES(%s)
    """,(nombre,))

    conexion.commit()

    print("Categoría registrada")

    cursor.close()
    conexion.close()


def listar_categorias():

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    SELECT * FROM categorias
    """)

    for categoria in cursor.fetchall():
        print(categoria)

    cursor.close()
    conexion.close()