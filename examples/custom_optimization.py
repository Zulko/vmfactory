# This script shows how to evolve mazes with custom criteria.
# We create a subclass ``Vmaze_NHT_long`` where the score is
# simply the length of a minimal solution of the labyrinth is
#there is one. Note that we d'ont even check the unicity of
#sthe solution. ::

import networkx as nx
from vmfactory import Vmaze_NHT
from vmfactory.canvas import squares_grid

class Vmaze_NHT_long(Vmaze_NHT):
    """ A class that will tend to optimize mazes so that
        their solution is very long. The unicity of the
        solution is not granted. """
    
    def compute_score(self):
        
        graph = self.compute_graph()
        if self.start not in graph.nodes(): return 0
        shortest = nx.shortest_path(graph, self.start)
        if graph.goal not in shortest.keys(): return 0
        return len(shortest[graph.goal])
        
canvas = squares_grid(4,4)
maze = Vmaze_NHT_long(canvas, start = 0, goal = 15)
maze.colorize( maze.random_colors() )
maze.anneal(200,20) # optimize the maze
maze.make_report().savefig('myreport.png')