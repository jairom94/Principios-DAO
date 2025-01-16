# import requests
# from http import HTTPStatus


# APIKEY = '607ecd0e'
# ENDPOINT = 'http://www.omdbapi.com/?apikey='
# palabra = input('Nombre de la pelicula? ')
# response = requests.get(f'{ENDPOINT}{APIKEY}&t={palabra}')
# if response.status_code == HTTPStatus.OK:
#     poster_url = response.json()['Poster']
#     response_poster = requests.get(poster_url)
#     with open(f'{palabra}.jpg','wb') as img:
#         #response_poster.content -> las imagenes se envian en bytes
#         img.write(response_poster.content)

# else:
#     print('Ha ocurrido un problema')
# print(response.status_code)
# print(response.headers['content-type'])
# print(type(response.text))
# print(response.json())

'''
import requests

# URL de la API que proporciona el video
url = 'https://ejemplo.com/api/video'

# Realizar la solicitud GET para obtener el video
response = requests.get(url, stream=True)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Abrir un archivo en modo binario para escribir el contenido del video
    with open('video.mp4', 'wb') as file:
        for chunk in response.iter_content(chunk_size=1024):
            file.write(chunk)
    print('El video se ha guardado correctamente como video.mp4')
else:
    print('Error al descargar el video:', response.status_code)

'''