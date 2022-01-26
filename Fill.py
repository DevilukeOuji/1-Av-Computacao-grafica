from Paint import PaintPixel

def readPixel(point,points):
    print(point,points)
    if point in points:
        return '#f00'
    else:
        return "other"

def Fill(points, point, color, borderColor = '#f00'):
    actColor = readPixel(point, points)
    x,y = point[0], point[1]
    if(actColor != borderColor and actColor != color):
        PaintPixel(x,y, color)
        Fill(points, [x+1, y], color, borderColor)
        Fill(points, [x, y+1], color, borderColor)
        Fill(points, [x-1, y], color, borderColor)
        Fill(points, [x, y-1], color, borderColor)