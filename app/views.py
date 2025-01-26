import tkinter as tk
from tkinter import ttk
from io import BytesIO
from PIL import Image as Img
from PIL import ImageTk
from enum import Enum,auto
from typing import Callable,Dict,Any

class Action(Enum):
    BUSCAR = auto()
    LIMPIAR = auto()
    CARGAR = auto()
    BORRAR = auto()
    GUARDAR = auto()



class BtnCustom(tk.Frame):
    def __init__(self,parent,text,action:Action,fun_delegada:Callable,**kwargs):
        
        super().__init__(parent,width=kwargs.get('width',None),\
        height=kwargs.get('height',None),highlightbackground='black',highlightthickness=1)
        self.pack_propagate(False)
        btn = tk.Button(self,text=text,background=kwargs.get('bg',None),\
                        relief=tk.FLAT,command=self.__handle_click)
        btn.pack(side=tk.TOP,fill=tk.BOTH,expand=True)
        # self.fun_args = kwargs.get('fun_args')
        self.action = action
        self.funcion_delegada = fun_delegada


    def __handle_click(self):
        self.funcion_delegada(self.action)

class TextField(tk.Frame):
    def __init__(self,parent,**kwargs):
        super().__init__(parent,width=kwargs.get('width'),\
        height=kwargs.get('height'),highlightbackground='black',highlightthickness=1)
        self.pack_propagate(False)
        self.text = tk.StringVar()
        txt = tk.Entry(self,textvariable=self.text)
        txt.pack(side=tk.TOP,fill=tk.BOTH,expand=True)

class ListView(tk.Frame):
    def __init__(self,show_pelicula,**kwargs):
        super().__init__(kwargs.get('parent'),width=kwargs.get('width'),height=kwargs.get('height'),highlightbackground='black',highlightthickness=1)
        self.pack_propagate(False)
        self.headers = []
        self.list = ttk.Treeview(self)
        self.list['columns'] = kwargs.get('headers')
        ancho_list = kwargs.get('width')
        for i,header in enumerate(kwargs.get('headers')):
            self.list.heading(header,text=header)
            width = ancho_list-70 if i == 0 else 70
            self.list.column(header,anchor=tk.CENTER,width=width)
        self.list.heading("#0", text='')
        self.list.column("#0", width=0,stretch=tk.NO)
        self.list.pack(side=tk.TOP,expand=True, fill=tk.BOTH)
        self.items = []
        # self.selected_item = None
        self.__item_selected = show_pelicula

        self.list.bind('<ButtonRelease-1>',self.on_click)

    def on_click(self,event):
        select_item = self.list.focus()        
        if select_item:
            item_data=self.list.item(select_item)
            print(item_data)
            titulo,_=item_data.get('values',None)
            self.__item_selected(titulo)
            
            item_id = item_data['text']
            print(item_id)

    def add(self,item:list):
        self.items.append(item)

    def clear(self):
        self.items = []
        for item in self.list.get_children():
            self.list.delete(item)

    def show(self):
        for item in self.items:
            self.list.insert('',tk.END,text=item[0],values=item[1:])

class Label(tk.Frame):
    def __init__(self,**kwargs):
        super().__init__(kwargs.get('parent'),width=kwargs.get('width'),\
        height=kwargs.get('height'))
        self.pack_propagate(False)
        lbl = tk.Label(self,text=kwargs.get('text'),anchor=kwargs.get('anchor'))
        lbl.pack(side=tk.TOP,expand=True,fill=tk.X)

class Image(tk.Frame):
    def __init__(self,parent,path='',**kwargs):
        super().__init__(parent,width=kwargs.get('width'),\
        height=kwargs.get('height'),highlightbackground='black',highlightthickness=1)
        self.pack_propagate(False)
        self.lbl_marco = tk.Label(self)
        self.lbl_marco.pack(side=tk.TOP,expand=True,fill=tk.BOTH)
        if path:
            with open(f"{path}", "rb") as f:
                image_bytes = f.read()
                # print(image_bytes)
            image_data = Img.open(BytesIO(image_bytes))
            output = BytesIO()
            image_data.save(output,format="PNG")
            output.seek(0)
            self.img = ImageTk.PhotoImage(file=output)
            self.lbl_marco.config(image=self.img)


