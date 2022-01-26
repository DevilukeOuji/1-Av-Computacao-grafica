from tkinter import *

class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)            
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        self.master.geometry(self._geom)
        self._geom=geom

window = Tk()
window.title("Simple Text Editor")

window.rowconfigure(0, minsize=1500, weight=1)
window.columnconfigure(1, minsize=1500, weight=1)

## parametros iniciais
tamanhoTela = 1000
tamanhoPixel = int(tamanhoTela / 100)

## criar o canvas utilizando o tkinter
canvas = Canvas(window)
aux = int(tamanhoTela / 2) + (tamanhoPixel / 2)

for x in range(0, tamanhoTela, tamanhoPixel): # linhas horizontais
    canvas.create_line(x, 0, x, tamanhoTela, fill='#808080')

for y in range(0, tamanhoTela, tamanhoPixel): # linhas horizontais
    canvas.create_line(0, y, tamanhoTela, y, fill='#808080')

canvas.create_line(0, aux - tamanhoPixel, tamanhoTela, aux - tamanhoPixel, fill="#f00") # linha central - horizontal
canvas.create_line(aux, 0, aux, tamanhoTela, fill="#f00") #