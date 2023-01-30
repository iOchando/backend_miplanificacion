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

def FunGuardarDistAves(items):
    try:
        conexion = conexionBD()
        cursor = conexion.cursor()

        query = " INSERT INTO AppPlanificacion_distaves " \
                " (id_plan_id, agrupacion, status, familia, undLunes, undMartes, undMiercoles, undJueves, undViernes, undSabado, undTotal, tonLunes, tonMartes, tonMiercoles, tonJueves, tonViernes, tonSabado, tonTotal) " \
                " VALUES(:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13, :14, :15, :16, :17, :18) "

        for i in range(len(items)):
            cursor.execute(query, (items[i]['id_plan'], items[i]['agrupacion'], items[i]['status'], items[i]['familia'], items[i]['undLunes'], items[i]['undMartes'], items[i]['undMiercoles'], items[i]['undJueves'], items[i]['undViernes'], items[i]['undSabado'], items[i]['undTotal'], items[i]['tonLunes'], items[i]['tonMartes'], items[i]['tonMiercoles'], items[i]['tonJueves'], items[i]['tonViernes'], items[i]['tonSabado'], items[i]['tonTotal']))
            print("se añadio", items[i]["agrupacion"])
        conexion.commit()

        query2 = " select " \
                "    agrupacion, status, familia, undLunes, undMartes, undMiercoles, undJueves, undViernes, undSabado, undTotal, tonLunes, tonMartes, tonMiercoles, tonJueves, tonViernes, tonSabado, tonTotal " \
                " from " \
                "     AppPlanificacion_distaves "

        cursor.execute(query2)
        rows = cursor.fetchall()
        json_data = list([])
        
        for row in rows:
            json_data.append({"agrupacion": row[0], "status": row[1]})

        cursor.close()
        conexion.close()
        print(json_data)
        return json_data
    except Exception as e:
        print("Ocurrió un error al Añadir: ", e)
        return False

def FunGuardarDistFamilia(items):
    try:
        conexion = conexionBD()
        cursor = conexion.cursor()

        query = " INSERT INTO AppPlanificacion_distfamilia " \
                " (id_plan_id, familia, rendimiento,tonLunes, tonMartes, tonMiercoles, tonJueves, tonViernes, tonSabado, tonTotal) " \
                " VALUES(:1, :2, :3, :4, :5, :6, :7, :8, :9, :10) "

        for i in range(len(items)):
            cursor.execute(query, (items[i]['id_plan'], items[i]['familia'], items[i]['rendimiento'], items[i]['tonLunes'], items[i]['tonMartes'], items[i]['tonMiercoles'], items[i]['tonJueves'], items[i]['tonViernes'], items[i]['tonSabado'], items[i]['tonTotal']))
            print("se añadio", items[i]["familia"])
        conexion.commit()

        query2 = " select " \
                "    familia, rendimiento,tonLunes, tonMartes, tonMiercoles, tonJueves, tonViernes, tonSabado, tonTotal " \
                " from " \
                "     AppPlanificacion_distfamilia "

        cursor.execute(query2)
        rows = cursor.fetchall()
        json_data = list([])
        
        for row in rows:
            json_data.append({"familia": row[0], "rendimiento": row[1]})

        cursor.close()
        conexion.close()
        print(json_data)
        return json_data
    except Exception as e:
        print("Ocurrió un error al Añadir: ", e)
        return False

def FunGuardarDistComercial(items):
    try:
        conexion = conexionBD()
        cursor = conexion.cursor()

        query = " INSERT INTO AppPlanificacion_distcomercial " \
                " (id_plan_id, nombre, ventLunes, ventMartes, ventMiercoles, ventJueves, ventViernes, ventSabado, ventTotal, proLunes, proMartes, proMiercoles, proJueves, proViernes, proSabado, proTotal, tipo) " \
                " VALUES(:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13, :14, :15, :16, :17) "

        for i in range(len(items)):
            cursor.execute(query, (items[i]['id_plan'], items[i]['nombre'], items[i]['ventLunes'], items[i]['ventMartes'], items[i]['ventMiercoles'], items[i]['ventJueves'], items[i]['ventViernes'], items[i]['ventSabado'], items[i]['ventTotal'], items[i]['proLunes'], items[i]['proMartes'], items[i]['proMiercoles'], items[i]['proJueves'], items[i]['proViernes'], items[i]['proSabado'], items[i]['proTotal'], items[i]['tipo']))
            print("se añadio", items[i]["nombre"])
        conexion.commit()

        query2 = " select " \
                "    nombre, ventLunes, ventMartes, ventMiercoles, ventJueves, ventViernes, ventSabado, ventTotal, proLunes, proMartes, proMiercoles, proJueves, proViernes, proSabado, proTotal, tipo " \
                " from " \
                "     AppPlanificacion_distcomercial "

        cursor.execute(query2)
        rows = cursor.fetchall()
        json_data = list([])
        
        for row in rows:
            json_data.append({"nombre": row[0]})

        cursor.close()
        conexion.close()
        print(json_data)
        return json_data
    except Exception as e:
        print("Ocurrió un error al Añadir: ", e)
        return False

