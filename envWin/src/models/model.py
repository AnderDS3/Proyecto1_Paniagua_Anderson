class Fraccion:
    """
    Representa una fracción simple.
    """

    def __init__(self, numerador: int, denominador: int):
        """
        Crea una fracción.

        Parametros:
            numerador: número de arriba
            denominador: número de abajo (no puede ser 0)
        """
        if denominador == 0:
            raise ValueError("El denominador no puede ser 0")

        self.numerador = numerador
        self.denominador = denominador
        
    def __str__(self):
        """
        Convierte la fracción en texto.

        Retorna:
            Una cadena en formato "numerador/denominador".
        """
        return str(self.numerador) + "/" + str(self.denominador)
    
    def simplificar(self):
        """
        Simplifica la fracción actual.
        
        Utiliza el Máximo Común Divisor (MCD) para
        reducir la fracción a su forma más simple.
        """
        a = self.numerador
        b = self.denominador
        
        while b != 0:
            temp = b
            b = a % b
            a = temp
            
        divisor = a
        
        self.numerador = self.numerador // divisor
        self.denominador = self.denominador // divisor
        
    def sumar(self, otra):
        """
        Suma dos fracciones.
        
        Parámetros:
            otra: Fracción a sumar
        Return:
            Una nueva fracción como resultado
        """
        numerador = (self.numerador * otra.denominador +
                     self.denominador * otra.numerador)
        
        denominador = (self.denominador * otra.denominador)
        
        resultado = Fraccion(numerador, denominador)
        resultado.simplificar()
        return resultado
        
    def restar(self, otra):
        """
        Resta de dos fracciones
        
        Parámetros:
            otra: Fracción a restar
        Return:
            Retorna el resultado de la resta.
        """
        numerador = (self.numerador * otra.denominador -
                     self.denominador * otra.numerador)
        
        denominador = (self.denominador * otra.denominador)
        
        resultado = Fraccion(numerador, denominador)
        resultado.simplificar()
        return resultado
        
    def multiplicar(self, otra):
        """
        Multiplica dos fracciones.
        
        Parámetros:
            otra: Fracción a multiplicar
        Return:
            Retorna el resultado de la multiplicación.
        """
        numerador = self.numerador * otra.numerador
        denominador = self.denominador * otra.denominador
        
        resultado = Fraccion(numerador, denominador)
        resultado.simplificar()
        return resultado
    
    def dividir(self, otra):
        """
        Divide dos fracciones.

        Parámetros:
            otra: fracción por la cual dividir.

        Retorna:
            Una nueva fracción con el resultado.
        """
        if otra.numerador == 0:
            raise ValueError("No se puede dividir entre 0")

        numerador = self.numerador * otra.denominador
        denominador = self.denominador * otra.numerador

        resultado = Fraccion(numerador, denominador)
        resultado.simplificar()
        return resultado
        

class DataModel:
    """
    Modelo de datos que gestiona una colección de fracciones.

    Este modelo se encarga de almacenar, devolver y limpiar
    la lista de fracciones utilizadas en la aplicación.
    """

    def __init__(self):
        """
        Inicializa el modelo de datos.

        Crea una lista vacía para almacenar objetos de tipo Fraccion.
        """
        self.fracciones = []

    def add_fraccion(self, fraccion):
        """
        Agrega una fracción a la lista.

        Parámetros:
            fraccion (Fraccion): objeto de tipo Fraccion que se desea almacenar.
        """
        self.fracciones.append(fraccion)

    def get_all(self):
        """
        Retorna todas las fracciones almacenadas en el modelo.

        Retorna:
            list: lista de objetos Fraccion.
        """
        return self.fracciones

    def clear(self):
        """
        Elimina todas las fracciones almacenadas en el modelo.
        """
        self.fracciones = []