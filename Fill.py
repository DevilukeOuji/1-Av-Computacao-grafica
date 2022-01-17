from Printer import DesenharPixel

def GetPoint(point, points):
    x,y = point[0], point[1]
    if [x,y] not in points:
        print('O ponto está fora do polígono.')
        return None
    current = [x,y]
    return current

def Fill(point,color = "#00f",edgeColor = "#f00"):
    x,y = point[0], point[1]
    current = [x,y]

    if current != edgeColor and current != color: #adicionar verificação.
        DesenharPixel(x,y,color)
        Fill([x+1,y], color, edgeColor)
        Fill([x,y+1], color, edgeColor)
        Fill([x-1,y], color, edgeColor)
        Fill([x,y-1], color, edgeColor)

point = GetPoint([2,6], [[1,5],[2,6]])
Fill(point)