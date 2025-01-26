import tkinter as tk

from app.views import Consultor,Action
from app.models import Consultor as Buscador

class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("BLOCKBUSTER")
        self.frm_consultor = Consultor(self,self.fun_buscar,self.fun_limpiar,\
                                    self.fun_favoritos,self.fun_guardar,\
                                    self.fun_borrar)
        self.frm_consultor.pack()
        self.busca = Buscador()


    def fun_buscar(self,action:Action):
        # print(action)
        titulo = self.frm_consultor.panel_peliculas.txt_buscar.text.get()
        self.busca.titulo = titulo
        self.busca.consultar()
        listado = [(peli.id,peli.titulo,peli.anio) for peli in self.busca.peliculas]
        self.frm_consultor.panel_peliculas.list_peliculas.items = listado
        self.frm_consultor.panel_peliculas.list_peliculas.show()
        
        


    def fun_limpiar(self,action:Action):
        self.frm_consultor.panel_peliculas.list_peliculas.clear()
        self.busca = Buscador()

    def fun_favoritos(self,action:Action):
        print(action)

    def fun_guardar(self,action:Action):
        print(action)
    
    def fun_borrar(self,action:Action):
        print(action)

    def run(self):
        self.mainloop()