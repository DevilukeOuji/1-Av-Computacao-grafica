from tkinter import *
from Canvas import *
import Bresenham
import Circle
import Curve
import Line_Clipping
import Polygon_Clipping
from Transformation import Translation, Scale, Rotation
from Fill import Fill
from Scanline import Scanline
#buttons
fr_buttons = Frame(window)


def menu(points= []):
  frameClear()
  btn_bresenham = Button(fr_buttons, text="Bresenham", command= lambda: GetBresenhamPoints(btn_bresenham)) 
  btn_circle = Button(fr_buttons, text="Círculo", command = lambda: GetCircleCoordinates(btn_circle))
  btn_curve = Button(fr_buttons, text="Curva", command= lambda: GetCurveCoordinates(btn_curve))
  btn_poliline = Button(fr_buttons, text="Polilinha", command= lambda: AskN(btn_poliline))
  btn_fill = Button(fr_buttons, text="Preenchimento recursivo", command= lambda: GetFillCoordinates(points))
  btn_scanline = Button(fr_buttons, text="Varredura", command= lambda: GetScanCoordinates(points))
  btn_lineClip = Button(fr_buttons, text="Recorte de linha", command=lambda: GetLineClipCoordinates(btn_lineClip))
  btn_polygonClip = Button(fr_buttons, text="Recorte de Polígono", command= lambda: GetPolygonClipPoints(points)) #bug
  btn_scale = Button(fr_buttons, text="Escala",command= lambda: GetScaleCoordinates(points))
  btn_translation = Button(fr_buttons, text="Translação",command= lambda: GetTranslationCoordinates(points))
  btn_rotation = Button(fr_buttons, text="Rotação",command= lambda: GetRotationCoordinates(points))
  btn_bresenham.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
  btn_circle.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
  btn_poliline.grid(row=2, column = 0, sticky="ew", padx=5, pady = 5)
  btn_curve.grid(row=3, column = 0, sticky="ew", padx=5, pady = 5)
  btn_fill.grid(row=4, column = 0, sticky="ew", padx=5, pady = 5)
  btn_scanline.grid(row=5, column = 0, sticky="ew", padx=5, pady = 5)
  btn_lineClip.grid(row=6, column = 0, sticky="ew", padx=5, pady = 5)
  btn_polygonClip.grid(row=7, column = 0, sticky="ew", padx=5, pady = 5)
  btn_scale.grid(row=8, column = 0, sticky="ew", padx=5, pady = 5)
  btn_translation.grid(row=9, column = 0, sticky="ew", padx=5, pady = 5)
  btn_rotation.grid(row=10, column = 0, sticky="ew", padx=5, pady = 5)


def frameClear():
    for wdgt in fr_buttons.grid_slaves():
        wdgt.grid_remove()

#interface
def GetPoints():
    points = []
    initialPoint = fr_buttons.grid_slaves(column=0)[1].get()
    finalPoint = fr_buttons.grid_slaves(column=0)[0].get()
    initialPoint = [int(i) for i in initialPoint.split(',')]
    finalPoint = [int(i) for i in finalPoint.split(',')]
    
    points = Bresenham.Draw(Bresenham.Bresenham(initialPoint, finalPoint))
    menu_btn = Button(fr_buttons, text="Voltar para o menu", padx=25, command= lambda: menu(points))
    menu_btn.grid(row= 0, rowspan=2,column=1, padx= 10,pady=5)

def GetBresenhamPoints(widget1):
    frameClear()
    initialPoint = Entry(fr_buttons, width=25)
    finalPoint = Entry(fr_buttons, width=25)

    initialPoint.grid(padx= 10,pady=5)
    initialPoint.insert(0, "Insira o Ponto Inicial: x,y")
    finalPoint.grid(padx= 10,pady=5)
    finalPoint.insert(0, "Insira o Ponto Final: x,y")

    line_btn = Button(fr_buttons, text="Desenhar Linha", padx=25, command= GetPoints)
    line_btn.grid(row= 0, rowspan=2,column=1, padx= 10,pady=5)

def GetPointsCircle():
    point = fr_buttons.grid_slaves(column=0)[1].get()
    radius = float(fr_buttons.grid_slaves(column=0)[0].get())
    point = [int(i) for i in point.split(',')]
    Circle.Draw(point, radius)

def GetCircleCoordinates(widget1):
    frameClear()
    point = Entry(fr_buttons, width=25)
    radius = Entry(fr_buttons, width=25)

    point.grid(padx= 10,pady=5)
    point.insert(0, "Insira o Ponto Central:")
    radius.grid(padx= 10,pady=5)
    radius.insert(0, "Insira o Raio:")

    circle_btn = Button(fr_buttons, text="Desenhar Circulo", padx=25, command= GetPointsCircle)
    circle_btn.grid(row= 0, rowspan=2,column=1, padx= 10,pady=5)

