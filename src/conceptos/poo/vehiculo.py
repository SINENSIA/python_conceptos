from abc import ABC, abstractmethod

class Vehiculo(ABC):
    """
    Clase para representar un vehículo.

    Atributos:
        _marca (str): Marca del vehículo.
        _modelo (str): Modelo del vehículo.
    """

    def __init__(self, marca, modelo):
        """
        Inicializa los atributos del vehículo con la marca y el modelo especificados.

        Parámetros:
            marca (str): Marca del vehículo.
            modelo (str): Modelo del vehículo.
        """
        self._marca = marca
        self._modelo = modelo

    @property
    def marca(self):
        """ Retorna la marca del vehículo. """
        return self._marca

    @marca.setter
    def marca(self, valor):
        """ Establece la marca del vehículo. """
        self._marca = valor

    @property
    def modelo(self):
        """ Retorna el modelo del vehículo. """
        return self._modelo

    @modelo.setter
    def modelo(self, valor):
        """ Establece el modelo del vehículo. """
        self._modelo = valor

    
    def testing(self):
        return "Esto viene de vehiculo"
    
    @abstractmethod
    def mostrar_informacion(self):
        pass