class Consultor(tk.Frame):
    def __init__(self,parent,fun_buscar,fun_limpiar,fun_favoritos,\
                fun_guardar,fun_borrar,**kwargs):
        super().__init__(parent)        
        self.panel_peliculas = PanelPeliculas(self,fun_buscar,fun_limpiar,fun_favoritos)
        self.panel_peliculas.pack(side=tk.LEFT,fill=tk.BOTH,expand=True,pady=10,padx=10)
        
        self.panel_detalle_pelicula = PanelPeliculaDetalle(self,\
                                        fun_guardar,fun_borrar)
        self.panel_detalle_pelicula.pack(side=tk.LEFT,fill=tk.BOTH,expand=True,pady=10,padx=10)
        #(side=tk.LEFT,fill=tk.BOTH,expand=True,pady=10,padx=10)
        # frm_header = tk.Frame(frmIzq,width=300)
        # frm_header.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # self.txt_buscar = TextField(parent=frm_header,height=30)
        # self.txt_buscar.pack(side=tk.LEFT,expand=True,fill=tk.X)

        # btn_buscar = BtnCustom(parent=frm_header,text='Buscar',width=60,\
        #                             height=30,\
        #                             fun_args=kwargs.get('fun_args'),\
        #                             fun_delegada=kwargs.get('fun_delegada'))
        # btn_buscar.pack(side=tk.LEFT,padx=5)

        # label = tk.Label(frmIzq,text='RESULTADOS',anchor=tk.W)
        # label.pack(side=tk.TOP,expand=True,fill=tk.X,pady=5)

        # listview = ListView(parent=frmIzq,width=300,height=400,headers=['Titulo','Año'])
        # listview.pack(side=tk.TOP,expand=True,fill=tk.BOTH)

        # btn_limpiar = BtnCustom(parent=frmIzq,text='Limpiar',height=30,)
        # btn_limpiar.pack(side=tk.TOP,expand=True,fill=tk.X,pady=5)

        # btn_favoritos = BtnCustom(parent=frmIzq,text='Cargar Favoritos',height=30)
        # btn_favoritos.pack(side=tk.TOP,expand=True,fill=tk.X,pady=5)

        # frmDer = tk.Frame(self)
        # frmDer.pack(side=tk.LEFT,fill=tk.BOTH,expand=True,pady=10,padx=10)


        # lbl_titulo = tk.Label(frmDer,anchor=tk.W,text='Titulo')
        # lbl_titulo.pack(side=tk.TOP,expand=True,fill=tk.X)
        # txt_titulo = TextField(parent=frmDer,height=30,width=300)
        # txt_titulo.pack(side=tk.TOP,expand=True,fill=tk.X,pady=5)

        # lbl_director = tk.Label(frmDer,anchor=tk.W,text='Director')
        # lbl_director.pack(side=tk.TOP,expand=True,fill=tk.X)
        # txt_director = TextField(parent=frmDer,height=30,width=300)
        # txt_director.pack(side=tk.TOP,expand=True,fill=tk.X,pady=5)

        # lbl_anio = tk.Label(frmDer,anchor=tk.W,text='Año')
        # lbl_anio.pack(side=tk.TOP,expand=True,fill=tk.X)
        # txt_anio = TextField(parent=frmDer,height=30,width=300)
        # txt_anio.pack(side=tk.TOP,expand=True,fill=tk.X, pady=5)

        # img_poster = Image(parent=frmDer,width=300,height=300,path='')
        # img_poster.pack(side=tk.TOP,expand=True,fill=tk.BOTH,pady=10)

        # frm_buttons = tk.Frame(frmDer,relief=tk.GROOVE)
        # frm_buttons.pack(side=tk.TOP,expand=True,fill=tk.X)

        # btn_guardar = BtnCustom(frm_buttons,'Guradar',Action.GUARDAR,funcion,height=30,width=70,)
        # btn_guardar.pack(side=tk.RIGHT,fill=tk.X)

        # btn_borrar = BtnCustom(frm_buttons,'Borrar',Action.BORRAR,funcion,height=30,width=60)
        # btn_borrar.pack(side=tk.RIGHT,fill=tk.X,padx=10)

