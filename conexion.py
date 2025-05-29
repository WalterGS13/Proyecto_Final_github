import mysql.connector
from mysql.connector import Error

#conexion a base de datos
try:
   conexion = mysql.connector.connect(
       host = 'localhost',
       port = 3306,
       user = 'wals',
       password = 'wals1234*',
       db = 'usuarios'
   )

   if conexion.is_connected():
       print("Conexion con exito")

except Error as ex:
    print("error de conexion", ex)

mycursor = conexion.cursor()

#funcion para crear cuenta en base a la informacion ingresada en los inputboxes (ban = numero de cuenta)
def crear_cuenta(dpi, nombre, edad, categoria, ban):
    if conexion.is_connected():
        mycursor.execute("INSERT INTO usuarios VALUES(%s, %s, %s, %s ,%s)", (dpi, nombre, edad, categoria, ban))
        conexion.commit()

#funcion para buscar cuenta en base al dpi
def buscar_cuenta(dpi):
    if conexion.is_connected():
        mycursor.execute("SELECT BAN FROM usuarios WHERE DPI = %s", (dpi,))
        cuenta = mycursor.fetchall()
        return(cuenta[0][0])

# Busca mempresia por medio del dpi
def buscar_membresia(dpi):
    if conexion.is_connected():
        mycursor.execute("SELECT CATEGORIA FROM usuarios WHERE DPI = %s", (dpi,))
        membresia = mycursor.fetchall()

        if mycursor.rowcount>0:
            return(membresia[0][0])
        else:
            print("No hay registros")