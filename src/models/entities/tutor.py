from .user import User


class Tutor(User):
    def __init__(self, cedula, contrasena, datos=None):
        super().__init__(cedula, contrasena, datos)

    def read_reporte_especifico(self, mysql, datos):
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

    def read_reportes_tutorados(self, mysql, datos):
        tupla_datos = tuple(datos.values())

        try:
            cursor = mysql.connection.cursor()
            cursor.callproc(
                'read_reportes_tutorados',
                tupla_datos
            )
            reportes = {}
            results = cursor.fetchall()
            for result in results:
                id_reporte = result[0]
                reportes.update({
                    'reporte_{}'.format(id_reporte): {
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
                })
            return reportes
        except Exception as e:
            print(str(e))
            return None
        finally:
            cursor.close()

    def read_reportes_estudiante_especifico(self, mysql, datos):
        tupla_datos = tuple(datos.values())

        try:
            cursor = mysql.connection.cursor()
            cursor.callproc(
                'read_reportes_estudiante_especifico',
                tupla_datos
            )
            reportes = {}
            results = cursor.fetchall()
            for result in results:
                id_reporte = result[0]
                reportes.update({
                    'reporte_{}'.format(id_reporte): {
                        'id_reporte': result[0],
                        'id_tutor': result[2],
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
                })
            return reportes
        except Exception as e:
            print(str(e))
            return None
        finally:
            cursor.close()

    def update_estatus_reporte(self, mysql, datos):
        datos.update({
            'estatus': datos.get('estatus').upper()
        })
        tupla_datos = tuple(datos.values())
        try:
            cursor = mysql.connection.cursor()
            cursor.callproc(
                'update_estatus_reporte_tutor',
                tupla_datos
            )
            mysql.connection.commit()
        except Exception as e:
            mysql.connection.rollback()
            print(str(e))
            return False
        finally:
            cursor.close()
        return True
