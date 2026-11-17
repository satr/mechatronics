"""Generate an original language-neutral teaching illustration: tangent slope and integral area.

Run: python3 tools/generate_calculus_figure.py
The curves are generic and are not operating instructions for physical equipment.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
# Remove Matplotlib's unused external DTD from the generated static SVG.
SVG_DOCTYPE = (
    '<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"\n'
    '  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">'
)
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'assets'/'figures'/'calculus_slope_area.svg'
fig,axs=plt.subplots(1,2,figsize=(10,4),layout='constrained')
t=np.linspace(0,3,301)
# Left: a derivative is the tangent slope of x(t)=t² at t0=1.5
x=t*t;t0=1.5;x0=t0*t0
axs[0].plot(t,x,label=r'$x(t)=t^2$',linewidth=2)
axs[0].plot(t,x0+2*t0*(t-t0),linestyle='--',label=r'$dx/dt=2t$')
axs[0].scatter([t0],[x0],zorder=4)
axs[0].set(xlabel=r'$t$',ylabel=r'$x$',title=r'$dx/dt$')
axs[0].set_xlim(0,3);axs[0].set_ylim(0,9.5);axs[0].grid(alpha=.2);axs[0].legend(loc='upper left')
# Right: integral of v(t)=2t from 0 to 2; shaded area is signed displacement.
axs[1].plot(t,2*t,linewidth=2,label=r'$v(t)=2t$')
sel=t<=2
axs[1].fill_between(t[sel],0,2*t[sel],alpha=.22)
axs[1].axvline(2,linestyle=':',linewidth=1)
axs[1].annotate('A = 4',(1.1,1.0),fontsize=13)
axs[1].set(xlabel=r'$t$',ylabel=r'$v$',title=r'$v(t)$')
axs[1].set_xlim(0,3);axs[1].set_ylim(0,6.2);axs[1].grid(alpha=.2)
plt.rcParams.update({'svg.fonttype':'none'})
fig.savefig(OUT,bbox_inches='tight')
source=OUT.read_text(encoding='utf-8')
if SVG_DOCTYPE in source:
    OUT.write_text(source.replace(SVG_DOCTYPE, ''), encoding='utf-8')
plt.close(fig)
print(OUT)
