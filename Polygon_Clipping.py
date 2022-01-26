top = 50 #pick those as args
right = 50
bottom = -50
left = -50

def ClipTop(polygon):
    new_polygon = []
    for i in range(len(polygon)):
        print(i)    
        p1 = polygon[i]
        p2 = polygon[(i+1) % len(polygon)]
        print(p1,p2)
        if p1[1] == 0:continue
        if(p1[0] < top): # from inside to inside
            if(p2[0] < top):
                new_polygon.append(p2)
            else:   #from inside to outside
                x = (top - p1[0]*(p2[1]-p1[1])) / (p2[0] -p1[0]+p1[1])
                new_polygon.append([round(x), top])
        else:
            if p2[0] > top: #from outside to inside
                x = (top - p1[0]*(p2[1]-p1[1])) / (p2[0] -p1[0]+p1[1])
                new_polygon.append([round(x),top])
                new_polygon.append(p2)
    return new_polygon

def ClipRight(polygon):
    new_polygon = []
    for i in range(len(polygon)):    
        p1 = polygon[i]
        p2 = polygon[(i+1) % len(polygon)]
        if p1[1] == 0:continue
        if(p1[0] < right): # from inside to inside
            if(p2[0] < right):
                new_polygon.append(p2)
            else:   #from inside to outside
                y = (right - p1[0]*(p2[1]-p1[1])) / (p2[0] -p1[0]+p1[1])
                new_polygon.append([right, round(y)])
        else:
            if p2[0] > right: #from outside to inside
                y = (right - p1[0]*(p2[1]-p1[1])) / (p2[0] -p1[0]+p1[1])
                new_polygon.append([right, round(y)])
                new_polygon.append(p2)
    return new_polygon

def ClipBottom(polygon):
    new_polygon = []
    for i in range(len(polygon)):    
        p1 = polygon[i]
        p2 = polygon[(i+1) % len(polygon)]
        if p1[1] == 0:continue
        if(p1[0] > bottom): # from inside to inside
            if(p2[0] > bottom):
                new_polygon.append(p2)
            else:   #from inside to outside
                x = (bottom - p1[0]*(p2[1]-p1[1])) / (p2[0] -p1[0]+p1[1])
                new_polygon.append([round(x),bottom])
        else:
            if p2[0] > bottom: #from outside to inside
                x = (bottom - p1[0]*(p2[1]-p1[1])) / (p2[0] -p1[0]+p1[1])
                new_polygon.append([round(x),bottom])
                new_polygon.append(p2)
    return new_polygon

def ClipLeft(polygon):
    new_polygon = []
    for i in range(len(polygon)):    
        p1 = polygon[i]
        p2 = polygon[(i+1) % len(polygon)]
        if p1[1] == 0:continue
        if(p1[0] > left): # from inside to inside
            if(p2[0] > left):
                new_polygon.append(p2)
            else:   #from inside to outside
                y = (left - p1[0]*(p2[1]-p1[1])) / (p2[0] -p1[0]+p1[1])
                new_polygon.append([left,round(y)])
        else:
            if p2[0] > left: #from outside to inside
                y = (left - p1[0]*(p2[1]-p1[1])) / (p2[0] -p1[0]+p1[1])
                new_polygon.append([left,round(y)])
                new_polygon.append(p2)
    return new_polygon

def PolygonClipping(polygon):
    clipped_polygon = []
    clipped_polygon = ClipTop(polygon)
    clipped_polygon = ClipRight(clipped_polygon)
    clipped_polygon = ClipBottom(clipped_polygon)
    clipped_polygon = ClipLeft(clipped_polygon)
    return clipped_polygon
