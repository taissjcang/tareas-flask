import unittest
from tareas_flask.models.tarea import Tarea


class TestTarea(unittest.TestCase):

    def test_creacion_tarea(self):
        tarea = Tarea(1, "Estudiar para la prueba", 1)

        self.assertEqual(tarea.descripcion, "Estudiar para la prueba")
        self.assertEqual(tarea.usuario_id, 1)


if __name__ == "__main__":
    unittest.main()
