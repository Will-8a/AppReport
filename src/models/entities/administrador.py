from .user import User


class Administrador(User):
    def __init__(self, cedula, contrasena, datos=None):
        super().__init__(cedula, contrasena, datos)
