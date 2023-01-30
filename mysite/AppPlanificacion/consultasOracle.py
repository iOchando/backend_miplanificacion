import cx_Oracle
import sqlite3
from django.http import JsonResponse

def conexionBD():
    hostname = '172.20.5.88'
    nombre_bd = 'Bizview Desarrollo'
    username = 'bi'
    password = 'bi'
    port = 1521
    sid = 'orclbi'
    try:
        #dsn = cx_Oracle.makedsn(hostname, port, sid)
        #conexion = cx_Oracle.connect(username, password, dsn)
        conexion = sqlite3.connect('sqlite3.db')
    except Exception as e:
        print("Ocurrió un error al conectar a Oracle: ", e)
    return conexion

def T_RGIP001():
    json_data = []
    try:
        conexion = conexionBD()
        cursor = conexion.cursor()
        query = " select " \
                "    ANOCON, MESCON, SEMCON, FECINI, FECFIN " \
                " from " \
                "     T_RGIP001 "
        cursor.execute(query)
        rows = cursor.fetchall()
        json_data = list()
        for row in rows:
            json_data.append({"ANOCON": row[0], "MESCON": row[1], "SEMCON": row[2], "FECINI": row[3], "FECFIN": row[4]})
    except Exception as e:
        print("Ocurrió un error Tabla Proveedores: ", e)

    conexion.close()
    return json_data
