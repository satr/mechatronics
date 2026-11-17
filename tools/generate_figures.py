"""Generate deterministic, language-neutral SVG diagrams from the toy mathematical models.

Only theoretical plots; no hardware interfaces. Run from any directory:
    python3 tools/generate_figures.py
Matplotlib is needed only for figure generation, not for the core lessons/tests.
"""
from __future__ import annotations
import math
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets' / 'figures'
OUT.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({'svg.fonttype': 'none', 'font.size': 11, 'figure.dpi': 120})

# Matplotlib inserts a remote SVG 1.1 DTD even for an original static plot.
# The image does not depend on the DTD and should not reference remote XML.
SVG_DOCTYPE = (
    '<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"\n'
    '  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">'
)


def remove_generated_doctype(path: Path) -> None:
    source = path.read_text(encoding="utf-8")
    if SVG_DOCTYPE in source:
        path.write_text(source.replace(SVG_DOCTYPE, ""), encoding="utf-8")


# 1. Normalized first-order response, fraction of completed step.
fig, ax = plt.subplots(figsize=(8.8, 4.7), layout='constrained')
ts = [i / 100 for i in range(501)]
ys = [1-math.exp(-t) for t in ts]
ax.plot(ts,ys,lw=2.5)
for n in (1,2,3):
    value = 1-math.exp(-n)
    ax.axvline(n,linestyle=':',linewidth=0.9)
    ax.scatter(n,value,s=55,zorder=3)
    ax.annotate(f'{100*value:.1f}%',(n,value),xytext=(5,-16 if n==3 else 9),textcoords='offset points')
ax.axhline(1,linestyle='--',linewidth=1)
ax.set_xlim(0,5)
ax.set_ylim(0,1.09)
ax.set_xlabel(r'$t/\tau$')
ax.set_ylabel(r'$(v(t)-v_0)/(u-v_0)$')
ax.grid(True,alpha=.22)
fig.savefig(OUT/'first_order_response.svg',bbox_inches='tight')
remove_generated_doctype(OUT/'first_order_response.svg')
plt.close(fig)

# 2. Euler left-endpoint integration of v(t)=2t mm/s (time in seconds).
fig, ax=plt.subplots(figsize=(8.8,4.7),layout='constrained')
ts=[i/100 for i in range(201)]
ax.plot(ts,[t*t for t in ts],lw=2.5,label=r'$x=t^2$')
dt=0.5
points=[0.0]
for n in range(4):points.append(points[-1]+(2*n*dt)*dt)
ax.plot([n*dt for n in range(5)],points,lw=2.0,label=r'$x_{\mathrm{Euler}},\ \Delta t=0.5\,\mathrm{s}$')
ax.scatter([n*dt for n in range(5)],points,s=30)
ax.set_xlabel(r'$t\ (\mathrm{s})$')
ax.set_ylabel(r'$x\ (\mathrm{mm})$')
ax.set_xlim(0,2)
ax.set_ylim(0,4.4)
ax.grid(True,alpha=.22)
ax.legend(loc='upper left')
fig.savefig(OUT/'euler_vs_exact.svg',bbox_inches='tight')
remove_generated_doctype(OUT/'euler_vs_exact.svg')
plt.close(fig)

# 3. Symbol-only block diagram of the ideal proportional torque model.
fig,ax=plt.subplots(figsize=(10.2,3.3),layout='constrained')
ax.set_xlim(0,12)
ax.set_ylim(0,3.8)
ax.axis('off')

def arrow(a,b,style='-|>'):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle=style,mutation_scale=13,lw=1.7))

def block(x,y,w,h,label):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.06',linewidth=1.3,facecolor='none'))
    ax.text(x+w/2,y+h/2,label,ha='center',va='center',fontsize=12)

ax.text(.25,2.6,r'$u$',fontsize=16,ha='center')
arrow((.45,2.55),(1.55,2.55))
ax.add_patch(Circle((1.9,2.55),.33,fill=False,lw=1.3))
ax.text(1.9,2.55,r'$\Sigma$',ha='center',va='center',fontsize=15)
ax.text(1.64,2.81,'+',ha='center',fontsize=10)
ax.text(1.91,2.1,'−',ha='center',fontsize=12)
arrow((2.23,2.55),(3.1,2.55))
ax.text(2.7,2.82,r'$e$',ha='center',fontsize=12)
block(3.15,2.1,2.25,.9,r'$M=K e$')
arrow((5.47,2.55),(6.45,2.55))
block(6.5,2.1,2.8,.9,r'$J\dot{\omega}=M$')
arrow((9.37,2.55),(11.65,2.55))
ax.text(11.66,2.83,r'$\omega$',ha='center',fontsize=16)
arrow((10.5,2.55),(10.5,.85),style='-')
arrow((10.5,.85),(1.91,.85),style='-')
arrow((1.91,.85),(1.91,2.19))
fig.savefig(OUT/'control_loop.svg',bbox_inches='tight')
remove_generated_doctype(OUT/'control_loop.svg')
plt.close(fig)
print('Generated 3 original SVG figures in', OUT)