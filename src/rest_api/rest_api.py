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
