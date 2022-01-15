class Scanline:

    def __init__(self, edges) -> None:
        self.edges = edges

    def GetMax(self):
        Y_list = []
        X_list = []
        for i in range(len(self.edges)):
            Y_list.append(self.edges[i][1])
            X_list.append(self.edges[i][0])
        Ymin, Ymax = min(Y_list), max(Y_list)
        Xmin, Xmax = min(X_list), max(X_list)
        return Ymin,Ymax, Xmin,Xmax

    def Scanline(self, points):
        Ymin,Ymax, Xmin,Xmax = Scanline.GetMax(self)
        for y in range(Ymin, Ymax+1):
            print(y)
            intersection_list = []
            for x in range(Xmin,Xmax+1): #montando a lista de interserções para um y
                for i in points: 
                    if [x,y] in i and [x,y] not in intersection_list: intersection_list.append([x,y]) #é um ponto? ajeitar tinkter para fazer a verificação 
            print('intersection_list',intersection_list)
            '''for i in range(len(intersection_list)-1): #linhas entre intersecções encontradas para um y
                if i % 2 == 0: 
                    b = Bresenham.Bresenham
                    points = b.Bresenham([intersection_list[i][0],y], [intersection_list[i+1][0],y])
                    b.draw(points)'''
        