# import psycopg2
# def connect():
#     connection = None
#     try:
#         print("Conexcion con la base de datos")
#         connection=psycopg2.connect(
#             host='localhost',
#             user='postgres',
#             password='postgres',
#             database='Intermoda',
#             client_encoding="UTF8"
#         ) 
#         connection.set_client_encoding('UTF8')
#         # print('Conexion exitosa')
#         var_cur = connection.cursor()

#         print("Database version is - ")
#         var_cur.execute("SELECT version()")

#         version_of_database = var_cur.fetchone()
#         print(version_of_database)

#         var_cur.close()
#         print("Conexion exitosa")
#     except Exception as ex:
#         print(f'Ocurrio un error {ex}') 
#     finally:
#             if connection is not None:
#                 connection.close()
#                 print("Database connection closed.")
                
# if __name__ == "__main__":
#     connect()

import psycopg2

def abrir():
    try:
        conexion = psycopg2.connect(host='localhost',database="intermoda2", user="postgres", password="postgres",client_encoding="UTF8")
        cursor = conexion.cursor()
        cursor.execute("SELECT version()")
        version = cursor.fetchone()
        print(f"PostgreSQL version: {version[0]}")
        cursor.close()
        return conexion
    except Exception as e:
        print(f"Error al abrir la conexión intermoda2: {e}")
        return None

if __name__ == "__main__":
    abrir()


########## error Error al abrir la conexión intermoda2: 'utf-8' codec can't decode byte 0xf3 in position 85: invalid continuation byte

# def abrir():
#         try:
#             conexion = psycopg2.connect(database="intermoda2", user="postgres", password="postgres", client_encoding="UTF8")
#             print("Conexión exitosa")
#             return conexion
#         except Exception as e:
#             print(f"Error al abrir la conexión: {e}")
#             return None
        
# def recuperar_todos():
#         cone = abrir()
#         if cone:
#             # Usar DictCursor para obtener resultados como un diccionario
#             cursor = cone.cursor(cursor_factory=extras.DictCursor)
#             try:
#                 sql = "SELECT version()"
#                 cursor.execute(sql)
#                 # Convertir las cadenas a UTF-8
#                 return [{key: str(value).encode('utf-8').decode('utf-8', 'ignore') for key, value in fila.items()} for fila in cursor.fetchall()]
#             except Exception as e:
#                 print(f"Error al recuperar datos: {e}")
#                 return None
#             finally:
#                 cursor.close()
#                 cone.close()
#         else:
#             print("No se pudo establecer la conexión.")
#             return None
        
# if __name__ == "__main__":
#     abrir()