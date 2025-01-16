class Film:
    def __init__(self,titulo=None,anio=None,id=None,imdbID=None,director=None,poster=None):
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