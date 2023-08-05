from werkzeug.security import check_password_hash
from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, cedula, contrasena, datos=None):
        self.cedula = cedula
        self.contrasena = contrasena

        if datos is not None:
            self.nombre_1 = datos.get('nombre_1')
            self.nombre_2 = datos.get('nombre_2')
            self.apellido_paterno = datos.get('apellido_paterno')
            self.apellido_materno = datos.get('apellido_materno')
            self.e_mail = datos.get('e_mail')
            self.tipo_de_usuario = datos.get('tipo_de_usuario')

    def get_id(self):
        return self.cedula

    @classmethod
    def check_password(self, hashed_password, contrasena):
        return check_password_hash(hashed_password, contrasena)
