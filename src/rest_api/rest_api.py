from flask import jsonify
from . import responses


class RestApi:
    def __init__(self):
        pass

    def usuario_anonimo(self):
        respuesta_api = responses.usuario_anonimo()
        return jsonify(respuesta_api)

    def usuario_no_autorizado(self):
        respuesta_api = responses.usuario_no_autorizado()
        return jsonify(respuesta_api)

    def campo_faltante(self, message, error_type):
        respuesta_api = responses.campo_faltante(
            message=message,
            error_type=error_type
        )
        return jsonify(respuesta_api)

    # Funcion para comparar los valores de la base
    # de datos y del request del cliente
    def comparar_campos(self, request_value, database_value):
        if request_value is not None:
            if request_value != database_value:
                return request_value
        return database_value

    def create_usuario_estudiante(self, mysql, current_user, request_cliente):
        # Verifica que el usuario no sea anonimo
        if current_user.is_anonymous:
            return self.usuario_anonimo()

        # Verifica que el usuario es administrador
        if current_user.tipo_de_usuario != 'ADMINISTRADOR':
            return self.usuario_no_autorizado()

        error_ocurrido = False
        message = ''
        error_type = ''

        # Verificar los campos requeridos en la solicitud
        if request_cliente.get('cedula_estudiante') is None:
            error_ocurrido = True
            message = 'Debe especificar la cedula del estudiante'
            error_type = 'CEDULA_ESTUDIANTE_NOT_SPECIFIED'

        elif request_cliente.get('primer_nombre') is None:
            error_ocurrido = True
            message = 'Debe especificar el primer nombre del estudiante'
            error_type = 'PRIMER_NOMBRE_ESTUDIANTE_NOT_SPECIFIED'

        elif request_cliente.get('primer_apellido') is None:
            error_ocurrido = True
            message = 'Debe especificar el primer apellido del estudiante'
            error_type = 'PRIMER_APELLIDO_ESTUDIANTE_NOT_SPECIFIED'

        elif request_cliente.get('e_mail') is None:
            error_ocurrido = True
            message = 'Debe especificar el e_mail del estudiante'
            error_type = 'E_MAIL_ESTUDIANTE_NOT_SPECIFIED'

        elif request_cliente.get('contrasena') is None:
            error_ocurrido = True
            message = 'Debe especificar la contrasena del estudiante'
            error_type = 'CONTRASENA_ESTUDIANTE_NOT_SPECIFIED'

        elif request_cliente.get('cedula_tutor') is None:
            error_ocurrido = True
            message = 'Debe especificar la cedula del tutor del estudiante'
            error_type = 'CEDULA_TUTOR_NOT_SPECIFIED'

        elif request_cliente.get('carrera') is None:
            error_ocurrido = True
            message = 'Debe especificar la carrera del estudiante'
            error_type = 'CARRERA_ESTUDIANTE_NOT_SPECIFIED'

        if error_ocurrido:
            return self.campo_faltante(
                message=message,
                error_type=error_type
            )

        # Verificar campos opcionales en la
        # solicitud (nombre_2 y apellido_materno)
        segundo_nombre = ''
        segundo_apellido = ''

        if request_cliente.get('segundo_nombre') is not None:
            segundo_nombre = request_cliente.get('segundo_nombre')

        if request_cliente.get('segundo_apellido') is not None:
            segundo_apellido = request_cliente.get('segundo_apellido')

        # Diccionario con los datos del usuario estudiante
        datos_usuario = {
            'cedula': request_cliente.get('cedula_estudiante'),
            'nombre_1': request_cliente.get('primer_nombre'),
            'nombre_2': segundo_nombre,
            'apellido_paterno': request_cliente.get('primer_apellido'),
            'apellido_materno': segundo_apellido,
            'e_mail': request_cliente.get('e_mail'),
            'contrasena': request_cliente.get('contrasena'),
            'tipo_de_usuario': 'ESTUDIANTE',
            'cedula_tutor': request_cliente.get('cedula_tutor'),
            'carrera': request_cliente.get('carrera'),
            'cantidad_reportes': 0,
            'horas_acumuladas': 0
        }

        # Se ejecuta la funcion para guardar al usuario en base de datos
        guardado_en_db = current_user.create_usuario_estudiante(
            mysql=mysql,
            datos=datos_usuario
        )

        respuesta_api = {}

        if guardado_en_db:
            respuesta_api = responses.usuario_guardado_en_base_de_datos(
                tipo_de_usuario='ESTUDIANTE'
            )
        else:
            respuesta_api = responses.error_interno()

        return jsonify(respuesta_api)