def GetPointsPoliline(n):
    points = []
    for i in range(0,2*int(n)-1,2):
      initialPoint = fr_buttons.grid_slaves(column=0)[i+1].get()
      finalPoint = fr_buttons.grid_slaves(column=0)[i].get()
      initialPoint = [int(i) for i in initialPoint.split(',')]
      finalPoint = [int(i) for i in finalPoint.split(',')]
      points += [Bresenham.Bresenham(initialPoint, finalPoint)]
    #Bresenham.Draw(points, poli=True)
    
    menu_btn = Button(fr_buttons, text="Voltar para o menu", padx=25, command= lambda: menu(points))
    menu_btn.grid(row= 0, rowspan=2,column=1, padx= 10,pady=5)

def GetN(widget1):
    nEdges = fr_buttons.grid_slaves(column=0)[0].get()
    GetPolilineCoordinates(widget1, n = nEdges)


def AskN(widget1):
    frameClear()
    nEdges = Entry(fr_buttons, width=25)
    nEdges.grid(padx= 10,pady=5)
    nEdges.insert(0, "Qual o número de vértices do polígono?")
    n_btn = Button(fr_buttons, text="Escolher vértices", padx=25, command= lambda: GetN(widget1))
    n_btn.grid(row= 0, rowspan=2,column=1, padx= 10,pady=5)

def GetPolilineCoordinates(widget1, n):
    frameClear()
    for _ in range(int(n)):
      initialPoint = Entry(fr_buttons, width=25)
      finalPoint = Entry(fr_buttons, width=25)
      initialPoint.grid(padx= 10,pady=5)
      initialPoint.insert(0, "Insira o Ponto Inicial: x,y")
      finalPoint.grid(padx= 10,pady=5)
      finalPoint.insert(0, "Insira o Ponto Final: x,y")

    poliline_btn = Button(fr_buttons, text="Desenhar Polilinha", padx=25, command= lambda: GetPointsPoliline(n))
    poliline_btn.grid(row= 0, rowspan=2,column=1, padx= 10,pady=5)


def GetLineClipPoints():
    initialPoint = fr_buttons.grid_slaves(column=0)[1].get()
    finalPoint = fr_buttons.grid_slaves(column=0)[0].get()
    initialPoint = [int(i) for i in initialPoint.split(',')]
    finalPoint = [int(i) for i in finalPoint.split(',')]
    
    Line_Clipping.LineClipping(initialPoint,finalPoint)
    menu_btn = Button(fr_buttons, text="Voltar para o menu", padx=25, command= lambda: menu())
    menu_btn.grid(row= 0, rowspan=2,column=1, padx= 10,pady=5)

def GetLineClipCoordinates(widget1):
    frameClear()
    initialPoint = Entry(fr_buttons, width=25)
    finalPoint = Entry(fr_buttons, width=25)

    initialPoint.grid(padx= 10,pady=5)
    initialPoint.insert(0, "Insira o Ponto Inicial: x,y")
    finalPoint.grid(padx= 10,pady=5)
    finalPoint.insert(0, "Insira o Ponto Final: x,y")

    line_btn = Button(fr_buttons, text="Desenhar Linha", padx=25, command= GetLineClipPoints)
    line_btn.grid(row= 0, rowspan=2,column=1, padx= 10,pady=5)

def GetPolygonClipPoints(points):
  flat_list = [item for sublist in points for item in sublist]
  new_polygon = Polygon_Clipping.ClipRight(flat_list)
  Bresenham.Draw(new_polygon)

def GetCurvePoints():
  controlPoints = fr_buttons.grid_slaves(column=0)[1].get()
  numberPoints = int(fr_buttons.grid_slaves(column=0)[0].get())
  controlPoints = [int(i) for i in controlPoints.split(',')]
  print(controlPoints, numberPoints)
  points = Curve.bezier_curve(controlPoints, numberPoints)
  points = [[round(points[i]), round(points[i+1])] for i in range(len(points)-1)]
  Bresenham.Draw(points)

  menu_btn = Button(fr_buttons, text="Voltar para o menu", padx=25, command= lambda: menu())
  menu_btn.grid(row= 0, rowspan=2,column=1, padx= 10,pady=5)

def GetCurveCoordinates(widget1):
  frameClear()
  controlPoints = Entry(fr_buttons, width=25)
  numberPoints = Entry(fr_buttons, width=25)

  controlPoints.grid(padx= 10,pady=5)
  controlPoints.insert(0, "Insira os pontos de controle:")
  numberPoints.grid(padx= 10,pady=5)
  numberPoints.insert(0, "Insira o número de pontos:")

  line_btn = Button(fr_buttons, text="Desenhar Curva", padx=25, command= GetCurvePoints)
  line_btn.grid(row= 0, rowspan=2,column=1, padx= 10,pady=5)

def GetScalePoints(points):
  x = fr_buttons.grid_slaves(column=0)[1].get()
  y = fr_buttons.grid_slaves(column=0)[0].get()
  x = float(x)
  y = float(y)

  flat_list = [item for sublist in points for item in sublist]
  print(flat_list)
  scaled = Scale(flat_list, x,y)
  Bresenham.Draw(points, poli=True)
  Bresenham.Draw(scaled, color = '#9400d3')
  menu_btn = Button(fr_buttons, text="Voltar para o menu", padx=25, command= lambda: menu())
  menu_btn.grid(row= 0, rowspan=2,column=1, padx= 10,pady=5)

