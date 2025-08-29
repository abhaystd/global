import argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from collections import defaultdict

def spiral_coords(H, W):
    """Generate coordinates in an outward spiral from center."""
    center_r = (H - 1) // 2
    center_c = (W - 1) // 2
    yield center_r, center_c
    total = H * W
    yielded = 1
    r, c = center_r, center_c
    step = 1
    while yielded < total:
        for _ in range(step):  # right
            c += 1
            if 0 <= r < H and 0 <= c < W:
                yield r, c; yielded += 1
        for _ in range(step):  # down
            r += 1
            if 0 <= r < H and 0 <= c < W:
                yield r, c; yielded += 1
        step += 1
        for _ in range(step):  # left
            c -= 1
            if 0 <= r < H and 0 <= c < W:
                yield r, c; yielded += 1
        for _ in range(step):  # up
            r -= 1
            if 0 <= r < H and 0 <= c < W:
                yield r, c; yielded += 1
        step += 1

def place_tiles(H, W, sizes=(4,3,2,1)):
    """Greedy tile placement from center-out spiral."""
    grid = np.zeros((H, W), dtype=int)
    tiles = []
    for s in sizes:
        for (r_center, c_center) in spiral_coords(H, W):
            offsets_r = {r_center - s//2, r_center - (s-1)//2}
            offsets_c = {c_center - s//2, c_center - (s-1)//2}
            placed_here = False
            for tl_r in sorted(offsets_r):
                for tl_c in sorted(offsets_c):
                    if tl_r < 0 or tl_c < 0 or tl_r+s > H or tl_c+s > W:
                        continue
                    if np.all(grid[tl_r:tl_r+s, tl_c:tl_c+s] == 0):
                        grid[tl_r:tl_r+s, tl_c:tl_c+s] = s
                        tiles.append({'size': s, 'r': tl_r, 'c': tl_c})
                        placed_here = True
                        break
                if placed_here:
                    break
    return tiles, grid

def plot_tiles(H, W, tiles, savepath):
    """Plot tiles with matplotlib."""
    fig, ax = plt.subplots(figsize=(max(6, W/2), max(4, H/2)))
    colors = {1: '#ff4d4d', 2: '#2f78ff', 3: '#ffd54f', 4: '#9be7a0'}
    for t in tiles:
        rect = patches.Rectangle((t['c'], t['r']), t['size'], t['size'],
                                 linewidth=0.6, edgecolor='black',
                                 facecolor=colors.get(t['size'], 'gray'))
        ax.add_patch(rect)
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.set_xticks(range(W+1))
    ax.set_yticks(range(H+1))
    ax.grid(True, linewidth=0.5)
    ax.set_aspect('equal')
    ax.invert_yaxis()
    legend_patches = [patches.Patch(facecolor=colors[s], edgecolor='black', label=f'{s}x{s}') for s in sorted(colors)]
    ax.legend(handles=legend_patches, bbox_to_anchor=(1.02, 1), loc='upper left')
    ax.set_title(f"Room {W}×{H} tiled (spiral greedy)")
    plt.tight_layout()
    plt.savefig(savepath, dpi=200)
    plt.show()

def tile_room(W, H):
    tiles, grid = place_tiles(H, W)
    counts = defaultdict(int)
    for t in tiles:
        counts[t['size']] += 1
    # Fill leftover with 1x1
    empty = np.sum(grid == 0)
    if empty > 0:
        for r in range(H):
            for c in range(W):
                if grid[r, c] == 0:
                    grid[r, c] = 1
                    tiles.append({'size': 1, 'r': r, 'c': c})
                    counts[1] += 1
    outpath = f"tiling_{W}x{H}.png"
    plot_tiles(H, W, tiles, outpath)
    print(f"Tiling summary for {W}x{H}: {dict(sorted(counts.items(), reverse=True))}")
    print(f"Saved image: {outpath}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Room Tiling Spiral Visualization")
    parser.add_argument("--width", type=int, required=True, help="Width of the room")
    parser.add_argument("--height", type=int, required=True, help="Height of the room")
    args = parser.parse_args()
    tile_room(args.width, args.height)
