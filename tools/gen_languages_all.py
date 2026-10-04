#!/usr/bin/env python3
"""Regenerate assets/projects/languages-all.png — stacked language bar + legend.
Data: gh api repos/pauliquib/<repo>/languages (bajty dle GitHub Linguist)."""
import json, os, subprocess
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch
from matplotlib.transforms import Bbox

REPOS = ["stone-and-clay","HardCoreMode","infoflowlab","Vlnky","Fedora-SecuriTUI",
         "k3x020-nucleo","svec-studio","PRE2MULTI","sencurio-developer"]
OWNER = "pauliquib"
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(REPO_ROOT, "assets", "projects", "languages-all.png")

# paleta vytezena z puvodniho grafu (custom, ne cisty linguist)
COLORS = {
    "Python":"#3572a5","JavaScript":"#f1e05a","GDScript":"#00bcd4","TypeScript":"#2b7489",
    "C":"#a8b1bb","Rust":"#dea584","CSS":"#9b59b6","HTML":"#e34c26","C++":"#f34b7d",
    "Shell":"#89e051","PHP":"#4f5d95","Assembly":"#b5835a","QML":"#2e7d32",
    "PowerShell":"#5c6bc0","GDShader":"#c678dd","Blade":"#f7523f",
    "Linker Script":"#607d8b","Ostatní":"#5c6370",
}
BG, FG = "#0d1117", "#e6edf3"
W, H = 1000, 314

tot = {}
for r in REPOS:
    data = json.loads(subprocess.check_output(["gh","api",f"repos/{OWNER}/{r}/languages"], text=True))
    for k,v in data.items(): tot[k] = tot.get(k,0)+v

total = sum(tot.values())
items = sorted(tot.items(), key=lambda kv:-kv[1])
thr = total*0.001
named = [(k,v) for k,v in items if v >= thr]
other = sum(v for k,v in items if v < thr)
entries = named + [("Ostatní", other)]
assert len(entries) <= 18, len(entries)

fig = plt.figure(figsize=(W/100, H/100), dpi=100)
fig.patch.set_facecolor(BG)
ax = fig.add_axes([0,0,1,1]); ax.set_xlim(0,W); ax.set_ylim(0,H); ax.axis("off")
ax.set_facecolor(BG)

ax.text(3, H-22, "Jazyky — veřejné i privátní repozitáře celkem",
        color=FG, fontsize=14.5, fontweight="bold", va="center", ha="left")

# stacked bar: y 48-73, x 1-999, pill clip
bar_x0, bar_x1, bar_y0, bar_y1 = 1, 999, 241, 267
pill = FancyBboxPatch((bar_x0, bar_y0), bar_x1-bar_x0, bar_y1-bar_y0,
                      boxstyle="round,pad=0,rounding_size=13",
                      mutation_aspect=1, transform=ax.transData, facecolor="none", edgecolor="none")
ax.add_patch(pill)
x = bar_x0
for name, b in entries:
    wseg = (bar_x1-bar_x0)*b/total
    r = Rectangle((x, bar_y0), wseg, bar_y1-bar_y0, facecolor=COLORS[name], edgecolor="none")
    r.set_clip_path(pill)
    ax.add_patch(r)
    x += wseg

# legenda: row-major, 3 sloupce x 6 radku (stejna geometrie jako puvodni)
cols_x = [16, 352, 680]; text_dx = 14
rows_y = [206, 170, 134, 102, 70, 30]
for i,(name,b) in enumerate(entries):
    row, col = divmod(i, 3)
    cx, cy = cols_x[col], rows_y[row]
    ax.scatter([cx],[cy], s=70, c=COLORS[name], marker="o", linewidths=0, clip_on=False)
    ax.text(cx+text_dx, cy, f"{name} {b/total*100:.1f}%", color=FG,
            fontsize=12.5, va="center", ha="left")

fig.savefig(OUT, dpi=100, facecolor=BG)
print("saved", OUT, "| entries:", len(entries), "| total MB:", round(total/1e6,2))
for n,b in entries: print(f"  {n:15} {b:>10}  {b/total*100:.1f}%")