def GetScaleCoordinates(points):
  frameClear()
  x = Entry(fr_buttons, width=25)
  y = Entry(fr_buttons, width=25)
  x.grid(padx= 10,pady=5)
  x.insert(0, "Insira o Ponto Inicial: x")
  y.grid(padx= 10,pady=5)
  y.insert(0, "Insira o Ponto Final: y")

  scale_btn = Button(fr_buttons, text="Alterar Escala", padx=25, command= lambda: GetScalePoints(points))
  scale_btn.grid(row= 0, rowspan=2,column=1, padx= 10,pady=5)

def GetTranslationPoints(points):
  x = fr_buttons.grid_slaves(column=0)[1].get()
  y = fr_buttons.grid_slaves(column=0)[0].get()
  x = float(x)
  y = float(x)

  flat_list = [item for sublist in points for item in sublist]
  translated = Translation(flat_list, x,y)
  print(translated)
  Bresenham.Draw(points, poli=True)
  Bresenham.Draw(translated, color = '#9400d3')
  menu_btn = Button(fr_buttons, text="Voltar para o menu", padx=25, command= lambda: menu())
  menu_btn.grid(row= 0, rowspan=2,column=1, padx= 10,pady=5)

def GetTranslationCoordinates(points):
  frameClear()
  x = Entry(fr_buttons, width=25)
  y = Entry(fr_buttons, width=25)
  x.grid(padx= 10,pady=5)
  x.insert(0, "Insira o Ponto Inicial: x")
  y.grid(padx= 10,pady=5)
  y.insert(0, "Insira o Ponto Final: y")

  scale_btn = Button(fr_buttons, text="Translação", padx=25, command= lambda: GetTranslationPoints(points))
  scale_btn.grid(row= 0, rowspan=2,column=1, padx= 10,pady=5)

def GetRotationPoints(points):
  angle = fr_buttons.grid_slaves(column=0)[0].get()
  angle = float(angle)

  flat_list = [item for sublist in points for item in sublist]
  rotate = Rotation(flat_list, angle)
  Bresenham.Draw(points, poli=True)
  Bresenham.Draw(rotate, color = '#9400d3')
  menu_btn = Button(fr_buttons, text="Voltar para o menu", padx=25, command= lambda: menu())
  menu_btn.grid(row= 0, rowspan=2,column=1, padx= 10,pady=5)

def GetRotationCoordinates(points):
  frameClear()
  x = Entry(fr_buttons, width=25)
  x.grid(padx= 10,pady=5)
  x.insert(0, "Insira o ângulo:")

  scale_btn = Button(fr_buttons, text="Rotação", padx=25, command= lambda: GetRotationPoints(points))
  scale_btn.grid(row= 0, rowspan=2,column=1, padx= 10,pady=5)

def GetFillPoints(points):
  point = fr_buttons.grid_slaves(column=0)[0].get()
  point = [int(i) for i in point.split(',')]
  print(points)
  Bresenham.Draw(points, poli=True)
  Fill(points, point, '#9400d3')
  menu_btn = Button(fr_buttons, text="Voltar para o menu", padx=25, command= lambda: menu())
  menu_btn.grid(row= 0, rowspan=2,column=1, padx= 10,pady=5)

def GetFillCoordinates(points):
  frameClear()
  point = Entry(fr_buttons, width=25)
  point.grid(padx= 10,pady=5)
  point.insert(0, "Escolha um ponto dentro do polígono:")

  scale_btn = Button(fr_buttons, text="Preencher", padx=25, command= lambda: GetFillPoints(points))
  scale_btn.grid(row= 0, rowspan=2,column=1, padx= 10,pady=5)

def GetScanPoints(points):
  Bresenham.Draw(points, poli=True)
  flat_list = [item for sublist in points for item in sublist]
  scanline = Scanline(flat_list)
  scanline_points = scanline.Scanline()
  Bresenham.Draw(scanline_points, poli=True, color = '#9400d3')

  Bresenham.Draw(points,color='#9400d3')
  menu_btn = Button(fr_buttons, text="Voltar para o menu", padx=25, command= lambda: menu())
  menu_btn.grid(row= 0, rowspan=2,column=1, padx= 10,pady=5)

def GetScanCoordinates(points):
  frameClear()
  scale_btn = Button(fr_buttons, text="Preencher", padx=25, command= lambda: GetScanPoints(points))
  scale_btn.grid(row= 0, rowspan=2,column=1, padx= 10,pady=5)

menu()
fr_buttons.grid(row=0, column=0, sticky="ns", pady=25)
canvas.grid(row=0, column=1, sticky="nsew", pady=25, padx= 15)

window.rowconfigure(0, minsize=1000, weight=1)
window.columnconfigure(1, minsize=1000, weight=1)

FullScreenApp(window)
window.mainloop()