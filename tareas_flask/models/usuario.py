class Usuario:
    def __init__(self, id, username, es_admin=False):
        self.id = id
        self.username = username
        self.es_admin = es_admin

    def es_administrador(self):
        return self.es_admin


class UsuarioAdmin(Usuario):
    def __init__(self, id, username):
        super().__init__(id, username, True)

    def puede_gestionar_usuarios(self):
        return True
