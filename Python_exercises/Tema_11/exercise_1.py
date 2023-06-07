import sqlite3

# Conecta a la base de datos o la crea si no existe
db_connection = sqlite3.connect('ej1.db')

# Crea un cursor para interactuar con la base de datos
db_cursor = db_connection.cursor()

# Crea la tabla "Alumnos" con las columnas "Id", "Nombre" y "Apellido"
db_cursor.execute("CREATE TABLE Alumnos(Id INT, Nombre TEXT, Apellido TEXT)")

# Inserta los datos de los alumnos en la tabla
db_cursor.execute("INSERT INTO Alumnos VALUES(1,'John', 'Smith')")
db_cursor.execute("INSERT INTO Alumnos VALUES(2,'Michael', 'Johnson')")
db_cursor.execute("INSERT INTO Alumnos VALUES(3,'Jessica', 'Williams')")
db_cursor.execute("INSERT INTO Alumnos VALUES(4,'David', 'Brown')")
db_cursor.execute("INSERT INTO Alumnos VALUES(5,'Sarah', 'Jones')")
db_cursor.execute("INSERT INTO Alumnos VALUES(6,'Emily', 'Davis')")
db_cursor.execute("INSERT INTO Alumnos VALUES(7,'Daniel', 'Miller')")
db_cursor.execute("INSERT INTO Alumnos VALUES(8,'Olivia', 'Wilson')")

# Confirma los cambios realizados en la base de datos
db_connection.commit()

# Realiza una búsqueda de un alumno por nombre en la tabla
db_cursor.execute("SELECT * FROM Alumnos WHERE Nombre = 'John'")

# Recupera los resultados de la búsqueda
filas = db_cursor.fetchall()

# Imprime las filas obtenidas por consola
print(filas)

# Cierra la conexión a la base de datos
db_connection.close()
