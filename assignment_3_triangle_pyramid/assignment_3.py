import argparse
import math
import matplotlib.pyplot as plt
from typing import Tuple, List

def triangle_vertices(center_x: float, center_y: float, s: float, upright: bool):
    h = s * math.sqrt(3) / 2.0
    if upright:
        return [
            (center_x, center_y + h),        
            (center_x - s/2, center_y),    
            (center_x + s/2, center_y),     
        ]
    else:
        return [
            (center_x, center_y - h),  
            (center_x - s/2, center_y ),    
            (center_x + s/2, center_y ),   
        ]

def build_pyramid(s: float, depth: int):
    h = s * math.sqrt(3) / 2.0
    fig, ax = plt.subplots()
    y = (depth)*h

    for row in range(1, depth+1):

        # center align each row
        x_start = - (row - 1) * (s / 2.0)
        y = y - h  # base of y axis for each depth

        for i in range(row):
            x = x_start + i * s
            verts = triangle_vertices(x, y, s, True)
            poly = plt.Polygon(verts, closed=True, facecolor="blue", edgecolor=None)
            ax.add_patch(poly)

        if row != depth:
            for i in range(row):
                x = x_start + i * s
                verts = triangle_vertices(x, y, s, False)
                poly = plt.Polygon(verts, closed=True, facecolor="yellow", edgecolor=None)
                ax.add_patch(poly)


    ax.set_aspect("equal")
    ax.axis("off")
    ax.autoscale(tight=True)
    plt.show()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--size", type=float, default=1.0)
    ap.add_argument("--depth", type=int, default=4)
    args = ap.parse_args()
    build_pyramid(args.size, args.depth)

if __name__ == "__main__":
    main()
