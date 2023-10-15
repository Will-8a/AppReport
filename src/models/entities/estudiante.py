from .user import User


class Estudiante(User):
    def __init__(self, cedula, contrasena, datos=None):
        super().__init__(cedula, contrasena, datos)

        self.id_tutor = datos.get('id_tutor')
        self.carrera = datos.get('carrera')
        self.cantidad_reportes = datos.get('cantidad_reportes')
        self.horas_acumuladas = datos.get('horas_acumuladas')

    # create reporte
    def create_reporte(self, mysql, datos):
        tupla_datos = tuple(datos.values())
        try:
            cursor = mysql.connection.cursor()
            cursor.callproc(
                'create_nuevo_reporte',
                tupla_datos
            )
            mysql.connection.commit()
            # update usuario estudiante()
            self.update_datos_estudiante(mysql, datos)
            # read usuario estudiante()
            self.read_datos_estudiante(mysql, datos)
        except Exception as e:
            print('a')
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

    # read reporte
    def read_reporte(self, mysql, datos):
        tupla_datos = tuple(datos.values())

        try:
            cursor = mysql.connection.cursor()
            cursor.callproc(
                'read_reporte_especifico',
                tupla_datos
            )
            result = cursor.fetchone()
            if result is None:
                return None
            else:
                informacion_reporte = {
                    'id_reporte': result[0],
                    'numero_reporte': result[3],
                    'horas_reporte': float(result[4]),
                    'aprobacion_tutor': result[5],
                    'aprobacion_coordinador': result[6],
                    'resumen_domingo': result[7],
                    'resumen_lunes': result[8],
                    'resumen_martes': result[9],
                    'resumen_miercoles': result[10],
                    'resumen_jueves': result[11],
                    'resumen_viernes': result[12]
                }
                return informacion_reporte
        except Exception as e:
            print(str(e))
            return None
        finally:
            cursor.close()

    def read_datos_estudiante(self, mysql, datos):
        tupla_datos = (datos.get('cedula_estudiante'), )
        try:
            cursor = mysql.connection.cursor()
            cursor.callproc(
                'read_datos_estudiante',
                (tupla_datos, )
            )
            row = cursor.fetchone()
            if row is None:
                return None
            else:
                self.cantidad_reportes = row[2]
                self.horas_acumuladas = row[3]
        except Exception as e:
            print('b')

            print(str(e))
            return None
        finally:
            cursor.close()

    def update_datos_estudiante(self, mysql, datos):
        tupla_datos = (datos.get('cedula_estudiante'), )
        try:
            cursor = mysql.connection.cursor()
            cursor.callproc(
                'update_datos_estudiante',
                tupla_datos
            )
            mysql.connection.commit()
            return True
        except Exception as e:
            print('c')

            mysql.connection.rollback()
            print(str(e))
            return False
        finally:
            cursor.close()

    # update reporte
    def update_reporte(self, mysql, datos):
        tupla_datos = tuple(datos.values())
        try:
            cursor = mysql.connection.cursor()
            cursor.callproc(
                'update_reporte_especifico',
                tupla_datos
            )
            mysql.connection.commit()
            # update usuario estudiante()
            self.update_datos_estudiante(mysql, datos)
            # read usuario estudiante()
            self.read_datos_estudiante(mysql, datos)
            return True
            # update usuario estudiante()
        except Exception as e:
            print(str(e))
            return False
        finally:
            cursor.close()
