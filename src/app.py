from flask import Flask, jsonify, request
from db import obtener_conexion
from ventas_predict import generar_informe
from exportar_sheets import exportar_a_sheets

app = Flask(__name__)

#Endpoint Listar Productos
@app.route('/api/productos', methods=['GET'])
def listar_productos():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Productos WHERE EstadoProd=1")
    productos = cursor.fetchall()
    conexion.close()
    return jsonify(productos)

