# AppReport

## AppReport API

### Agregar estudiante [/api/agregar_estudiante]

#### Agregar un nuevo estudiante a la base de datos [POST]

Este endpoint permite al administrador agregar un nuevo estudiante a la base de datos.

```json
{
    "cedula_estudiante": 123456789,
    "primer_nombre": "John",
    "segundo_nombre": "Doe",
    "primer_apellido": "Smith",
    "segundo_apellido": "Johnson",
    "e_mail": "john.doe@example.com",
    "contrasena": "jd12345",
    "cedula_tutor": 987654321,
    "carrera": "INF"
}
```

Los parámetros `segundo nombre` y `segundo apellido` son opcionales, la solicitud de creación de estudiante se realizara sin esos parámetros.

#### Respuesta usuario estudiante

Cuando se ha guardado correctamente al estudiante en la base de datos.

```json
{
    "status": true,
    "response": {
        "message": "Nuevo usuario estudiante guardado",
        "type": "NEW_USER_ESTUDIANTE_SAVED_IN_DATABASE"
    }
}
```

### Agregar Tutor [/api/agregar_tutor]

#### Agregar un nuevo tutor a la base de datos [POST]

Este endpoint permite al administrador agregar un nuevo tutor a la base de datos.

```json
{
    "cedula_tutor":  123456789,
    "primer_nombre": "John",
    "segundo_nombre": "Doe",
    "primer_apellido": "Smith",
    "segundo_apellido": "Johnson",
    "e_mail": "john.doe@example.com",
    "contrasena": "jd12345"
}
```

Los parámetros `segundo nombre` y `segundo apellido` son opcionales, la solicitud de creación de usuario se realizara sin esos parámetros.

#### Respuestas usuario tutor guardado

Cuando el nuevo tutor se ha guardado correctamente en la base de datos.

```json
{
    "status": true,
    "response": {
        "message": "Nuevo usuario tutor guardado",
        "type": "NEW_USER_TUTOR_SAVED_IN_DATABASE"
    }
}
```

### Nuevo reporte [/api/nuevo_reporte] 

#### Crea un reporte [POST]

Permite a los usuarios estudiantes crear reportes en la base de datos.

```json
{
    "cedula_estudiante": 123456789,
    "cedula_tutor": 987654321,
    "numero_reporte": 1,
    "horas_reporte": 4,
    "resumen_domingo": "",
    "resumen_lunes": "",
    "resumen_martes": "",
    "resumen_miercoles": "",
    "resumen_jueves": "",
    "resumen_viernes": ""
}
```

Los parámetros `resumen_xxxxx` son opcionales (Sea xxxxx el día correspondiente), la solicitud de creación de reporte se realizara sin esos parámetros.

#### Respuesta reporte guardado en la base de datos

Cuando se ha guardado correctamente el reporte en la base de datos.

```json
{
    "status": true,
    "response": {
        "message": "Reporte guardado exitosamente",
        "type": "REPORTE_SAVED_IN_DATABASE"
    }
}
```

### Leer datos estudiante [/api/leer_estudiante]

#### Leer los datos de un estudiante en la base de datos [GET]

Este endpoint permite al administrador leer los datos guardados en la base de datos de un estudiante.

```json
{
    "cedula_estudiante": 123456789
}
```

#### Respuestas datos del usuario

Se envía un json con los datos existentes del usuario en la base de datos.

```json
{
    "nombre_1": "JONH",
    "nombre_2": "DOE",
    "apellido_materno": "SMITH",
    "apellido_paterno": "JOHNSON",
    "cantidad_reportes": 1,
    "carrera": "INF",
    "cedula": "123456789",
    "e_mail": "john.doe@example.com",
    "horas_acumuladas": "5.00",
    "id_tutor": "987654321",
    "tipo_de_usuario": "ESTUDIANTE"
}
```

### Leer datos tutor [/api/leer_tutor]

#### Leer los datos de un tutor en la base de datos [GET]

Este endpoint permite al administrado leer los datos guardados en la base de datos de un tutor.

```json
{
    "cedula_tutor": 987654321
}
```

#### Respuesta datos del usuario

Se envía un json con los datos existentes del usuario en la base de datos.

```json
{
    "cedula": "987654321",
    "nombre_1": "JONH",
    "nombre_2": "DOE",
    "apellido_paterno": "JOHNSON",
    "apellido_materno": "SMITH",
    "e_mail": "john.doe@example.com",
    "tipo_de_usuario": "ESTUDIANTE"
}
```

### Leer datos reporte [/api/leer_reporte]

#### Leer los datos de un reporte en la base de datos [GET]

Permite a todos los usuarios leer los datos guardados en la base de datos de un reporte semanal.

