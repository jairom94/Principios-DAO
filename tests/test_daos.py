from app.models import Film
from app.daos import DAO_Sqlite_Film,DAO_CSV_Film
from pytest import fixture

@fixture
def daoSqlite():
    _dao = DAO_Sqlite_Film()
    _dao._DAO_Sqlite__actualiza(
    """ CREATE TABLE "peliculas" (
        "id"	INTEGER NOT NULL UNIQUE,
        "titulo"	TEXT NOT NULL,
        "anio"	INTEGER NOT NULL,
        "imdbID"	TEXT NOT NULL,
        "director"	TEXT NOT NULL,
        "poster"	TEXT,        
        PRIMARY KEY("id" AUTOINCREMENT)
    );"""
    )
    return _dao

@fixture
def daoCSV():
    dao_csv = DAO_CSV_Film()
    return dao_csv



def test_create_dao(daoSqlite):

    assert daoSqlite.model == Film    
    assert daoSqlite.all() == []

def test_consulta_todas_devuelve_una(daoSqlite):
    
    peli = Film('Titulo',1989,1,'imdb01','Un director','url...')
    daoSqlite.save(peli)

    pelis = daoSqlite.all()

    assert len(pelis) == 1
    assert pelis[0] == peli

def test_borrar_una_peli(daoSqlite):
    
    peli = Film('Titulo',1989,1,'imdb01','Un director','url...')
    daoSqlite.save(peli)

    peli = Film('Titulo II',1990,2,'imdb02','otro director','url...')
    daoSqlite.save(peli)

    pelis = daoSqlite.all()
    assert len(pelis) == 2

    daoSqlite.delete(2)

    pelis = daoSqlite.all()
    assert len(pelis) == 1
    assert pelis[0] == Film('Titulo',1989,1,'imdb01','Un director','url...')

def test_crear_dao_csv(daoCSV):
    assert daoCSV.model == Film
    assert daoCSV.all() == []

def test_consulta_datos_csv(daoCSV):    
    
    peli = Film("Titulo", 1989, 1, "imdb01", "Un director", "aqui una url")
    daoCSV.save(peli)

    peli = Film("Titulo 2", 1990, 2, "imdb03", "Otro director", "aqui otra url")
    daoCSV.save(peli)

    pelis = daoCSV.all()
    assert len(pelis) == 2

    daoCSV.delete(2)

    pelis = daoCSV.all()
    assert len(pelis) == 1

    assert pelis[0] == Film("Titulo", 1989, 1, "imdb01", "Un director", "aqui una url")