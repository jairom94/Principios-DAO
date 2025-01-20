from abc import ABC, abstractmethod
from enum import Enum,auto

class Alimento(Enum):
    FOTOSINTESIS = 1
    MATERIA_DESCOMPOSICION = 2
    CARNE = 3
    VEGETALES = 4
    MATERIA_INORGANICA = 5

class ReproduccionVegetal(Enum):
    FLORES = auto()
    ESPORAS = auto()
    BIPARTICION = auto()

class Estimulo(Enum):
    QUIMICA = auto()

class Respuesta(Enum):
    APROXIMACION = auto()
    HUIDA = auto()
    ESCONDERESE = auto()
    CRECER = auto()
    DEFENSA = auto()


class Ser_Vivo(ABC):
    energia = 0

    @abstractmethod
    def nutrirse(self,alimento:Alimento):
        # raise NotImplementedError('Debe instancias el metodo nutrirse para un ser vivo real.')
        pass
    
    @abstractmethod
    def relacionarse(self,estimulo:Estimulo)->Respuesta:
        # raise NotImplementedError('Debes instanciar el método relacionarse.')
        pass

    @abstractmethod
    def reproducir(self,modo:ReproduccionVegetal)->object:
        # raise NotImplementedError('Debes instanciar el método reproducir para un ser vivo real.')
        pass
    

class Vegetal(Ser_Vivo):

    def nutrirse(self,alimento:Alimento):
        if alimento != Alimento.FOTOSINTESIS:
            raise ValueError('Muerto por hambre.')
        else:
            self.energia += 1

    #Si se declara una clase abstracata
    #Se debe implementar todos sus metos
    #Al crear su implementacion

    def relacionarse(self, estimulo:Estimulo)->Respuesta:
        if estimulo == Estimulo.QUIMICA:
            return Respuesta.DEFENSA

class Geranio(Vegetal):
    def reproducir(self,modo:ReproduccionVegetal):
        if modo != ReproduccionVegetal.FLORES:
            return None
        else:
            return Geranio()
