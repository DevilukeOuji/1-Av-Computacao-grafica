from typing import final
import Printer

class Bresenham():

    def Bresenham(initial_point, final_point):
        x1, x2 = initial_point[0],final_point[0]
        y1, y2  = initial_point[1],final_point[1]
        points = []
        if x2 == x1:
            points = (Bresenham.YLine(x1, [y1,y2]))
            return points
        else: 
            m = (y2 - y1) / (x2 - x1)
            swipe_coordinates, swipe_x, swipe_y,new_x1,new_x2,new_y1,new_y2 = Bresenham.Reflection( x1,x2,y1,y2,m)
            x1,x2,y1,y2 = new_x1,new_x2,new_y1,new_y2
            m = (y2 - y1) / (x2 - x1)
            e = m - 0.5
            points.append([x1,y1])
            while x1 < x2:
                if e > 0:
                    y1 += 1
                    e -= 1
                x1 += 1
                e += m
                points.append([x1,y1])
            Bresenham.ReflectionInverse( swipe_coordinates, swipe_x, swipe_y, points)
        return points
        
    def Reflection(x1,x2,y1,y2,m):
        swipe_coordinates, swipe_x, swipe_y = 0,0,0
        x1, y1 = x1,y1
        x2, y2 = x2, y2
        if m > 1 or m < -1:
            x1,y1= y1,x1
            x2, y2 = y2, x2
            swipe_coordinates = True
        if x1 > x2:
            x1 = -x1
            x2 = -x2
            swipe_x = True
        if y1 > y2:
            y1 = -y1
            y2 = -y2
            swipe_y = True
        return swipe_coordinates, swipe_x, swipe_y, x1,x2,y1,y2

    def ReflectionInverse( swipe_coordinates, swipe_x,swipe_y, points):
        if swipe_coordinates:
            for point in points:
                point[0],point[1] = point[1], point[0]
        if swipe_x:
            for point in points:
                point[0] *= -1
        if swipe_y:
            for point in points:
                point[1] *= -1
    
    def Draw(points, poli = False, color = '#f00'):

        if poli:
            for i in points:
                for j in i:
                    Printer.DesenharPixel(j[0], j[1], color)
        else: 
            for point in points:
                Printer.DesenharPixel(point[0], point[1], color)

    def YLine(x,Y_points):
        points = []
        Ymax = max(Y_points[0], Y_points[1]+1)
        Ymin = min(Y_points[0], Y_points[1]+1)
        for i in range(Ymin, Ymax):
            points.append([x,i])
        return points

    def Poliline(*args):
        args = args[0]
        group = [Bresenham.Bresenham(args[i], args[i+1]) for i in range(len(args)-1)]
        group.append(Bresenham.Bresenham(args[len(args)-1],args[0]))
        return group
