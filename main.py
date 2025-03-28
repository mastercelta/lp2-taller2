from flask import Flask, render_template, redirect
import sqlite3
from pprint import pprint

# cargamos todos los datos
conexion = sqlite3.connect('tienda.sqlite3')
conexion.row_factory = sqlite3.Row 
cursor = conexion.cursor()

# obtener todos los productos
cursor.execute("""
SELECT * FROM productos;
""")

productos = [dict(row) for row in cursor.fetchall()]

pprint(productos)
cursor.close()
conexion.close()


