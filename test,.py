import Bresenham
a = [(0,1),(5,9),(4,5),(12,13)]
Y_list = []
X_list = []
for i in range(len(a)): #achando X e Y máximos e mínimos
    Y_list.append(a[i][1])
    X_list.append(a[i][0])
Ymin = min(Y_list)
Ymax =max(Y_list)
Xmin = min(X_list)
Xmax = min(X_list)

for y in range(Ymin, Ymax):
    for x in range(Xmin,Xmax): #montando a lista de interserções para um y
        intersection_list = []
        if (x,y) == True: #é um ponto? ajeitar tinkter para fazer a verificação
            intersection_point = (x,y)
        intersection_list.append(intersection_point)

    for i in range(len(intersection_list)-1): #linhas entre intersecções encontradas para um y
        if i % 2 == 0: 
            for j in range(intersection_list[i], len(intersection_list[i+1])):
                b = Bresenham.Bresenham
                points = b.Bresenham([intersection_list[i][0],y], [intersection_list[i+1][0],y])
                b.draw(points)