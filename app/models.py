from abc import ABC
from enum import Enum
import requests

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

class Argumentos(Enum):
    ID = ('i','optional')
    TITLE = ('t','optional')
    TYPE = ('type','no')
    SEARCH = ('s','required')
    PAGE = ('page','no')
    RETORNO = ('r','no')

class Ombd:
    endpoint = 'http://www.omdbapi.com/'
    
    def __init__(self,apikey:str)->None:        
        self.apikey=apikey
        self.action = None

    args_valor = tuple[Argumentos,str]
    def run_query(self,argumentos:list[args_valor])->list|dict:
        response = {}
        if self.apikey:
            url = f'{self.endpoint}?apikey={self.apikey}'
            params_url = '&'
            for arg,value in argumentos:
                arg_simbol,required = arg.value
                params_url += f'{arg_simbol}={value}&'
            if params_url != '&':
                url += params_url
            data = requests.get(url)
            response = data.json()

        return response
    
class Consultor:
    __apikey = '607ecd0e' 
    #fields = ['titulo','anio','id','imdbID','director','poster']
    fields = {
        'titulo':'Title',
        'anio':'Year',
        'imdbID':'imdbID',
        'poster':'Poster'
    }
    
    def __init__(self,titulo:str=''):
        self.__titulo = titulo
        self.__ombd = Ombd(self.__apikey)
        self.peliculas:list[Film] = []  
        self.__settings = [
            (Argumentos.RETORNO,'json'),
            (Argumentos.TYPE,'movie')
        ]
        self.response:str = 'False'
        # self.response:dict = {}
    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self,value):
        self.__titulo = value

    def consultar(self):        
        #fields = ['titulo','anio','id','imdbID','director','poster']
        search = (Argumentos.SEARCH,self.titulo)
        self.__settings.append(search)
        response = self.__ombd.run_query(self.__settings)
        if response.get('Response') == 'True':
            self.response = 'True'
            pelis:list[dict] = response.get('Search')
            for peli in pelis:
                peli_encontrada = {f'{field}':peli[f'{self.fields[f'{field}']}'] for field in Film.fields if field in self.fields}
                peli_encontrada['director'] = 'Anonimo'
                peli_encontrada['id'] = 0
                film = Film(**peli_encontrada)
                self.peliculas.append(film)
        # return response   
    
    def pelicula_seleccionada(self,titulo:str):
        buscando = next((peli for peli in self.peliculas if peli.titulo == titulo),None)
        return buscando

        
