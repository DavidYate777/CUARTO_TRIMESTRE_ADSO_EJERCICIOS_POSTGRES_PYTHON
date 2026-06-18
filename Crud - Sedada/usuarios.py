from conexionpostgres import conectar

def crear_usuario():

    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    correo = input("Correo: ")
    password = input("Contraseña: ")
    id_rol = int(input("ID Rol: "))

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    INSERT INTO usuarios
    (nombre, apellido, correo, password, id_rol)
    VALUES (%s,%s,%s,%s,%s)
    """,(nombre, apellido, correo, password, id_rol))

    conexion.commit()

    print("Usuario registrado")

    cursor.close()
    conexion.close()


def listar_usuarios():

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM usuarios")

    for usuario in cursor.fetchall():
        print(usuario)

    cursor.close()
    conexion.close()