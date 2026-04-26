"""
Se importan componentes de Tkinter para construir la interfaz gráfica.

- Label: muestra texto en pantalla.
- Button: crea botones interactivos.
- Frame: contenedor para organizar elementos.
- Entry: permite ingresar datos por teclado.
"""
from tkinter import Tk, Label, Button, Frame, Entry

class View:
    """
    Vista de la aplicación.

    Se encarga de:
    - Mostrar la interfaz gráfica.
    - Capturar datos del usuario.
    - Ejecutar acciones al presionar botones.
    """
    def __init__(self, master):
        """
        Inicializa la interfaz gráfica.

        Parámetros:
            master: ventana principal de Tkinter
        """
        # Nombre de la ventana
        self.master = master
        master.title("Calculadora de Fracciones")

        # Ventana (Contenedor principal)
        self.frame = Frame(master)
        self.frame.pack()

        # ===== VARIABLES DE CONEXIÓN (MVC) =====
        self.comando_agregar = None
        self.comando_suma = None
        self.comando_resta = None
        self.comando_multiplicacion = None
        self.comando_division = None
        self.comando_limpiar = None

        # ===== ENTRADAS / LABELS =====
        Label(self.frame, text="Numerador").pack()
        self.num_entry = Entry(self.frame)
        self.num_entry.pack()

        Label(self.frame, text="Denominador").pack()
        self.den_entry = Entry(self.frame)
        self.den_entry.pack()

        # ===== BOTÓN AGREGAR (BASE MODIFICADA) =====
        self.button = Button(self.frame,text="Agregar",
                             command=self.on_button_click)
        self.button.pack()

        # ===== BOTONES DE OPERACIONES =====
        Button(self.frame,text="Sumar",
               command=self.on_sumar_click).pack()

        Button(self.frame, text="Restar",
               command=self.on_restar_click).pack()

        Button(self.frame,text="Multiplicar",
               command=self.on_multiplicar_click).pack()

        Button(self.frame,text="Dividir",
               command=self.on_dividir_click).pack()
        
        Button(self.frame, text="Limpiar",
               command=self.on_limpiar_click).pack()

        # ===== RESULTADO (BASE) =====
        self.label = Label(self.frame, text="Resultado:")
        self.label.pack()
        
        # ===== LISTA DE FRACCIONES =====
        self.lista_label = Label(self.frame, text="Fracciones:")
        self.lista_label.pack()

    # ===== EVENTOS (llamada a los metodos) =====
    def on_button_click(self):
        """
        Se usa para agregar fracciones.
        """
        if self.comando_agregar:
            self.comando_agregar()

    def on_sumar_click(self):
        """Ejecuta la suma de fracciones."""
        if self.comando_suma:
            self.comando_suma()

    def on_restar_click(self):
        """Ejecuta la resta de fracciones."""
        if self.comando_resta:
            self.comando_resta()

    def on_multiplicar_click(self):
        """Ejecuta la multiplicación de fracciones."""
        if self.comando_multiplicacion:
            self.comando_multiplicacion()

    def on_dividir_click(self):
        """Ejecuta la división de fracciones."""
        if self.comando_division:
            self.comando_division()
    
    def on_limpiar_click(self):
        if self.comando_limpiar:
            self.comando_limpiar()

    # ===== MÉTODOS GET =====

    def get_num(self):
        """
        Obtiene el numerador ingresado por el usuario.
        """
        return self.num_entry.get()

    def get_den(self):
        """
        Obtiene el denominador ingresado por el usuario.
        """
        return self.den_entry.get()

    # ===== MOSTRAR RESULTADO =====

    def update_display(self, text):
        """
        Muestra un resultado en la interfaz.

        Parámetros:
            text: texto a mostrar.
        """
        self.label.config(text="Resultado: " + text)
    
    def limpiar_inputs(self):
        """
        Limpia las cajas de texto.
        """
        self.num_entry.delete(0, "end")
        self.den_entry.delete(0, "end")

    def update_label(self, text):
        """
        Se mantiene por compatibilidad.
        """
        self.label.config(text=text)
    def mostrar_lista(self, lista):
        """
        Muestra todas las fracciones almacenadas.

        Parámetros:
            lista: lista de objetos Fraccion.
        """
        texto = "Fracciones: "

        i = 0
        while i < len(lista):
            texto += str(lista[i]) + "  "
            i += 1

        self.lista_label.config(text=texto)