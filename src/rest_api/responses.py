# Respuesta para cuando el usuario no ha iniciado sesion
def usuario_anonimo():
    '''
    Retorna una respuesta de error cuando un usuario anonimo
    (no autenticado) intenta realizar una accion que requiere
    autenticacion.

    Returns:
    -------
    dict
        Un diccionario que incluye el estado de exito y un sub-diccionario
        'response' con detalles sobre el problema.
    '''
    data = {
        'status': False,
        'response': {
            'message': 'Debe iniciar sesion primero',
            'type': 'UNAUTHENTICATED_USER'
        }
    }
    return data


# Respuesta para cuando el usuario no esta autorizado
def usuario_no_autorizado():
    '''
    Retorna una respuesta de error cuando el tipo de usuario no esta
    autorizado para realizar una accion que requiere un tipo de usuario
    distinto

    Returns:
    -------
        dict
            Un diccionario que incluye el estado de exito y un sub-diccionario
            'response' con detalles sobre el problema.
    '''
    data = {
        'status': False,
        'response': {
            'message': 'No esta autorizado',
            'type': 'ERROR_UNAUTHORIZED_USER'
        }
    }
    return data


# Respuesta para cuando no se especifica un campo necesario
def campo_faltante(message, error_type):
    '''
    Generar una respuesta estandarizada para un caso en que un campo requerido
    este ausente.

    Params:
    -------
    message : str
        Un mensaje descriptivo del problema que se ha encontrado.

    error_type : str
        Una cadena de texto que identifica el tipo de problema que ha causado
        este error.

    Returns:
    -------
    dict
        Un diccionario que incluye el estado de exito y un sub-diccionario
        'response' con detalles sobre el problema.
    '''
    data = {
        'status': False,
        'response': {
            'message': message,
            'type': error_type
        }
    }
    return data


# Respuesta cuando se ha guardado un nuevo usuario en la base de datos
def usuario_guardado_en_base_de_datos(tipo_de_usuario):
    '''
    Retorna una respuesta cuando un nuevo usuario ha sido guardado en
    la base de datos.

    Params:
    -------
    tipo_de_usuario : str
        Una cadena de texto que identifica el tipo de usuario que se ha
        guardado en la base de datos

    Returns:
    -------
    dict
        Diccionario con el estado y la respuesta de la creacion del nuevo
        usuario. El estado es siempre True y la respuesta contiene un mensaje
        indicando que el usuario ha sido guardado y el tipo de respuesta,
        ademas se agrega un espacio para la variable del tipo de usuario

    '''
    data = {
        'status': True,
        'response': {
            'message': 'Nuevo usuario {} guardado'.format(
                tipo_de_usuario.lower()
            ),
            'type': 'NEW_USER_{}_SAVED_IN_DATABASE'.format(
                tipo_de_usuario
            )
        }
    }
    return data


# Respuesta cuando se ha actualizado un usuario en la base de datos
def usuario_actualizado_en_base_de_datos(tipo_de_usuario):
    '''
    Retorna una respuesta cuando un usuario ha sido actualizado en
    la base de datos.

    Params:
    -------
    tipo_de_usuario : str
        Una cadena de texto que identifica el tipo de usuario que se ha
        actualizado en la base de datos

    Returns:
    -------
    dict
        Diccionario con el estado y la respuesta de la actualizacion del
        usuario. El estado es siempre True y la respuesta contiene un mensaje
        indicando que el usuario ha sido actualizado y el tipo de respuesta,
        ademas se agrega un espacio para la variable del tipo de usuario
    '''
    data = {
        'status': True,
        'response': {
            'message': 'Usuario {} actualizado en base de datos'.format(
                tipo_de_usuario.lower()
            ),
            'type': 'USER_{}_UPDATE_IN_DATABASE'.format(
                tipo_de_usuario
            )
        }
    }
    return data


# Respuesta cuando se elimina un usuario de la base de datos
def usuario_eliminado_en_base_de_datos(cedula):
    '''
    Retorna una respuesta cuando un usuario ha sido eliminado en
    la base de datos.

    Params:
    -------
    cedula : str
        Una cadena de texto que identifica el la cedula del usuario
        que se ha eliminado en la base de datos

    Returns:
    -------
    dict
        Diccionario con el estado y la respuesta de la eliminacion del
        usuario. El estado es siempre True y la respuesta contiene un mensaje
        indicando que el usuario ha sido eliminado y el tipo de respuesta,
        ademas se agrega un espacio para la cedula del tipo de usuario
    '''
    data = {
        'status': True,
        'response': {
            'message': 'Usuario {} eliminado en base de datos'.format(
                cedula
            ),
            'type': 'USER_{}_UPDATE_IN_DATABASE'.format(
                cedula
            )
        }
    }
    return data


# respuesta cuando se actualiza un reporte en la base de datos
def estatus_reporte_cambiado(id_reporte, estatus_reporte, status=True):
    '''
    Retorna una respuesta cuando un reporte ha sido actualizado en
    la base de datos.

    Params:
    -------
    id_reporte : str
        Una cadena de texto que funciona como el identificador del
        reporte que se ha actualizado en la base de datos

    estatus_reporte : str
        Una cadena de texto que especifica el estatus del reporte
        actualizado en la base de datos
    Returns:
    -------
    dict
        Diccionario con el estado y la respuesta de la actualizacion del
        estado del reporte es siempre True y la respuesta contiene un mensaje
        indicando el estado ha sido actualizado y el identificador del reporte,
        ademas se agrega espacios para el id del reporte y el estado
    '''
    data = {
        'status': status,
        'response': {
            'message': 'Reporte {} {} exitosamente'.format(
                id_reporte, estatus_reporte.lower()
            ),
            'type': 'REPORTE_{}_STATUS_UPDATE_IN_DATABASE'.format(
                id_reporte
            )
        }
    }
    return data


# Respuesta para cuando ocurrio un error interno
def error_interno():
    '''
    Retorna una respuesta de error cuando ocurre un error
    interno en el programa.

    Returns:
    ------
    dict
        Un diccionario que contiene el estado de la operación y la respuesta
        con el mensaje y el tipo de error.
    '''
    data = {
        'status': False,
        'response': {
            'message': 'Ocurrio un error interno',
            'type': 'INTERNAL_ERROR'
        }
    }
    return data


# Respuesta para cuando se guarda un nuevo reporte
def reporte_guardado():
    '''
    Retorna una respuesta cuando un reporte se ha guardado
    en la base de datos.

    Returns:
    ------
    dict
        Un diccionario que contiene el estado de la operación y la respuesta
        con el mensaje. El estado es siempre True y la respuesta contiene un
        mensaje indicando que el reporte ha sido guardado.
    '''
    data = {
        'status': True,
        'response': {
            'message': 'Reporte guardado exitosamente',
            'type': 'REPORTE_SAVED_IN_DATABASE'
        }
    }
    return data
