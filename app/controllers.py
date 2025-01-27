import tkinter as tk

from app.views import Consultor,Action
from app.models import Consultor as Buscador,Film



class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("BLOCKBUSTER")
        frm_consultor = Consultor(self,self.fun_buscar,self.fun_limpiar,\
                                    self.fun_favoritos,self.fun_guardar,\
                                    self.fun_borrar,self.show_pelicula)
        frm_consultor.pack()
        self.panel_peliculas = frm_consultor.panel_peliculas
        self.panel_detalle_pelicula = frm_consultor.panel_detalle_pelicula 
        self.busca = Buscador()


    def fun_buscar(self,action:Action):
        # print(action)
        titulo = self.panel_peliculas.txt_buscar.text.get()
        self.busca.titulo = titulo
        self.busca.consultar()
        listado = [(peli.id,peli.titulo,peli.anio) for peli in self.busca.peliculas]
        self.panel_peliculas.list_peliculas.items = listado
        self.panel_peliculas.list_peliculas.show()
        
        


    def fun_limpiar(self,action:Action):
        self.panel_peliculas.list_peliculas.clear()
        self.busca = Buscador()

    def fun_favoritos(self,action:Action):
        print(action)

    def fun_guardar(self,action:Action):
        print(action)
    
    def fun_borrar(self,action:Action):
        print(action)

    def show_pelicula(self,titulo:str):        
        film:Film = self.busca.pelicula_seleccionada(titulo)
        self.panel_detalle_pelicula.txt_titulo.text.set(film.titulo)
        self.panel_detalle_pelicula.txt_director.text.set(film.director)
        self.panel_detalle_pelicula.txt_anio.text.set(film.anio)
        self.panel_detalle_pelicula.img_poster.url = film.poster        
        self.panel_detalle_pelicula.img_poster.preview_poster()


    def run(self):
        self.mainloop()