```json
{
    "cedula_estudiante": 123456789,
    "numero_reporte": 1
}
``` 

#### Respuesta con los datos del reporte

```json
{
    "id_reporte": 1,
    "numero_reporte": 1,
    "horas_reporte": 0.0,
    "aprobacion_coordinador": "SIN APROBAR",
    "aprobacion_tutor": "SIN APROBAR",
    "resumen_domingo": "",
    "resumen_lunes": "",
    "resumen_martes": "",
    "resumen_miercoles": "",
    "resumen_jueves": "",
    "resumen_viernes": ""
}
```

### Leer reportes estudiante [/api/leer_reportes_estudiante]

#### Leer todos los reportes de un estudiante [GET]

Permite a los usuarios obtener todos los reportes de la base de datos de un estudiante.

```json
{
    "cedula_estudiante": 123456789
}
```

#### Respuesta con la información de los reportes

```json
{
    "reporte_1": {
        "aprobacion_coordinador": "SIN APROBAR",
        "aprobacion_tutor": "SIN APROBAR",
        "horas_reporte": 0.0,
        "id_reporte": 1,
        "id_tutor": "2",
        "numero_reporte": 1,
        "resumen_domingo": "",
        "resumen_lunes": "",
        "resumen_martes": "",
        "resumen_miercoles": "",
        "resumen_jueves": "",
        "resumen_viernes": ""
    },
    "reporte_2": {
        "aprobacion_coordinador": "APROBADO",
        "aprobacion_tutor": "APROBADO",
        "horas_reporte": 7.0,
        "id_reporte": 2,
        "id_tutor": "2",
        "numero_reporte": 2,
        "resumen_domingo": "",
        "resumen_lunes": "",
        "resumen_martes": "",
        "resumen_miercoles": "",
        "resumen_jueves": "",
        "resumen_viernes": ""
    }
}
```

### Leer reportes tutorados [/api/leer_reportes_tutorados]

#### Leer los reportes tutorados [/api/GET]

Permite que un usuario tutor pueda leer todos los reportes que esta tutorando.

```json
{
    "cedula_tutor": 987654321
}
```

#### Respuesta con la información de los reportes

```json
{
    "reporte_1": {
        "aprobacion_coordinador": "SIN APROBAR",
        "aprobacion_tutor": "SIN APROBAR",
        "horas_reporte": 0.0,
        "id_reporte": 1,
        "numero_reporte": 1,
        "resumen_domingo": "",
        "resumen_jueves": "",
        "resumen_lunes": "",
        "resumen_martes": "",
        "resumen_miercoles": "",
        "resumen_viernes": ""
    },
    "reporte_2": {
        "aprobacion_coordinador": "APROBADO",
        "aprobacion_tutor": "APROBADO",
        "horas_reporte": 7.0,
        "id_reporte": 2,
        "numero_reporte": 2,
        "resumen_domingo": "",
        "resumen_jueves": "",
        "resumen_lunes": "",
        "resumen_martes": "",
        "resumen_miercoles": "",
        "resumen_viernes": ""
    },
    "reporte_3": {
        "aprobacion_coordinador": "APROBADO",
        "aprobacion_tutor": "APROBADO",
        "horas_reporte": 7.0,
        "id_reporte": 3,
        "numero_reporte": 1,
        "resumen_domingo": "",
        "resumen_jueves": "",
        "resumen_lunes": "",
        "resumen_martes": "",
        "resumen_miercoles": "",
        "resumen_viernes": ""
    }
}
```

### Actualizar información de un estudiante [/api/actualizar_estudiante]

#### Actualizar la información de un estudiante en la base de datos [PUT]

Permite al administrador actualizar la información en la base de datos de un estudiante.

```json
{
    "cedula_estudiante": 123456789,
    "primer_nombre": "John",
    "segundo_nombre": "DOE",
    "primer_apellido": "Smith",
    "segundo_apellido": "Johnson",
    "e_mail": "john.doe@example.com",
    "cedula_tutor": 987654321,
    "carrera": "ADM_E"
}
```

Solamente el parámetro cedula_estudiante es obligatorio la solicitud de actualización de estudiante se realizara sin los demás parámetros.

#### Respuesta sobre la actualización de la información

```json
{
    "status": true,
    "response": {
        "message": "Usuario estudiante actualizado en base de datos",
        "type": "USER_ESTUDIANTE_UPDATE_IN_DATABASE"
    }
}
```

### Actualizar información de un tutor [/api/actualizar_tutor]

#### Actualizar la información de un tutor en la base de datos [PUT]

Permite al administrador actualizar la información en la base de datos de un tutor.

