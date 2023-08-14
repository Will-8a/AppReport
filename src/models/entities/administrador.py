from decimal import Decimal
from .user import User
from werkzeug.security import generate_password_hash


class Administrador(User):
    def __init__(self, cedula, contrasena, datos=None):
        super().__init__(cedula, contrasena, datos)

    def generar_contrasena(self, contrasena):
        # regresa una contrasena hasheada
        return generate_password_hash(contrasena)

    def create_usuario_estudiante(self, mysql, datos):
        datos.update(
            {
                'nombre_1': datos.get('nombre_1').upper(),
                'nombre_2': datos.get('nombre_2').upper(),
                'apellido_paterno': datos.get('apellido_paterno').upper(),
                'apellido_materno': datos.get('apellido_materno').upper(),
                'e_mail': datos.get('e_mail').upper(),
                'contrasena': self.generar_contrasena(datos.get('contrasena')),
                'tipo_de_usuario': datos.get('tipo_de_usuario').upper(),
                'carrera': datos.get('carrera').upper()
            }
        )
        tupla_datos = tuple(datos.values())
        try:
            cursor = mysql.connection.cursor()
            # Llamar al procedimiento almacenado
            cursor.callproc(
                'create_usuario_estudiante',
                tupla_datos)
            mysql.connection.commit()
        except Exception as e:
            # Revertir los cambios si se produce un error
            mysql.connection.rollback()
            print(str(e))
            return False
        finally:
            # Cerrar el cursor
            cursor.close()
        # Regresa True si se realizaron los cambios correctamente
        # en la base de datos
        return True

    def create_usuario_tutor(self, mysql, datos):
        datos.update(
            {
                'nombre_1': datos.get('nombre_1').upper(),
                'nombre_2': datos.get('nombre_2').upper(),
                'apellido_paterno': datos.get('apellido_paterno').upper(),
                'apellido_materno': datos.get('apellido_materno').upper(),
                'e_mail': datos.get('e_mail').upper(),
                'contrasena': self.generar_contrasena(datos.get('contrasena')),
                'tipo_de_usuario': datos.get('tipo_de_usuario').upper()
            }
        )
        tupla_datos = tuple(datos.values())
        try:
            cursor = mysql.connection.cursor()

            # Llamar al procedimiento almacenado
            cursor.callproc(
                'create_usuario_tutor',
                tupla_datos
            )
            mysql.connection.commit()
        except Exception as e:
            mysql.connection.rollback()
            print(str(e))
            raise False
        finally:
            # cerrar el cursor
            cursor.close()
        # Regresa True si se realizaron los cambios
        # correctamente en la base de datos
        return True

    def read_usuario_estudiante(self, mysql, cedula):
        try:
            cursor = mysql.connection.cursor()
            cursor.callproc(
                'read_usuario_estudiante',
                (cedula, )
            )
            result = cursor.fetchone()
            if result is None:
                return None
            else:
                informacion_usuario_estudiante = {
                    'cedula': result[0],
                    'nombre_1': result[1],
                    'nombre_2': result[2],
                    'apellido_paterno': result[3],
                    'apellido_materno': result[4],
                    'e_mail': result[5],
                    'tipo_de_usuario': result[7],
                    'id_tutor': result[8],
                    'carrera': result[9],
                    'cantidad_reportes': result[10],
                    'horas_acumuladas': Decimal(result[11])
                }
                return informacion_usuario_estudiante
        except Exception as e:
            print(str(e))
            return None
        finally:
            cursor.close()

    def update_usuario_estudiante(self, mysql, datos):
        datos.update(
            {
                'nombre_1': datos.get('nombre_1').upper(),
                'nombre_2': datos.get('nombre_2').upper(),
                'apellido_paterno': datos.get('apellido_paterno').upper(),
                'apellido_materno': datos.get('apellido_materno').upper(),
                'e_mail': datos.get('e_mail').upper(),
                'tipo_de_usuario': datos.get('tipo_de_usuario').upper(),
                'carrera': datos.get('carrera').upper()
            }
        )
        tupla_datos = tuple(datos.values())
        try:
            cursor = mysql.connection.cursor()

            cursor.callproc(
                'update_usuario_estudiante',
                tupla_datos
            )

            mysql.connection.commit()
        except Exception as e:
            mysql.connection.rollback()
            print(str(e))
            return False
        finally:
            cursor.close()

        # Regresa True si se realizaron los cambios correctamente
        # en la base de datos
        return True

    def delete_usuario_estudiante(self, mysql, cedula):
        try:
            cursor = mysql.connection.cursor()
            cursor.callproc(
                'delete_usuario_estudiante',
                (cedula, )
            )
            mysql.connection.commit()
        except Exception as e:
            mysql.connection.rollback()
            print(str(e))
            return False
        finally:
            cursor.close()
        # Regresa True si se realizaron los cambios
        # correctamente en la base de datos
        return True
