from app.models import Film


def test_crear_pelicula():
    peli = Film(titulo='Titulo',anio=1989,)
    assert peli.titulo == 'Titulo'
    assert peli.anio == 1989
    assert peli.id is None
    assert peli.imdbID is None
    assert peli.director is None
    assert peli.poster is None