"""
Se importa la clase Fraccion desde el modelo para realizar
operaciones matemáticas.
"""
from models.model import Fraccion


class Controller:
    """
    Controlador de la aplicación.

    Se encarga de conectar la vista con el modelo,
    gestionar las fracciones y realizar operaciones.
    """

    def __init__(self, model, view):
        """
        Inicializa el controlador.

        Parámetros:
            model: modelo de datos
            view: interfaz gráfica
        """
        self.model = model
        self.view = view

        # ===== Agregar Fracciones =====
        self.view.comando_agregar = self.handle_button_click

        # ===== Operaciones =====
        self.view.comando_suma = self.sumar_todo
        self.view.comando_resta = self.restar_todo
        self.view.comando_multiplicacion = self.multiplicar_todo
        self.view.comando_division = self.dividir_todo
        self.view.comando_limpiar = self.limpiar_lista

    def handle_button_click(self):
        """
        Método base del botón.

        Ahora se usa para AGREGAR fracciones al modelo.
        """
        try:
            num = self.view.get_num()
            den = self.view.get_den()

            fraccion = Fraccion(int(num), int(den))

            # Guardar en el modelo
            self.model.add_fraccion(fraccion)

            self.view.update_display("Fracción agregada")
            self.view.limpiar_inputs()
            self.view.mostrar_lista(self.model.get_all())

        except Exception as e:
            self.view.update_display("Error: " + str(e))

    def sumar_todo(self):
        """
        Suma todas las fracciones almacenadas.
        """
        lista = self.model.get_all()

        if len(lista) == 0:
            self.view.update_display("No hay fracciones")
            return

        resultado = lista[0]

        i = 1
        while i < len(lista):
            resultado = resultado.sumar(lista[i])
            i += 1

        self.view.update_display(str(resultado))

    def restar_todo(self):
        """
        Resta todas las fracciones almacenadas.
        """
        lista = self.model.get_all()

        if len(lista) == 0:
            self.view.update_display("No hay fracciones")
            return

        resultado = lista[0]

        i = 1
        while i < len(lista):
            resultado = resultado.restar(lista[i])
            i += 1

        self.view.update_display(str(resultado))

    def multiplicar_todo(self):
        """
        Multiplica todas las fracciones almacenadas.
        """
        lista = self.model.get_all()

        if len(lista) == 0:
            self.view.update_display("No hay fracciones")
            return

        resultado = lista[0]

        i = 1
        while i < len(lista):
            resultado = resultado.multiplicar(lista[i])
            i += 1

        self.view.update_display(str(resultado))

    def dividir_todo(self):
        """
        Divide todas las fracciones almacenadas.
        """
        #obtiene la lista de fracciones
        lista = self.model.get_all() 

        if len(lista) == 0:
            self.view.update_display("No hay fracciones")
            return

        resultado = lista[0]

        i = 1
        while i < len(lista):
            resultado = resultado.dividir(lista[i])
            i += 1

        self.view.update_display(str(resultado))
    
    def limpiar_lista(self):
        self.model.fracciones = []
        self.view.update_display("Lista limpiada")
        self.view.mostrar_lista([])