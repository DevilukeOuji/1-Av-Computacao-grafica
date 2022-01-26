from tkinter import mainloop

import Printer

def bezier_curve(control_points, number_of_curve_points):
    last_point = number_of_curve_points - 1
    return [ bezier_point(control_points, i / last_point )
             for i in range(number_of_curve_points)
           ]

def bezier_point(control_points, t):
    while len(control_points) > 1:
        control_linestring = zip(control_points[:-1], control_points[1:])
        control_points = [(1 - t) * p1 + t * p2 for p1, p2 in control_linestring]
    return control_points[0]