def FunEditarDistAves(items):
    try:
        conexion = conexionBD()
        cursor = conexion.cursor()
        
        query = " UPDATE AppPlanificacion_distaves SET undLunes = :1, undMartes = :2, undMiercoles = :3, undJueves = :4, undViernes = :5, undSabado = :6, undTotal = :7, tonLunes = :8, tonMartes = :9, tonMiercoles = :10, tonJueves = :11, tonViernes = :12, tonSabado = :13, tonTotal = :14 " \
                " WHERE id = :15 "

        for i in range(len(items)):
            cursor.execute(query, (items[i]['undLunes'], items[i]['undMartes'], items[i]['undMiercoles'], items[i]['undJueves'], items[i]['undViernes'], items[i]['undSabado'], items[i]['undTotal'], items[i]['tonLunes'], items[i]['tonMartes'], items[i]['tonMiercoles'], items[i]['tonJueves'], items[i]['tonViernes'], items[i]['tonSabado'], items[i]['tonTotal'], items[i]['id']))

        conexion.commit()

        query2 = " select " \
                "    agrupacion, status, familia, undLunes, undMartes, undMiercoles, undJueves, undViernes, undSabado, undTotal, tonLunes, tonMartes, tonMiercoles, tonJueves, tonViernes, tonSabado, tonTotal " \
                " from " \
                "     AppPlanificacion_distaves "

        cursor.execute(query2)
        rows = cursor.fetchall()
        json_data = list([])
        
        for row in rows:
            json_data.append({"agrupacion": row[0], "status": row[1]})

        cursor.close()
        conexion.close()
        return json_data
    except Exception as e:
        print("Ocurrió un error al actualizar: ", e)
        return False

def FunEditarDistFamilia(items):
    try:
        conexion = conexionBD()
        cursor = conexion.cursor()

        query = " UPDATE AppPlanificacion_distfamilia SET tonLunes = :1, tonMartes = :2, tonMiercoles = :3, tonJueves = :4, tonViernes = :5, tonSabado = :6, tonTotal = :7 " \
                " WHERE id = :8 "

        for i in range(len(items)):
            cursor.execute(query, (items[i]['tonLunes'], items[i]['tonMartes'], items[i]['tonMiercoles'], items[i]['tonJueves'], items[i]['tonViernes'], items[i]['tonSabado'], items[i]['tonTotal'], items[i]['id']))
            print("se actualizo", items[i]["familia"])
        conexion.commit()

        query2 = " select " \
                "    familia, rendimiento,tonLunes, tonMartes, tonMiercoles, tonJueves, tonViernes, tonSabado, tonTotal " \
                " from " \
                "     AppPlanificacion_distfamilia "

        cursor.execute(query2)
        rows = cursor.fetchall()
        json_data = list([])
        
        for row in rows:
            json_data.append({"familia": row[0], "rendimiento": row[1]})

        cursor.close()
        conexion.close()
        print(json_data)
        return json_data
    except Exception as e:
        print("Ocurrió un error al actualizar: ", e)
        return False

def FunEditarDistComercial(items):
    try:
        conexion = conexionBD()
        cursor = conexion.cursor()

        query = " UPDATE AppPlanificacion_distcomercial SET ventLunes = :1, ventMartes = :2, ventMiercoles = :3, ventJueves = :4, ventViernes = :5, ventSabado = :6, ventTotal = :7, proLunes = :8, proMartes = :9, proMiercoles = :10, proJueves = :11, proViernes = :12, proSabado = :13, proTotal = :14 " \
                " WHERE id = :15 "


        for i in range(len(items)):
            cursor.execute(query, (items[i]['ventLunes'], items[i]['ventMartes'], items[i]['ventMiercoles'], items[i]['ventJueves'], items[i]['ventViernes'], items[i]['ventSabado'], items[i]['ventTotal'], items[i]['proLunes'], items[i]['proMartes'], items[i]['proMiercoles'], items[i]['proJueves'], items[i]['proViernes'], items[i]['proSabado'], items[i]['proTotal'], items[i]['id']))
        conexion.commit()

        query2 = " select " \
                "    nombre, ventLunes, ventMartes, ventMiercoles, ventJueves, ventViernes, ventSabado, ventTotal, proLunes, proMartes, proMiercoles, proJueves, proViernes, proSabado, proTotal " \
                " from " \
                "     AppPlanificacion_distcomercial "

        cursor.execute(query2)
        rows = cursor.fetchall()
        json_data = list([])
        
        for row in rows:
            json_data.append({"nombre": row[0]})

        cursor.close()
        conexion.close()
        print(json_data)
        return json_data
    except Exception as e:
        print("Ocurrió un error al Añadir: ", e)
        return False
