from Printer import DesenharPixel


class Fill:

    def Fill(x,y,color,edgeColor):
        current = lerPixel(x,y) # ajeitar tinkter para fazer verificação
        if current != edgeColor and current != color:
            DesenharPixel(x,y,color)
            Fill(x+1,y, color, edgeColor)
            Fill(x,y+1, color, edgeColor)
            Fill(x-1,y, color, edgeColor)
            Fill(x,y-1, color, edgeColor)
