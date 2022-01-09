import Printer
class Line:

    def Line(initial_point, final_point):
        x1, x2 = initial_point[0],final_point[0]
        y1, y2  = initial_point[1],final_point[1]
        deltaX, deltaY = abs(x2 - x1), abs(y2 - y1)
        signalX, signalY = 1 if x2 > x1 else -1, 1 if y2 > y1 else -1
        err = deltaX - deltaY
        twoTimeserr = None
        while (x1 != x2 or y1 != y2):
            twoTimeserr = 2 * err
            if (twoTimeserr > -deltaY): err -= deltaY; x1 += signalX
            if (twoTimeserr <  deltaX): err += deltaX; y1 += signalY
            print(x1, y1)
            Printer.DesenharPixel(x1, y1)