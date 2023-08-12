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
