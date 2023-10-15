from .user import User


class Tutor(User):
    def __init__(self, cedula, contrasena, datos=None):
        super().__init__(cedula, contrasena, datos)
