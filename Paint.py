from Canvas import canvas
tamanhoTela = 1000
tamanhoPixel = int(tamanhoTela / 100)

def PointsConversion(x, y): # converter coordenadas para o sistema de grade
  real_x = int((tamanhoPixel * x) + (tamanhoTela / 2))
  real_y = int((tamanhoTela / 2) - (tamanhoPixel * y))
  return real_x, real_y

def PaintPixel(x, y, cor = '#f00'): # desenha um pixel na grade
  x1, y1 = PointsConversion(x, y)
  canvas.create_rectangle(x1, y1, x1 + tamanhoPixel, y1 - tamanhoPixel, fill=cor)