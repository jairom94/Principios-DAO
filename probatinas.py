# import requests
# from http import HTTPStatus


# APIKEY = '607ecd0e'
# ENDPOINT = 'http://www.omdbapi.com/?apikey='
# palabra = input('Nombre de la pelicula? ')
# response = requests.get(f'{ENDPOINT}{APIKEY}&t={palabra}')
# if response.status_code == HTTPStatus.OK:
#     poster_url = response.json()['Poster']
#     response_poster = requests.get(poster_url)
#     with open(f'{palabra}.png','wb') as img:
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
from app.views import Consultor,PanelPeliculas,Action,BtnCustom,\
    TextField,PanelPeliculaDetalle,ListView
import tkinter as tk

root = tk.Tk()

def fun_prueba(action:Action):
    print(action)

# p_pelis = PanelPeliculaDetalle(root,fun_prueba,fun_prueba)
# p_pelis.pack(side=tk.LEFT,fill=tk.BOTH,expand=True,pady=10,padx=10)

# txt = TextField(root,height=30,width=500)
# txt.pack()



# btn_limpiar = BtnCustom(root,'Limpiar',Action.LIMPIAR,\
#                                 fun_prueba,height=30,width=100)
# btn_limpiar.pack()


# frame = Consultor(root,None,None,None)
# txt = TextField(parent=root,width=190,height=60)
# txt.pack()
# btn = BtnCustom(parent=root,text='Boton1',width=190,height=60)
# btn.pack()

# lbl_result = Label(parent=root,text='RESULTADOS',width=300,height=50,anchor=tk.W)
# lbl_result.pack()
listview = ListView(parent=root,width=300,height=400,headers=['Titulo','Año'])
listview.pack()
data = [
    (1,'Peli1',1990),
    (2,'Peli2',1992)
]
for item in data:
    listview.list.insert('',tk.END,text=item[0],values=item[1:])

# path_img = 'Batman.png'

# image = Image(parent=root,width=300,height=400,path=path_img)
# image.pack()

root.mainloop()



