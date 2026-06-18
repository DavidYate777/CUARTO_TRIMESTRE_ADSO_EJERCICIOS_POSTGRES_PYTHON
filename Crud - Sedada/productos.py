from conexionpostgres import conectar

# CREAR PRODUCTO
def crear_producto():

    nombre = input("Nombre del producto: ")
    descripcion = input("Descripción: ")
    precio = float(input("Precio: "))
    categoria = int(input("ID Categoría: "))

    conexion = conectar()

    cursor = conexion.cursor()

    sql = """
    INSERT INTO productos
    (nombre, descripcion, precio, id_categoria)
    VALUES (%s,%s,%s,%s)
    """

    valores = (
        nombre,
        descripcion,
        precio,
        categoria
    )

    cursor.execute(sql, valores)

    conexion.commit()

    print("✅ Producto registrado correctamente")

    cursor.close()
    conexion.close()


# LISTAR PRODUCTOS
def listar_productos():

    conexion = conectar()

    cursor = conexion.cursor()

    cursor.execute("""
    SELECT *
    FROM productos
    ORDER BY id_producto
    """)

    productos = cursor.fetchall()

    print("\n===== PRODUCTOS =====")

    for producto in productos:
        print(producto)

    cursor.close()
    conexion.close()


# BUSCAR PRODUCTO
def buscar_producto():

    id_producto = int(
        input("Ingrese ID del producto: ")
    )

    conexion = conectar()

    cursor = conexion.cursor()

    cursor.execute("""
    SELECT *
    FROM productos
    WHERE id_producto=%s
    """, (id_producto,))

    producto = cursor.fetchone()

    if producto:
        print(producto)
    else:
        print("❌ Producto no encontrado")

    cursor.close()
    conexion.close()


# ACTUALIZAR PRODUCTO
def actualizar_producto():

    id_producto = int(
        input("ID producto: ")
    )

    nombre = input("Nuevo nombre: ")

    precio = float(
        input("Nuevo precio: ")
    )

    conexion = conectar()

    cursor = conexion.cursor()

    cursor.execute("""
    UPDATE productos
    SET nombre=%s,
        precio=%s
    WHERE id_producto=%s
    """,
    (
        nombre,
        precio,
        id_producto
    ))

    conexion.commit()

    print("✅ Producto actualizado")

    cursor.close()
    conexion.close()


# ELIMINAR PRODUCTO
def eliminar_producto():

    id_producto = int(
        input("ID producto: ")
    )

    conexion = conectar()

    cursor = conexion.cursor()

    cursor.execute("""
    DELETE FROM productos
    WHERE id_producto=%s
    """,
    (id_producto,))

    conexion.commit()

    print("✅ Producto eliminado")

    cursor.close()
    conexion.close()