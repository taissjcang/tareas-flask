class Tarea:
    def __init__(self, id, descripcion, usuario_id):
        self.id = id
        self.descripcion = descripcion
        self.usuario_id = usuario_id

    def to_dict(self):
        return {
            "id": self.id,
            "descripcion": self.descripcion
        }
