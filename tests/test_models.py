from app.models import Film,Ombd,Argumentos,Consultor


def test_crear_pelicula():
    peli = Film(titulo='Titulo',anio=1989,)
    assert peli.titulo == 'Titulo'
    assert peli.anio == 1989
    assert peli.id is None
    assert peli.imdbID is None
    assert peli.director is None
    assert peli.poster is None

def test_search_peli_no_existe():
    apikey = '607ecd0e'
    ombd = Ombd(apikey)
    args_value = [
        (Argumentos.SEARCH,''),
        (Argumentos.RETORNO,'json')
    ]
    response = ombd.run_query(args_value)    
    assert response.get('Response') == 'False'

def test_search_peli_existe():
    apikey = '607ecd0e'
    ombd = Ombd(apikey)
    args_value = [
        (Argumentos.TITLE,'Batman'),
        (Argumentos.RETORNO,'json')
    ]
    response = ombd.run_query(args_value)
    assert response.get('Title') ==  'Batman' 
    args_value = [
        (Argumentos.TITLE,''),
        (Argumentos.RETORNO,'json')
    ]
    response = ombd.run_query(args_value)
    assert response.get('Title') is  None

def test_consultor_batman():
    consultor = Consultor('Batman')
    consultor.consultar()
    assert len(consultor.peliculas) > 0

    consultor_ = Consultor('')
    consultor_.consultar()
    assert not consultor_.peliculas
    assert consultor_.response == 'False'

def test_consultor_selccion_pelicula():
    consultor = Consultor('Batman')
    consultor.consultar()
    assert len(consultor.peliculas) > 0
    peli_select = consultor.pelicula_seleccionada('Batman v Superman: Dawn of Justice')
    assert peli_select.anio == '2016'

    



    # assert response.get('Error') == 'Incorrect IMDb ID.'
