import math
from typing import List, Tuple
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Polygon as SPolygon, Point

# Default polygon from the brief
DEFAULT_VERTICES = [
    (9.05, 7.76),
    (12.5, 3.0),
    (10.0, 0.0),
    (5.0, 0.0),
    (2.5, 3.0),
    (4.5, 5.0),
]

def to_np(vertices: List[Tuple[float, float]]) -> np.ndarray:
    V = np.array(vertices, dtype=float)
    # Ensure closed polygon for plotting convenience (do not duplicate for math)
    return V

def polygon_area(V: np.ndarray) -> float:
    # Shoelace formula
    x = V[:, 0]
    y = V[:, 1]
    s = np.dot(x, np.roll(y, -1)) - np.dot(y, np.roll(x, -1))
    return 0.5 * abs(s)

def edge_lengths(V: np.ndarray) -> np.ndarray:
    E = np.roll(V, -1, axis=0) - V
    return np.linalg.norm(E, axis=1)

def interior_angles(V: np.ndarray) -> np.ndarray:
    n = len(V)
    angles = []
    for i in range(n):
        prev = V[(i-1) % n]
        cur = V[i]
        nxt = V[(i+1) % n]
        a = prev - cur
        b = nxt - cur
        # Compute angle between vectors a and b
        dot = np.dot(a, b)
        na = np.linalg.norm(a)
        nb = np.linalg.norm(b)
        cosang = np.clip(dot / (na * nb), -1.0, 1.0)
        ang = math.degrees(math.acos(cosang))
        angles.append(ang)
    return np.array(angles)

def is_convex(V: np.ndarray) -> bool:
    # Check signs of z-components of cross products of successive edges
    E1 = np.roll(V, -1, axis=0) - V
    E2 = np.roll(V, -2, axis=0) - np.roll(V, -1, axis=0)
    z = E1[:, 0] * E2[:, 1] - E1[:, 1] * E2[:, 0]
    # All non-zero cross signs should be either >=0 or <=0 consistently
    nonzero = z[~np.isclose(z, 0.0)]
    if len(nonzero) == 0:
        return False  # degenerate
    return np.all(nonzero >= 0) or np.all(nonzero <= 0)

def centroid_vertices(V: np.ndarray) -> Tuple[float, float]:
    # Average of vertices (as asked), not the area-weighted centroid
    c = V.mean(axis=0)
    return float(c[0]), float(c[1])

def visualize(V: np.ndarray, centroid_xy: Tuple[float, float], angles: np.ndarray):
    # Prepare closed path for plotting
    P = np.vstack([V, V[0]])
    plt.figure()
    plt.fill(P[:, 0], P[:, 1], alpha=0.25)
    plt.plot(P[:, 0], P[:, 1], linewidth=2)

    # Label vertices
    for i, (x, y) in enumerate(V, start=1):
        plt.text(x, y, f"V{i}", fontsize=10, ha="right", va="bottom")

    # Mark centroid
    cx, cy = centroid_xy
    plt.scatter([cx], [cy], s=40, label="Centroid")
    plt.text(cx, cy, "  C", va="center")

    # Annotate angles
    for (x, y), ang in zip(V, angles):
        plt.text(x, y, f" {ang:.1f}°", fontsize=8, va="top")

    plt.axis("equal")
    plt.title("Polygon with Centroid and Interior Angles")
    plt.show()

def main(vertices: List[Tuple[float, float]] = None):
    V = to_np(vertices or DEFAULT_VERTICES)
    area = polygon_area(V)
    lengths = edge_lengths(V)
    angles = interior_angles(V)
    convex = is_convex(V)
    cx, cy = centroid_vertices(V)

    # Shapely validations
    sp = SPolygon(V)
    shapely_area = sp.area
    shapely_centroid = sp.centroid

    print(f"Polygon Area (shoelace): {area:.4f}")
    print(f"Polygon Area (shapely):  {shapely_area:.4f}")
    print(f"Edge Lengths: {np.round(lengths, 4).tolist()}")
    print(f"Interior Angles (deg): {np.round(angles, 2).tolist()}")
    print(f"Is Convex: {convex}")
    print(f"Centroid (vertex-avg): ({cx:.4f}, {cy:.4f})")
    print(f"Centroid (shapely):     ({shapely_centroid.x:.4f}, {shapely_centroid.y:.4f})")

    visualize(V, (cx, cy), angles)

if __name__ == "__main__":
    main()