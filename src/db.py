import mysql.connector

def obtener_conexion():
    return mysql.connector.connect(
        host = "",
        user ="",
        password = "",
        database = ""
    )