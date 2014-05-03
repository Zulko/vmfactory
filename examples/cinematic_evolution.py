# The next script shows how to make an animation of a
# maze being optimized (requires a recent Matplotlib
# and ImageMagick): ::

import os
import networkx as nx
from matplotlib import animation
import matplotlib.pyplot as plt
from vmfactory import Vmaze_NHT
from vmfactory.canvas import stacked_cubes


input_name_format = "_tmp_evograph_%03d.vm"
 
G = Vmaze_NHT(** stacked_cubes())
G.start, G.goal = 0, max(G.nodes())
G.colorize( G.random_colors() )

counter = 0
score = G.score
for i in range(100):
    G.improve(100,max(.1,0.3*(1-1.0*i/400.0)))
    if G.score != score:
        score = G.score
        G.to_file(input_name_format%counter)
        counter += 1


fig, axes = plt.subplots(1,3, figsize=(10,3))

def animate(nframe):
    G = Vmaze_NHT.from_file(input_name_format % nframe)
    fig = G.make_report(axes=axes)
    fig.savefig("_tmp_%02d.jpeg"%nframe)

anim = animation.FuncAnimation(fig, animate, frames=counter)
anim.save("test.gif", fps=.5, writer="imagemagick")