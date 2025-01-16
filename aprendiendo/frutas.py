import sqlite3
from sqlite3 import Cursor,Connection

con =sqlite3.connect('data/frutas.db')
#conectar a la base de datos
# ../ -> se debe buscar desde donde se ejecuta el script de python
# atras/data/dase_datos

cursor = con.cursor()


def crear_tabla(cursor:Cursor,nombre,con:Connection):
    sql = f'CREATE TABLE IF NOT EXISTS {nombre} ( id INTEGER PRIMARY KEY, nombre TEXT, precio REAL )'
    cursor.execute(sql)
    con.commit()  

def poner_datos(cursor:Cursor,nombre,con:Connection):
    sql = f"INSERT INTO {nombre} (nombre, precio) VALUES ('Pera', 12.3), ('Manzana', 15.80)"
    cursor.execute(sql)
    con.commit()  

class Producto:
    def __init__(self,id,nombre,precio):
        self.id = id
        self.nombre = nombre
        self.precio = precio
    
    def get_valor_total(self):
        return self.precio * 3
    
    def __str__(self):
        return self.nombre
    
    def __repr__(self):
        return self.__str__()

def registros(cursor:Cursor):
    sql = 'Select * from products'    
    result = cursor.execute(sql).fetchall()    
    return [Producto(id,nom,precio) for id,nom,precio in result]

# crear_tabla(cursor,'products',con)
# poner_datos(cursor,'products',con)

print(registros(cursor))
con.close()

    




