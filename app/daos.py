import sqlite3
from abc import ABC,abstractmethod
from tempfile import NamedTemporaryFile
import csv
import os

from app.models import Model,Film


TEMPFILE = 'TEMPFILE'

class DAO(ABC):
    model:Model = None

    @abstractmethod
    def all(self):
        pass

    @abstractmethod
    def save(self,data):
        pass

    @abstractmethod
    def delete(self,id):
        pass

class DAO_Memory(DAO):
    def __init__(self,path):        
        self.path = path
        self.__repo = []

    def all(self):
        return self.__repo
    
    def save(self,pelicula):
        self.__repo.append(pelicula)

    def delete(self,id):
        self.__repo = list(filter(lambda peli:peli.id != id,self.__repo))

class DAO_Sqlite(DAO):
    table = ''
    def __extract_fields(self):
        return f'{', '.join(self.model.fields)}'

    def __actualiza(self,query,params=[]):
        conn = sqlite3.connect(self.path)
        cursor = conn.cursor()
        cursor.execute(query,params)
        conn.commit()
        conn.close()

    def __consulta(self,query,params=[]):
        conn = sqlite3.connect(self.path)
        cursor = conn.cursor()
        cursor.execute(query,params)
        filas = cursor.fetchall()
        return [self.model.from_list(*fila) for fila in filas]

    def __init__(self,path=TEMPFILE):
        if path == TEMPFILE:
            tempdb = NamedTemporaryFile(delete=False)
            tempdb.close()
            self.path = tempdb.name
        else:
            self.path = path
        # self.__repo = []

    def all(self):
        query = f'SELECT {self.__extract_fields()} from {self.table}'
        return self.__consulta(query)

    def save(self,data):        
        query = f"""insert into {self.table}
        ({self.__extract_fields()})
        values ({', '.join(['?']*len(self.model.fields))})
        """
        values = [getattr(data,atributo) for atributo in self.model.fields]
        self.__actualiza(query,values)
        
        # self.__repo.append(pelicula)

    def delete(self,id:int):
        # self.__repo = list(filter(lambda peli:peli.id != id,self.__repo))        
        query = f'delete from {self.table} where id = ?'
        self.__actualiza(query,(id,))

    def clean_table_(self,name_table:str):
        conn = sqlite3.connect(self.path)
        cursor = conn.cursor()
        sql = f'delete from {name_table}'
        cursor.execute(sql)
        conn.commit()
        conn.close()

class DAO_CSV(DAO):
    def __extract_values(self,fila):
        result = []
        for tipo_dato,field in zip(self.model.types,self.model.fields):
            value = tipo_dato(fila[field])
            result.append(value)
        return result
    
    def __init__(self, path=TEMPFILE):
        if path == TEMPFILE:
            tempdb = NamedTemporaryFile(delete=False)
            tempdb.close()
            self.path = tempdb.name
        else:
            self.path = path

    def all(self):
        file = open(self.path,'r',newline='',encoding='UTF-8')
        reader = csv.DictReader(file,delimiter=",",quotechar='"')
        result = []
        for fila in reader:
            args = self.__extract_values(fila)
            result.append(self.model(*args))
        file.close()
        return result
    
    def save(self,data):
        file = open(self.path,'a+',newline='',encoding='UTF-8')
        file.seek(0)
        has_data_file = file.read(1)
        
        writer = csv.DictWriter(file,delimiter=",",quotechar='"',fieldnames=self.model.fields)
        dict_data = {attr:getattr(data,attr) for attr in self.model.fields}
        
        if not has_data_file:
            writer.writeheader()
        
        writer.writerow(dict_data)
        file.close()

    def delete(self, id):
        file = open(self.path,'r',newline='',encoding='UTF-8')
        newpath = f'{self.path}_copy'
        new_file = open(newpath,'w',newline='',encoding='UTF-8')
        reader = csv.DictReader(file,delimiter=",",quotechar='"')
        writer = csv.DictWriter(new_file,delimiter=",",quotechar='"',fieldnames=self.model.fields)
        writer.writeheader()
        datos = list(filter(lambda model:model.get('id')!=str(id),reader))
        writer.writerows(datos)
        file.close()
        new_file.close()
        os.remove(self.path)
        os.rename(newpath,self.path)

class DAO_Sqlite_Film(DAO_Sqlite):
    table = 'peliculas'
    model = Film

class DAO_CSV_Film(DAO_CSV):
    model = Film

