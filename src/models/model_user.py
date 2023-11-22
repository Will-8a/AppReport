from .entities.administrador import Administrador
from .entities.estudiante import Estudiante
from .entities.tutor import Tutor


class ModelUser():
    @classmethod
    def login(self, mysql, user):
        try:
            cursor = mysql.connection.cursor()
            cedula = user.cedula
            cursor.callproc('read_usuario', (cedula, ))
            row = cursor.fetchone()
            if row is not None:
                user_information = {
                    'cedula': row[0],
                    'nombre_1': row[1],
                    'nombre_2': row[2],
                    'apellido_paterno': row[3],
                    'apellido_materno': row[4],
                    'login': '1',
                    'e_mail': row[5],
                    'contrasena': row[6],
                    'tipo_de_usuario': row[7]
                }

                if user_information.get('tipo_de_usuario') == 'ADMINISTRADOR':
                    user = Administrador(
                        cedula=row[0],
                        contrasena=Administrador.check_password(
                            hashed_password=row[6],
                            contrasena=user.contrasena),
                        datos=user_information)
                elif user_information.get('tipo_de_usuario') == 'ESTUDIANTE':
                    cursor.close()
                    cursor = mysql.connection.cursor()
                    cursor.callproc(
                        'read_datos_estudiante',
                        (cedula, )
                    )
                    row = cursor.fetchone()
                    user_information.update({
                        'id_tutor': row[0],
                        'carrera': row[1],
                        'cantidad_reportes': row[2],
                        'horas_acumuladas': row[3]
                    })

                    user = Estudiante(
                        cedula=user_information.get('cedula'),
                        contrasena=Estudiante.check_password(
                            hashed_password=user_information.get('contrasena'),
                            contrasena=user.contrasena
                        ),
                        datos=user_information
                    )
                elif user_information.get('tipo_de_usuario') == 'TUTOR':
                    user = Tutor(
                        cedula=row[0],
                        contrasena=Tutor.check_password(
                            hashed_password=row[6],
                            contrasena=user.contrasena
                        ),
                        datos=user_information
                    )
                return user
            return None
        except Exception as e:
            raise Exception(e)
        finally:
            cursor.close()

    @classmethod
    def get_by_cedula(self, mysql, cedula):
        try:
            cursor = mysql.connection.cursor()
            cursor.callproc('read_usuario_except_password', (cedula, ))
            row = cursor.fetchone()
            if row is not None:
                user_information = {
                    'cedula': row[0],
                    'nombre_1': row[1],
                    'nombre_2': row[2],
                    'apellido_paterno': row[3],
                    'apellido_materno': row[4],
                    'login': '0',
                    'e_mail': row[5],
                    'tipo_de_usuario': row[6]
                }

                if user_information.get('tipo_de_usuario') == 'ADMINISTRADOR':
                    usuario_logeado = Administrador(
                        cedula=row[0],
                        contrasena=None,
                        datos=user_information)
                elif user_information.get('tipo_de_usuario') == 'ESTUDIANTE':
                    cursor.close()
                    cursor = mysql.connection.cursor()
                    cursor.callproc(
                        'read_datos_estudiante',
                        (cedula, )
                    )
                    row = cursor.fetchone()
                    user_information.update({
                        'id_tutor': row[0],
                        'carrera': row[1],
                        'cantidad_reportes': row[2],
                        'horas_acumuladas': row[3]
                    })

                    usuario_logeado = Estudiante(
                        cedula=user_information.get('cedula'),
                        contrasena=None,
                        datos=user_information
                    )
                elif user_information.get('tipo_de_usuario') == 'TUTOR':
                    usuario_logeado = Tutor(
                        cedula=row[0],
                        contrasena=None,
                        datos=user_information
                    )
                return usuario_logeado
            return None
        except Exception as e:
            raise Exception(e)
        finally:
            cursor.close()