class PanelPeliculas(tk.Frame):
    def __init__(self,parent,fun_buscar,fun_limpiar,fun_favoritos,show_pelicula,**kwargs):
        super().__init__(parent)
        # self.pack_propagate(False)
        frm_header = tk.Frame(self,width=300)
        frm_header.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        self.txt_buscar = TextField(frm_header,height=30,width=250)
        self.txt_buscar.pack(side=tk.LEFT,expand=True,fill=tk.X)

        btn_buscar = BtnCustom(frm_header,'Buscar',Action.BUSCAR,\
                            fun_buscar,width=60,height=30)
        btn_buscar.pack(side=tk.LEFT,padx=5)

        label = tk.Label(self,text='RESULTADOS',anchor=tk.W)
        label.pack(side=tk.TOP,expand=True,fill=tk.X,pady=5)

        self.list_peliculas = ListView(show_pelicula,parent=self,width=300,height=400,headers=['Titulo','Año'])
        self.list_peliculas.pack(side=tk.TOP,expand=True,fill=tk.BOTH,pady=5)

        btn_limpiar = BtnCustom(self,'Limpiar',Action.LIMPIAR,\
                                fun_limpiar,height=30,width=300)
        btn_limpiar.pack(side=tk.TOP,expand=True,fill=tk.X,pady=5)

        btn_favoritos = BtnCustom(self,'Cargar Favoritos',Action.CARGAR,\
                                fun_favoritos,height=30,width=300)
        btn_favoritos.pack(side=tk.TOP,expand=True,fill=tk.X,pady=5)

class PanelPeliculaDetalle(tk.Frame):
    def __init__(self,parent,fun_guardar,fun_borrar,**kwargs):
        super().__init__(parent)
        # self.pack_propagate(False)
        lbl_titulo = tk.Label(self,anchor=tk.W,text='Titulo')
        lbl_titulo.pack(side=tk.TOP,expand=True,fill=tk.X)
        txt_titulo = TextField(self,height=30,width=300)
        txt_titulo.pack(side=tk.TOP,expand=True,fill=tk.X,pady=5)

        lbl_director = tk.Label(self,anchor=tk.W,text='Director')
        lbl_director.pack(side=tk.TOP,expand=True,fill=tk.X)
        txt_director = TextField(self,height=30,width=300)
        txt_director.pack(side=tk.TOP,expand=True,fill=tk.X,pady=5)

        lbl_anio = tk.Label(self,anchor=tk.W,text='Año')
        lbl_anio.pack(side=tk.TOP,expand=True,fill=tk.X)
        txt_anio = TextField(self,height=30,width=300)
        txt_anio.pack(side=tk.TOP,expand=True,fill=tk.X, pady=5)

        img_poster = Image(self,'',width=300,height=300)
        img_poster.pack(side=tk.TOP,expand=True,fill=tk.BOTH,pady=10)

        frm_buttons = tk.Frame(self,relief=tk.GROOVE)
        frm_buttons.pack(side=tk.TOP,expand=True,fill=tk.X)

        btn_guardar = BtnCustom(frm_buttons,'Guradar',Action.GUARDAR,fun_guardar,height=30,width=70,)
        btn_guardar.pack(side=tk.RIGHT,fill=tk.X)

        btn_borrar = BtnCustom(frm_buttons,'Borrar',Action.BORRAR,fun_borrar,height=30,width=60)
        btn_borrar.pack(side=tk.RIGHT,fill=tk.X,padx=10)
