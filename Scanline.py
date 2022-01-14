a = [(0,1),(5,9),(4,5),(12,13)]
class Scanline:

    def Scanline(*args):
        Y_list = []
        for i in range(len(args)):
            Y_list.append(args[i][1])
        Ymin, Ymax = min(Y_list), max(Y_list)
        