```json
{
    "cedula_tutor": 987654321,
    "primer_nombre": "John",
    "segundo_nombre": "DOE",
    "primer_apellido": "Smith",
    "segundo_apellido": "Johnson",
    "e_mail": "john.doe@example.com",
}
```

Solamente el parámetro cedula_tutor es obligatorio la solicitud de actualización de tutor se puede realizar sin los demás parámetros.

#### Respuesta sobre la actualización de la información

```json
{
    "status": true,
    "response": {
        "message": "Usuario tutor actualizado en base de datos",
        "type": "USER_TUTOR_UPDATE_IN_DATABASE"
    }
}
```

### Actualizar estatus reporte [/api/actualizar_tutor]

#### Actualizar el estatus de un reporte en la base de datos[PUT]

Permite al administrador y a los tutores aprobar o desaprobar un reporte en la base de datos.

```json
{
    "estatus_reporte": "APROBADO",
    "id_reporte": 1
}
```

Para que un usuario tutor pueda usar esta función tiene que especificar su cedula en la solicitud.

```json
{
    "estatus_reporte": "APROBADO",
    "id_reporte": 1,
    "cedula_tutor": 987654321
}
```
#### Respuesta sobre el estatus del reporte cambiado

```json
{
    "status": true,
    "response": {
        "message": "Reporte 1 XXXX exitosamente",
        "type": "REPORTE_1_STATUS_UPDATE_IN_DATABASE"
    }
}
```

`XXXX` es el estatus cambiado en la base de datos `Aprobado` o `desaporbado`

### Actualizar reporte [/api/actualizar_reporte]

#### Actualiza la informacion de un reporte [PUT]

Permite a los usuarios estudiantes actualizar reportes en la base de datos.

```json
{
    "id_reporte": 1,
    "cedula_estudiante": 123456789,
    "horas_reporte": 4,
    "resumen_domingo": "",
    "resumen_lunes": "",
    "resumen_martes": "",
    "resumen_miercoles": "",
    "resumen_jueves": "",
    "resumen_viernes": ""
}
```

Los parámetros `resumen_xxxxx` son opcionales, la solicitud de creación de reporte se realizara sin esos parámetros.

#### Respuesta reporte guardado en la base de datos

Cuando se ha guardado correctamente el reporte en la base de datos.

```json
{
    "status": true,
    "response": {
        "message": "Reporte guardado exitosamente",
        "type": "REPORTE_SAVED_IN_DATABASE"
    }
}
```

### Eliminar estudiante [/api/eliminar_estudiante]

#### Elimina a un estudiante [DELETE]

Permite al administrador eliminar un estudiante y su información de la base de datos.

```json
{
    "cedula_estudiante": 123456789
}
```

#### Respuesta usuario eliminado en la base de datos

Cuando se ha guardado correctamente el reporte en la base de datos.

```json
{
    "status": true,
    "response": {
        "message": "Usuario estudiante eliminado en base de datos",
        "type": "USER_ESTUDIANTE_UPDATE_IN_DATABASE"
    }
}
```

### Eliminar tutor [/api/eliminar_tutor]

#### Elimina a un tutor [DELETE]

Permite al administrador eliminar un tutor y su información de la base de datos.

```json
{
    "cedula_tutor": 987654321
}
```

#### Respuesta usuario eliminado en la base de datos

Cuando se ha guardado correctamente el reporte en la base de datos.

```json
{
    "status": true,
    "response": {
        "message": "Usuario tutor eliminado en base de datos",
        "type": "USER_TUTOR_UPDATE_IN_DATABASE"
    }
}
```


### Otras Respuestas

Además de las respuestas estándar que se deberían recibir por parte del servidor, esta es una lista de las posibles respuestas que puede emitir la API al ocurrir un error.

#### Usuario anónimo

Respuesta para cuando se esta intentado realizar la solicitud y no se ha iniciado sesión.

```json
{
    "status": false,
    "response": {
        "message": "Debe iniciar sesion primero",
        "type": "UNAUTHENTICATED_USER"
    }
}

```

#### Usuario no autorizado

Respuesta para cuando el usuario que esta realizando la solicitud no es administrador.

```json
{
    "status": false,
    "response": {
        "message": "No esta autorizado",
        "type": "ERROR_UNAUTHORIZED_USER"
    }
}
```

#### Campo faltante

Respuesta cuando un campo requerido esta ausente.

```json
{
    "status": false,
    "response": {
        "message": "Debe especificar XXXX",
        "type": "XXXX_NOT_SPECIFIED"
    }
}
```

`XXXX` es el campo que falta en el request.

####  Error interno

Respuesta para cuando ocurre un error en el lado del servidor.

```json
{
    "status": false,
    "response": {
        "message": "Ocurrio un error interno",
        "type": "INTERNAL_ERROR"
    }
}
```
