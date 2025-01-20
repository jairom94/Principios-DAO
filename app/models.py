from abc import ABC

class Model(ABC):
    fields:list = []
    types:list = []

    @classmethod
    def from_list(cls,*args):
        return cls(*args)
    
    def to_list(self):
        return [getattr(self,field) for field in self.fields]
    
    def __eq__(self,otro):
        result = False
        if isinstance(otro,self.__class__):
            result = all([getattr(self,field)==getattr(otro,field) for field in self.fields])
        return result

    def __hash__(self):
        values = [getattr(self,field) for field in self.fields]
        return hash(tuple(values))

    def __repr__(self):
        return f'{self.__class__.__name__}: ' +\
        f'{', '.join([f'{field}: {getattr(self,field)}' for field in self.fields])}'
    
    def __str__(self):
        return self.__repr__()

class Film(Model):
    fields = ['titulo','anio','id','imdbID','director','poster']
    types = [str,int,int,str,str,str]
    def __init__(self,titulo:str,anio:int,id=None,imdbID=None,director=None,poster=None):
        self.titulo = titulo
        self.anio = anio
        self.__id = id
        self.__imdbID = imdbID
        self.__director = director
        self.__poster = poster

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self,value):
        self.__id = value

    @property
    def imdbID(self):
        return self.__imdbID

    @imdbID.setter
    def imdbID(self,value):
        self.__imdbID = value

    @property
    def director(self):
        return self.__director

    @director.setter
    def director(self,value):
        self.__director = value

    @property
    def poster(self):
        return self.__poster

    @poster.setter
    def poster(self,value):
        self.__poster = value

    def __eq__(self,otro):
        result = False
        if isinstance(otro,Film):
            result = self.titulo == otro.titulo \
            and self.anio == otro.anio \
            and self.id == otro.id \
            and self.imdbID == otro.imdbID \
            and self.director == otro.director \
            and self.poster == otro.poster
        return result
    
    def __hash__(self):
        return hash(self.titulo,self.anio,\
                    self.id,self.imdbID,\
                    self.director,\
                    self.poster)

    def __repr__(self):
        return f'Pelicula: {self.titulo}, Estreno: {self.anio}'
    
    def __str__(self):
        return self.__repr__()