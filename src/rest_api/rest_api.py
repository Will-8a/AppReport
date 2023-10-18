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

    def create_usuario_tutor(self, mysql, current_user, request_cliente):
        # Verifica que el usuario no sea anonimo
        if current_user.is_anonymous:
            return self.usuario_anonimo()

        # Verifica que el usuario es administrador
        if current_user.tipo_de_usuario != 'ADMINISTRADOR':
            return self.usuario_no_autorizado()

        # Variable utilizada para levantar un error de campo faltante
        error_ocurrido = False
        message = ''
        error_type = ''

        # Verificar que los campos requeridos esten en la solicitud
        if request_cliente.get('cedula_tutor') is None:
            error_ocurrido = True
            message = 'Debe especificar la cedula del tutor'
            error_type = 'CEDULA_ESTUDIANTE_NOT_SPECIFIED'

        elif request_cliente.get('primer_nombre') is None:
            error_ocurrido = True
            message = 'Debe especificar el primer nombre del tutor'
            error_type = 'PRIMER_NOMBRE_ESTUDIANTE_NOT_SPECIFIED'

        elif request_cliente.get('primer_apellido') is None:
            error_ocurrido = True
            message = 'Debe especificar el primer apellido del tutor'
            error_type = 'PRIMER_APELLIDO_ESTUDIANTE_NOT_SPECIFIED'

        elif request_cliente.get('e_mail') is None:
            error_ocurrido = True
            message = 'Debe especificar el e_mail del tutor'
            error_type = 'E_MAIL_ESTUDIANTE_NOT_SPECIFIED'

        elif request_cliente.get('contrasena') is None:
            error_ocurrido = True
            message = 'Debe especificar la contrasena del tutor'
            error_type = 'CONTRASENA_ESTUDIANTE_NOT_SPECIFIED'

        # Verificar si ocurrio un error y devolver json con la respuesta
        if error_ocurrido:
            data = responses.campo_faltante(message, error_type)
            return jsonify(data)

        # Verificar campos opcionales en la
        # solicitud (nombre2 y segundo apellido)
        segundo_nombre = ''
        segundo_apellido = ''
        if request_cliente.get('segundo_nombre') is not None:
            segundo_nombre = request_cliente.get('segundo_nombre')

        if request_cliente.get('segundo_apellido') is not None:
            segundo_apellido = request_cliente.get('segundo_apellido')

        # Diccionario con los datos del usuario estudiante
        datos_usuario = {
            'cedula': request_cliente.get('cedula_tutor'),
            'nombre_1': request_cliente.get('primer_nombre'),
            'nombre_2': segundo_nombre,
            'apellido_paterno': request_cliente.get('primer_apellido'),
            'apellido_materno': segundo_apellido,
            'e_mail': request_cliente.get('e_mail'),
            'contrasena': request_cliente.get('contrasena'),
            'tipo_de_usuario': 'TUTOR'
        }

        # Se ejecuta la funcion para guardar al usuario en base de datos
        guardado_en_db = current_user.create_usuario_tutor(
            mysql=mysql,
            datos=datos_usuario
        )

        respuesta_api = {}

        if guardado_en_db:
            respuesta_api = responses.usuario_guardado_en_base_de_datos(
                tipo_de_usuario='TUTOR'
            )
        else:
            respuesta_api = responses.error_interno()

        return jsonify(respuesta_api)

    def read_usuario_estudiante(self, mysql, current_user, request_cliente):
        # Verifica que el usuario no sea anonimo
        if current_user.is_anonymous:
            return self.usuario_anonimo()

        # Verifica que el usuario es administrador
        if current_user.tipo_de_usuario != 'ADMINISTRADOR':
            return self.usuario_no_autorizado()

        if request_cliente.get('cedula_estudiante') is None:
            message = 'Debe especificar la cedula del estudiante'
            error_type = 'CEDULA_ESTUDIANTE_NOT_SPECIFIED'
            return self.campo_faltante(
                message=message,
                error_type=error_type
            )

        respuesta_api = current_user.read_usuario_estudiante(
            mysql=mysql,
            cedula=request_cliente.get('cedula_estudiante')
        )
        return jsonify(respuesta_api)

    def read_usuario_tutor(self, mysql, current_user, request_cliente):
        # Verifica que el usuario no sea anonimo
        if current_user.is_anonymous:
            return self.usuario_anonimo()

        # Verifica que el usuario es administrador
        if current_user.tipo_de_usuario != 'ADMINISTRADOR':
            return self.usuario_no_autorizado()

        if request_cliente.get('cedula_tutor') is None:
            message = 'Debe especificar la cedula del tutor'
            error_type = 'CEDULA_TUTOR_NOT_SPECIFIED'
            data = responses.campo_faltante(
                message,
                error_type
            )
            return jsonify(data)

        data = current_user.read_usuario_tutor(
            mysql=mysql,
            cedula=request_cliente.get('cedula_tutor'),
        )
        return jsonify(data)

    def read_reporte_especifico(self, mysql, current_user, request_cliente):
        # Verifica que el usuario no sea anonimo
        if current_user.is_anonymous:
            return self.usuario_anonimo()

        cedula_estudiante = request_cliente.get('cedula_estudiante')
        numero_reporte = request_cliente.get('numero_reporte')

        if cedula_estudiante == 'undefined' or cedula_estudiante is None:
            message = 'Debe especificar la cedula del estudiante'
            error_type = 'CEDULA_ESTUDIANTE_NOT_SPECIFIED'
            data = responses.campo_faltante(
                message=message,
                error_type=error_type
            )
            return jsonify(data)

        if numero_reporte == 'undefined' or numero_reporte is None:
            message = 'Debe especificar el numero del reporte'
            error_type = 'NUMERO_REPORTE_NOT_SPECIFIED'
            data = responses.campo_faltante(
                message=message,
                error_type=error_type
            )
            return jsonify(data)

        datos = {
            'cedula_estudiante': cedula_estudiante,
            'numero_reporte': numero_reporte
        }

        data = current_user.read_reporte_especifico(
            mysql=mysql,
            datos=datos
        )
        return jsonify(data)

    def read_reportes_estudiante_especifico(self, mysql, current_user, request_cliente):
        # Verifica que el usuario no sea anonimo
        if current_user.is_anonymous:
            return self.usuario_anonimo()

        cedula_estudiante = request_cliente.get('cedula_estudiante')

        if cedula_estudiante == 'undefined' or cedula_estudiante is None:
            message = 'Debe especificar la cedula del estudiante'
            error_type = 'CEDULA_ESTUDIANTE_NOT_SPECIFIED'
            data = responses.campo_faltante(
                message=message,
                error_type=error_type
            )
            return jsonify(data)

        datos = {
            'cedula_estudiante': cedula_estudiante
        }

        data = current_user.read_reportes_estudiante_especifico(
            mysql=mysql,
            datos=datos
        )
        return jsonify(data)

    def read_reportes_tutorados(self, mysql, current_user, request_cliente):
        # Verifica que el usuario no sea anonimo
        if current_user.is_anonymous:
            return self.usuario_anonimo()

        # Verifica que el usuario es tutor
        if current_user.tipo_de_usuario != 'TUTOR':
            return self.usuario_no_autorizado()

        cedula_tutor = request_cliente.get('cedula_tutor')

        if cedula_tutor == 'undefined' or cedula_tutor is None:
            message = 'Debe especificar la cedula del tutor'
            error_type = 'CEDULA_TUTOR_NOT_SPECIFIED'
            return self.campo_faltante(
                message=message,
                error_type=error_type
            )

        datos = {
            'id_tutor': request_cliente.get('cedula_tutor')
        }

        print(datos)

        respuesta_api = current_user.read_reportes_tutorados(
            mysql=mysql,
            datos=datos
        )

        # agregar respuestas para cuando
        # no hay reportes para mostrar
        return jsonify(respuesta_api)

    def update_usuario_estudiante(self, mysql, current_user, request_cliente):
        # Verifica que el usuario no sea anonimo
        if current_user.is_anonymous:
            return self.usuario_anonimo()

        # Verifica que el usuario es administrador
        if current_user.tipo_de_usuario != 'ADMINISTRADOR':
            return self.usuario_no_autorizado()

        if request_cliente.get('cedula_estudiante') is None:
            message = 'Debe especificar la cedula del estudiante'
            error_type = 'CEDULA_ESTUDIANTE_NOT_SPECIFIED'
            return self.campo_faltante(
                message=message,
                error_type=error_type
            )

        cedula_estudiante = request_cliente.get('cedula_estudiante')

        datos_usuario_estudiante = current_user.read_usuario_estudiante(
            mysql=mysql,
            cedula=cedula_estudiante
        )

        # Se comparan los valores los de la base de
        # datos con el request del cliente
        nombre_1 = self.comparar_campos(
            request_cliente.get('primer_nombre'),
            datos_usuario_estudiante.get('nombre_1')
        )

        nombre_2 = self.comparar_campos(
            request_cliente.get('segundo_nombre'),
            datos_usuario_estudiante.get('nombre_2')
        )
        apellido_paterno = self.comparar_campos(
            request_cliente.get('primer_apellido'),
            datos_usuario_estudiante.get('apellido_paterno')
        )
        apellido_materno = self.comparar_campos(
            request_cliente.get('segundo_apellido'),
            datos_usuario_estudiante.get('apellido_materno')
        )
        e_mail = self.comparar_campos(
            request_cliente.get('e_mail'),
            datos_usuario_estudiante.get('e_mail')
        )
        tipo_de_usuario = datos_usuario_estudiante.get('tipo_de_usuario')
        cedula_tutor = self.comparar_campos(
            request_cliente.get('cedula_tutor'),
            datos_usuario_estudiante.get('id_tutor')
        )
        carrera = self.comparar_campos(
            request_cliente.get('carrera'),
            datos_usuario_estudiante.get('carrera')
        )

        # Se crea un nuevo objeto combinando los datos del
        # request del cliente y los datos de la base de datos
        nuevos_datos_usuario = {
            'cedula': cedula_estudiante,
            'nombre_1': nombre_1,
            'nombre_2': nombre_2,
            'apellido_paterno': apellido_paterno,
            'apellido_materno': apellido_materno,
            'e_mail': e_mail,
            'tipo_de_usuario': tipo_de_usuario,
            'cedula_tutor': cedula_tutor,
            'carrera': carrera
        }

        actualizado_en_db = current_user.update_usuario_estudiante(
            mysql=mysql,
            datos=nuevos_datos_usuario
        )

        respuesta_api = {}

        if actualizado_en_db:
            respuesta_api = responses.usuario_actualizado_en_base_de_datos(
                tipo_de_usuario=nuevos_datos_usuario.get('tipo_de_usuario')
            )
        else:
            respuesta_api = responses.error_interno()

        return jsonify(respuesta_api)

    def update_usuario_tutor(self, mysql, current_user, request_cliente):
        # Verifica que el usuario no sea anonimo
        if current_user.is_anonymous:
            return self.usuario_anonimo()

        # Verifica que el usuario es administrador
        if current_user.tipo_de_usuario != 'ADMINISTRADOR':
            return self.usuario_no_autorizado()

        if request_cliente.get('cedula_tutor') is None:
            message = 'Debe especificar la cedula del tutor'
            error_type = 'CEDULA_TUTOR_NOT_SPECIFIED'
            return self.campo_faltante(
                message=message,
                error_type=error_type
            )

        cedula_tutor = request_cliente.get('cedula_tutor')

        datos_usuario_tutor = current_user.read_usuario_tutor(
            mysql=mysql,
            cedula=cedula_tutor
        )

        # Se comparan los valores los de la base de
        # datos con el request del cliente
        nombre_1 = self.comparar_campos(
            request_cliente.get('primer_nombre'),
            datos_usuario_tutor.get('nombre_1')
        )

        nombre_2 = self.comparar_campos(
            request_cliente.get('segundo_nombre'),
            datos_usuario_tutor.get('nombre_2')
        )
        apellido_paterno = self.comparar_campos(
            request_cliente.get('primer_apellido'),
            datos_usuario_tutor.get('apellido_paterno')
        )
        apellido_materno = self.comparar_campos(
            request_cliente.get('segundo_apellido'),
            datos_usuario_tutor.get('apellido_materno')
        )
        e_mail = self.comparar_campos(
            request_cliente.get('e_mail'),
            datos_usuario_tutor.get('e_mail')
        )
        tipo_de_usuario = datos_usuario_tutor.get('tipo_de_usuario')

        # Se crea un nuevo objeto combinando los datos del
        # request del cliente y los datos de la base de datos
        nuevos_datos_usuario = {
            'cedula': cedula_tutor,
            'nombre_1': nombre_1,
            'nombre_2': nombre_2,
            'apellido_paterno': apellido_paterno,
            'apellido_materno': apellido_materno,
            'e_mail': e_mail,
            'tipo_de_usuario': tipo_de_usuario
        }

        actualizado_en_db = current_user.update_usuario_tutor(
            mysql=mysql,
            datos=nuevos_datos_usuario
        )

        respuesta_api = {}

        if actualizado_en_db:
            respuesta_api = responses.usuario_actualizado_en_base_de_datos(
                tipo_de_usuario=nuevos_datos_usuario.get('tipo_de_usuario')
            )
        else:
            respuesta_api = responses.error_interno()

        return jsonify(respuesta_api)

    def update_estatus_reporte(self, mysql, current_user, request_cliente):
        # Verifica que el usuario no sea anonimo
        if current_user.is_anonymous:
            return self.usuario_anonimo()

        # Verifica si el usuario es tipo estudiante
        if current_user.tipo_de_usuario == 'ESTUDIANTE':
            return self.usuario_no_autorizado()

        if request_cliente.get('estatus_reporte') is None:
            message = 'Debe especificar el estatus del reporte'
            error_type = 'ESTATUS_REPORTE_NOT_SPECIFIED'
            data = responses.campo_faltante(
                message=message,
                error_type=error_type
            )
            return jsonify(data)

        if request_cliente.get('id_reporte') is None:
            message = 'Debe especificar el id del reporte'
            error_type = 'ID_REPORTE_NOT_SPECIFIED'
            data = responses.campo_faltante(
                message=message,
                error_type=error_type
            )
            return jsonify(data)

        datos_reporte = {}

        if current_user.tipo_de_usuario == 'TUTOR':
            if request_cliente.get('cedula_tutor') is None:
                message = 'Debe especificar la cedula del tutor'
                error_type = 'CEDULA_TUTOR_NOT_SPECIFIED'
                data = responses.campo_faltante(
                    message=message,
                    error_type=error_type
                )
                return jsonify(data)

            datos_reporte = {
                'estatus': request_cliente.get('estatus_reporte'),
                'id_reporte': request_cliente.get('id_reporte'),
                'cedula_tutor': request_cliente.get('cedula_tutor')
            }
        else:
            datos_reporte = {
                'id_reporte': request_cliente.get('id_reporte'),
                'estatus': request_cliente.get('estatus_reporte')
            }

        actualizado_en_db = current_user.update_estatus_reporte(
            mysql=mysql,
            datos=datos_reporte
        )

        respuesta_api = {}

        if actualizado_en_db:
            respuesta_api = responses.estatus_reporte_cambiado(
                id_reporte=datos_reporte.get('id_reporte'),
                estatus_reporte=request_cliente.get('estatus_reporte')
            )
        else:
            respuesta_api = responses.error_interno()

        return jsonify(respuesta_api)

    def delete_usuario_estudiante(self, mysql, current_user, request_cliente):
        # Verifica que el usuario no sea anonimo
        if current_user.is_anonymous:
            return self.usuario_anonimo()

        # Verifica que el usuario es administrador
        if current_user.tipo_de_usuario != 'ADMINISTRADOR':
            return self.usuario_no_autorizado()

        if request_cliente.get('cedula_estudiante') is None:
            message = 'Debe especificar la cedula del estudiante'
            error_type = 'CEDULA_ESTUDIANTE_NOT_SPECIFIED'
            return self.campo_faltante(
                message=message,
                error_type=error_type
            )

        cedula_estudiante = request_cliente.get('cedula_estudiante')

        eliminado_en_db = current_user.delete_usuario_estudiante(
            mysql=mysql,
            cedula=cedula_estudiante
        )

        respuesta_api = {}

        if eliminado_en_db:
            respuesta_api = responses.usuario_eliminado_en_base_de_datos(
                cedula=cedula_estudiante
            )
        else:
            respuesta_api = responses.error_interno()

        return jsonify(respuesta_api)

    def delete_usuario_tutor(self, mysql, current_user, request_cliente):
        # Verifica que el usuario no sea anonimo
        if current_user.is_anonymous:
            return self.usuario_anonimo()

        # Verifica que el usuario es administrador
        if current_user.tipo_de_usuario != 'ADMINISTRADOR':
            return self.usuario_no_autorizado()

        if request_cliente.get('cedula_tutor') is None:
            message = 'Debe especificar la cedula del tutor'
            error_type = 'CEDULA_TUTOR_NOT_SPECIFIED'
            return self.campo_faltante(
                message=message,
                error_type=error_type
            )

        cedula_tutor = request_cliente.get('cedula_tutor')

        eliminado_en_db = current_user.delete_usuario_tutor(
            mysql=mysql,
            cedula=cedula_tutor
        )

        respuesta_api = {}

        if eliminado_en_db:
            respuesta_api = responses.usuario_eliminado_en_base_de_datos(
                cedula=cedula_tutor
            )
        else:
            respuesta_api = responses.error_interno()

        return respuesta_api
