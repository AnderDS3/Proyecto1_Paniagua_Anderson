"""
test_fracciones.py

Suite de pruebas para la clase Fraccion usando unittest.

Este archivo verifica que las operaciones aritméticas básicas
(suma, resta, multiplicación, división y simplificación) funcionen
correctamente en la clase Fraccion.
"""

import sys  # Nos permite modificar la lista de carpetas donde Python busca módulos
import os   # Nos permite construir rutas de carpetas y archivos
import unittest  # Framework de Python para crear y ejecutar tests automáticamente

# Python busca módulos solo en la carpeta donde está el archivo que ejecutas.
# Como estamos en 'tests/', no puede ver la carpeta 'src/' que está arriba.
# Estas 3 líneas le dicen a Python: "también busca módulos en la carpeta raíz".
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importamos las dos clases que vamos a probar
from src.models.model import Fraccion, DataModel


class TestFraccion(unittest.TestCase):
    """Pruebas para la clase Fraccion."""

    def test_suma(self):
        """1/2 + 1/2 debe dar 1/1."""
        f1 = Fraccion(1, 2)
        f2 = Fraccion(1, 2)
        resultado = f1.sumar(f2)
        self.assertEqual(str(resultado), "1/1")

    def test_resta(self):
        """3/4 - 1/4 debe dar 1/2."""
        f1 = Fraccion(3, 4)
        f2 = Fraccion(1, 4)
        resultado = f1.restar(f2)
        self.assertEqual(str(resultado), "1/2")

    def test_multiplicacion(self):
        """2/3 * 3/4 debe dar 1/2."""
        f1 = Fraccion(2, 3)
        f2 = Fraccion(3, 4)
        resultado = f1.multiplicar(f2)
        self.assertEqual(str(resultado), "1/2")

    def test_division(self):
        """1/2 dividido 1/4 debe dar 2/1."""
        f1 = Fraccion(1, 2)
        f2 = Fraccion(1, 4)
        resultado = f1.dividir(f2)
        self.assertEqual(str(resultado), "2/1")

    def test_simplificacion(self):
        """2/4 simplificado debe dar 1/2."""
        f = Fraccion(2, 4)
        f.simplificar()
        self.assertEqual(str(f), "1/2")

    def test_denominador_cero(self):
        """Crear una fracción con denominador 0 debe lanzar ValueError."""
        with self.assertRaises(ValueError):
            Fraccion(1, 0)

    def test_division_entre_cero(self):
        """Dividir entre una fracción con numerador 0 debe lanzar ValueError."""
        with self.assertRaises(ValueError):
            Fraccion(1, 2).dividir(Fraccion(0, 4))


class TestDataModel(unittest.TestCase):
    """Pruebas para la clase DataModel."""

    def setUp(self):
        """
        Se ejecuta automáticamente antes de cada test.
        Crea un modelo con 3 fracciones listas para usar.
        """
        self.model = DataModel()
        self.model.add_fraccion(Fraccion(1, 4))  # la más pequeña
        self.model.add_fraccion(Fraccion(3, 4))  # la más grande
        self.model.add_fraccion(Fraccion(1, 2))  # la del medio

    def test_mayor_fraccion(self):
        """La fracción mayor de [1/4, 3/4, 1/2] debe ser 3/4."""
        resultado = self.model.mayor_fraccion()
        self.assertEqual(str(resultado), "3/4")

    def test_menor_fraccion(self):
        """La fracción menor de [1/4, 3/4, 1/2] debe ser 1/4."""
        resultado = self.model.menor_fraccion()
        self.assertEqual(str(resultado), "1/4")

    def test_limpiar(self):
        """Después de limpiar, la lista debe estar vacía."""
        self.model.clear()
        self.assertEqual(self.model.get_all(), [])


if __name__ == "__main__":
    unittest.main()