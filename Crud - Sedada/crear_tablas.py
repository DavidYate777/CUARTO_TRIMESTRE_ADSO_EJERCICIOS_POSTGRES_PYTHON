from conexionpostgres import conectar

conexion = conectar()

if conexion:

    cursor = conexion.cursor()

    # ROLES
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS roles(
        id_rol SERIAL PRIMARY KEY,
        nombre VARCHAR(50) NOT NULL
    );
    """)

    # USUARIOS
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios(
        id_usuario SERIAL PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        apellido VARCHAR(100) NOT NULL,
        correo VARCHAR(100) UNIQUE NOT NULL,
        password VARCHAR(255) NOT NULL,
        id_rol INT,
        FOREIGN KEY(id_rol)
        REFERENCES roles(id_rol)
    );
    """)

    # CATEGORIAS
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS categorias(
        id_categoria SERIAL PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL
    );
    """)

    # PRODUCTOS
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos(
        id_producto SERIAL PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        descripcion TEXT,
        precio NUMERIC(10,2) NOT NULL,
        disponible BOOLEAN DEFAULT TRUE,
        id_categoria INT,
        FOREIGN KEY(id_categoria)
        REFERENCES categorias(id_categoria)
    );
    """)

    # MESAS
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS mesas(
        id_mesa SERIAL PRIMARY KEY,
        numero_mesa INT NOT NULL,
        capacidad INT NOT NULL,
        estado VARCHAR(20) DEFAULT 'Libre'
    );
    """)

    # PEDIDOS
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pedidos(
        id_pedido SERIAL PRIMARY KEY,
        fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        estado VARCHAR(20) DEFAULT 'Pendiente',
        id_mesa INT,
        FOREIGN KEY(id_mesa)
        REFERENCES mesas(id_mesa)
    );
    """)

    # DETALLE PEDIDOS
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS detalle_pedidos(
        id_detalle SERIAL PRIMARY KEY,
        id_pedido INT,
        id_producto INT,
        cantidad INT NOT NULL,
        precio_unitario NUMERIC(10,2),

        FOREIGN KEY(id_pedido)
        REFERENCES pedidos(id_pedido),

        FOREIGN KEY(id_producto)
        REFERENCES productos(id_producto)
    );
    """)

    # FACTURAS
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS facturas(
        id_factura SERIAL PRIMARY KEY,
        subtotal NUMERIC(10,2),
        impuesto NUMERIC(10,2),
        total NUMERIC(10,2),
        metodo_pago VARCHAR(50),
        id_pedido INT,

        FOREIGN KEY(id_pedido)
        REFERENCES pedidos(id_pedido)
    );
    """)

    conexion.commit()

    cursor.close()
    conexion.close()

    print("Tablas creadas correctamente")