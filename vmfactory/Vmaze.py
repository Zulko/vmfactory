"""

This module implements a base class for Viennese Mazes 

It is then subclassed

There are two classes: in ``Vmaze`` it is allowed to go twice in a row
through the same traffic light, and in ``Vmaze_NHT`` it is not.

But most of the lines of code here are for drawing fancy things :)

"""


import pickle
from string import ascii_lowercase

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
    


class Vmaze(nx.Graph):
    """

    Base Class for Viennese Mazes with the necessary
    methods to automatically generate mazes (initialization,
    optimization, drawing).

    Notes that this does not implement states graph and score
    computation.

    Refer to classes Vmaze_NHT and Vmaze_HT for directly
    usable classes.

    For the special class of Viennese Mazes with no half-turns
    (meaning that you cannot pass the same light twice in a row)
    

    Examples
    =========

    >>> # In this example we initialize a maze from a canvas,
    >>> # optimize the colors, and generate a report. 
    >>> from vmfactory import Vmaze, squares_canvas
    >>> canvas = squares_canvas(4,4) 
    >>> maze = Vmaze(canvas, start = 0, goal = 15)
    >>> maze.colorize( maze.random_colors() )
    >>> maze.anneal(100,20) # optimize the maze
    >>> maze.make_report()


    Parameters
    ============

    canvas
      A Networkx graph object or a list of edges which form the canvas
      to be colored.

    start
      Node of the canvas from which the maze starts

    goal
      Node of the maze that must be reached.

    nodes_pos
      Position of the nodes when drawing the graph.

    """
    
    
    def __init__(self, canvas, start=None, goal=None, nodes_pos=None):

        nx.Graph.__init__(self, canvas)
        self.start = start
        self.goal = goal
        self.score = -1

        if nodes_pos is not None:
            self.nodes_pos = nodes_pos
        elif 'pos' in self.node[self.nodes()[0]]:
            self.nodes_pos = {n : self.node[n]['pos']
                              for n in self.nodes()}
        else:
            self.nodes_pos = None

        try:
            self.colors = [self[n1][n2]['col_num']
                           for (n1,n2) in self.edges()]
        except:
            self.colorize(  [None for e in self.edges()] )



    # ===   SOLVING   ==============================================
    


    def solve_graph(self, graph = None):
        """ Returns the maze's solution as a path in the state graph.
        """
        # compute_graph depends on the subclass

        if graph is None:
            graph = self.compute_graph()
        
        if ((graph.edges() == []) or
            (not (graph.start in graph)) or
             (graph.successors(graph.start) == [])):
            return [], graph
        
        try:
            shortest = list(nx.all_shortest_paths(graph,
                                                  graph.start,
                                                  graph.goal))
        except nx.NetworkXNoPath:
            return []
        
        return shortest



    def fancy_solution(self,solution):
        """ Makes the solution of Vmaze.format_solution() even more
            readable, as a string.
        """
            
        labels = dict(zip(self.nodes(),ascii_lowercase))
        return "-".join([labels[i] for i in solution]) 
    
    
    
    # ===   SCORING  =================================================



    def compute_score(self):
        """ Computes a score for the maze.

        This is an example of scoring function which implements a
        few of my favorite criteria for a good maze:

        - The solution is unique and long.
        - There are plenty of loops and bagends.
        - Many openings, many false endings which make the maze
          difficult to solve backwards.

        This is all very subjective and incomplete. To grow mazes
        according to other criteria, overwrite this function in a
        subclass of Vmaze. 
        
        """
        
        score = 1.0
        
        graph = self.compute_graph()
        
        if len(graph.nodes()) == 0:
            return 0
        
        shortest = nx.shortest_path(graph, self.start)
        
        # Check that there is only one solution.
        
        if graph.goal not in shortest.keys():
            return 0
        
        # Check that there is one solution exactly

        gen = nx.all_simple_paths(graph, self.start, self.goal)
        next(gen)
        try:
            next(gen)
        except StopIteration:
            pass
        else:
            return 1.0
        
        distances = {n: len(p) for n,p in shortest.items()}
        path_goal = shortest[self.goal]
        d_goal = distances[self.goal]
        subgraph = nx.subgraph(graph, shortest.keys())
        
        
        # Reward the length of the minimal solution
        
        score *= d_goal ** 2
        
        # Reward the openings, and the states that are nearer
        # than the solution in general
        
        openings_1 = len([d for n,d in distances.items()
                      if d <= 2])
        
        openings_2 = len([d for n,d in distances.items()
                      if d <= d_goal])
        
        score *= (openings_1 * openings_2 ** 2)
        
        # Reward the "loops"
        
        n_loops = len([e for e in subgraph.edges()
                       if abs(distances[e[0]] -distances[e[1]])>1])
        
        score *= (n_loops ** 0.5)

        # Reward the false endings

        paths_to_end = nx.shortest_path( graph, target=graph.goal)
        n_endings = len( [path for path in paths_to_end.values()
                          if len(path)<3])
        
        score *= n_endings

        return score
    
    

    # ===   COLORATION, OPTIMIZATION   ==============================
    


    def colorize(self, colors):
        """ Sets the colors of the maze's edges. """

        self.colors = colors
        for (n1,n2),color in zip(self.edges() , colors):
            self[n1][n2]['color_num']  = color
    


    def random_colors(self):
        """ Generates a vector of random colors for the maze. """

        return np.random.randint(0, 3, size=len(self.colors))
    
    

    def mutate_colors(self, proba_change):
        """ Randomly changes some colors of the maze, each color
        light having a probability proba_change to be changed. """

        changes = np.random.randint(0, 2, size=len(self.colors))
        randoms = np.random.uniform(size= len(self.colors))
        indices = randoms < proba_change
        new_colors = (self.colors + indices*changes) % 3
        self.colorize( new_colors )
    
    

    def improve(self, n=1, proba_change=0.5):
        """ Improves the maze through random color changes.


        Each traffic light has a probability ``proba_change`` of being
        modified to create the new maze. If the new maze has a score
        lower than the current maze it is dumped, otherwise it
        replaces the current maze.

        This procedure is carried over ``n`` times.

        """

        for i in range(n):
            
            old_colors = self.colors[:]
            self.mutate_colors(proba_change)
            new_score = self.compute_score()
            
            if new_score <= self.score:
                self.colorize(old_colors)
            else:
                self.score = new_score


    def anneal(self, n, k=10):
        """ Evolves a maze using annealing (cooldown).
         
        For each ``i`` in ``0..n-1``, the method "improve()" will be
        called ``k`` times with a probability of mutation
        ``1.0*(n-i)/n``.
         """
        
        for i in range(n):
            self.improve(k, proba_change=1.0*(n-i)/n)
    


    # ===   DRAWING   ===============================================
    


    def draw_quick(self,ax = None):
        """ Quick drawing of the maze.

        Example
        ========
        
        >>> import matplotlib.pyplot as plt
        >>> fig, ax = plt.subplots(1)
        >>> maze.draw_quick(ax)

        """

        if ax is None:
            fig, ax = plt.subplots(1)

        D = {0:'green', 1:'orange', 2:'red', None:'k'}
        colors = [D[c] for c in self.colors]
        nx.draw(self, ax=ax, edge_color=colors, width=4,
                node_color='w', pos=self.nodes_pos)



    def draw_fancy(self, ax=None, draw_lights=True):
        """ Fancy drawing of the maze.

        Draws the maze with lights in a fancy way, with marks on the
        streets, letters instead of numbers to label the nodes
        (by default), etc... ``draw_light`` determines whether a
        circle of the corresponding color is drawn in the middle of
        each edge. 

        """

        if ax is None:
            fig, ax = plt.subplots(1)

        D = {0:'green', 1:'orange', 2:'red', None:'k'}
        colors = [D[c] for c in self.colors]
        
        labels = dict(zip(self.nodes(),ascii_lowercase))
        
        # Streets
        nx.draw_networkx_edges(self, ax=ax, pos=self.nodes_pos,
                               edge_color='grey', width=6)
        
        # Marks on the streets
        nx.draw_networkx_edges(self, self.nodes_pos, ax=ax,
                           edge_color='white', style='--')
        
        # Colors of the streets
        nx.draw_networkx_edges(self, self.nodes_pos, ax=ax, width=6,
                               edge_color=colors, alpha=.5)

        # Nodes (no label)
        nx.draw_networkx_nodes(self, self.nodes_pos, ax=ax,
                               linewidths=.5, node_color='white')
        
        # Nodes labels
        nx.draw_networkx_labels(self, self.nodes_pos, ax=ax,
                                labels=labels, font_weight='bold')
        
        if draw_lights:
            for e,c in zip(self.edges(),colors):
                xy1, xy2 = map( np.array, [self.nodes_pos[e[i]]
                                           for i in [0,1]])
                x,y = .5*(xy1 + xy2)
                ax.plot([x],[y], markersize=10, color=c, marker='o',
                                 markeredgewidth=1.2)

        ax.set_axis_off()



    def draw_graph(self, ax=None, node_size=8):

        """ Draws the state graph of the maze in a fancy way. """

        if ax is None:
            fig, ax = plt.subplots(1)
            
        graph = self.compute_graph()
        d = nx.shortest_path(graph, graph.start)
        p_goal = d[self.goal]
        d_goal = len(p_goal)
        subgraph = nx.subgraph(graph, d.keys())
        n_levels = max(map(len, d.values()))

        nodespos = dict()
        max_nodes_in_level = 0
        nodes = [self.start]
        nodespos[self.start] = [-0.5,0]

        for i in range(1,n_levels+2):

            nodes = [[ n for n in nx.DiGraph.successors(graph,m) 
                       if len(d[n])==i+1] for m in nodes]
            nodes = sum(nodes, [])
            seen = set()
            seen_add = seen.add
            nodes = [ n for n in nodes if n not in seen
                      and not seen_add(n)]

            #nodes = list(set(sum(nodes, [])))

            # place the nodes of the solution on the left
            l = [n for n in nodes if n in p_goal]
            if l != []:
                nodes.remove(l[0])
                nodes = [l[0]] + nodes

            
            if len(nodes) > max_nodes_in_level:
                max_nodes_in_level = len(nodes)

            for j, n in enumerate(nodes):
                nodespos[n] = [j-1.0*len(nodes)/2,-i]

            
        
        if ax is None:
            fig, ax = subplots(1)

        main_edges = [(n1,n2) for (n1,n2) in subgraph.edges()
                       if (len(d[n2]) - len(d[n1]) == 1)]

        other_edges = [e for e in subgraph.edges()
                       if e not in main_edges]


        nx.draw_networkx_edges(nx.Graph(subgraph),
                 edgelist=other_edges, ax=ax, pos=nodespos,
                 width=0.5, alpha=.4)

        nx.draw_networkx_edges(nx.Graph(subgraph),
                 edgelist=main_edges, ax=ax, pos=nodespos,
                 width=2)

        nx.draw_networkx_nodes(subgraph, pos=nodespos, ax=ax,
                                  node_size=node_size)



        for n, col in ([graph.start, 'g'],[graph.goal, 'b']):
            nx.draw_networkx_nodes(graph, nodespos, [n],
                                   ax=ax, node_size=1.5*node_size, 
                                   node_color=col)
        ax.set_ylim(-n_levels, 1)
        ax.set_xlim(-1.0*max_nodes_in_level /2-1,
                     1.0*max_nodes_in_level/2)

        ax.set_axis_off()



    def draw_solution(self, ax, node_size=30, shift=[1,1],
                      print_solution=False):

        """ Draws the solution of the maze in a fancy way.

        Parameters
        ===========

        ax
          A matplotlib ax

        node_size
          Size of the nodes, obviously.

        shift
          Vector (x,y) indicating the direction in which the solution
          line will be slightly shifted when the solution passes
          more than one time by the same node.

        print_solution
          If true, the solution (sequence of letters designating the
          different nodes, like a-b-g-e-f-m) is written down as the
          title of the ax.


        """ 
    
        nx.draw_networkx_edges(self, self.nodes_pos, ax=ax, width=4,
                               alpha=.2)
        
        nx.draw_networkx_nodes(self, self.nodes_pos, ax=ax,
                               node_size = node_size,
                               linewidths=.5, node_color='white')
        
        # position shift for the case where we come back to a node
        
        n0,n1 = [ self.nodes_pos[self.nodes()[i]] for i in [0,1]]
        delta = np.array(n0)-np.array(n1)
        norm = np.sqrt((delta * delta).sum())
        shift = 1.0*np.array(shift)
        shift /= np.sqrt((shift * shift).sum())
        delta_pos = norm * shift/8
        
        counter = {n:0 for n in self.nodes()}
        def pos(node):
            p = np.array(self.nodes_pos[node])
            shift = counter[node]*delta_pos
            return p + shift
        
        sol = self.solve_graph()[0]
        sol = self.format_solution( sol )
        
        positions = [pos(sol[0])]
        counter[sol[0]] += 1

        for n in sol[1:]:
            positions.append(pos(n))
            counter[n] +=1
        x,y = zip(*positions)

        ax.plot(x,y, c='w', lw=4)
        ax.plot(x,y, c='r', lw=2)
        
        if print_solution:
            title = "Solution: \n%s"%(self.fancy_solution(sol))
            ax.set_title(title)
        
        ax.set_axis_off()


    
    def make_report(self, axes=None, figsize=(10,3)):
        """ Makes a full report of the maze (colors, graph, solution)

        This is not very flexible but practical for quick scripts.

        """
    
        if axes is None:
            fig, axes = plt.subplots(1,3, figsize=figsize)
        else:
            fig = axes[0].figure
        
        for ax in axes:
            ax.clear()
        
        axes[0].set_title("Maze")
        axes[1].set_title("Graph")
        axes[2].set_title("Solution")
        self.draw_fancy(ax=axes[0], draw_lights=False)
        self.draw_graph(ax=axes[1], node_size=50)
        axes[1].set_title("Scored %d"%self.compute_score())
        self.draw_solution(ax=axes[2])
        fig.subplots_adjust(wspace=0)
        return fig

    

    # ===   IMPORT / EXPORT ========================================
    


    def __str__(self):

        edges = [e2 if (e2[2]['color_num'] is not None) else e1
                 for e1, e2 in zip(list(self.edges(data=False)),
                                   list(self.edges(data=True)))]
        str_edges = "[\n    %s]"%(",\n    ".join(map(str,edges)))

        if self.nodes_pos is not None:
            nodes_pos = ["%s : [%.03f, %.03f]"%(str(n), pos[0], pos[1])
                     for n,pos in self.nodes_pos.items()]
            str_nodes_pos = "{\n    %s}"%(",\n    ".join(nodes_pos))
        else:
            str_nodes_pos ="None"
        
        return "{\n  %s}"%(",\n\n  ".join(
                              ["'start': %s"%(str(self.start)),
                               "'goal': %s"%(str(self.goal)),
                               "'canvas' :%s"%str_edges,
                               "'nodes_pos':%s"%str_nodes_pos]))



    def __getstate__(self):
        return {'canvas': self.edges(data=True),
                'nodes_pos': self.nodes_pos,
                'start': self.start, 'goal': self.goal}
    
    
    
    def __setstate__(self, state):
        self.__init__(**state)
        try:
            colors = [e[2]['color_num'] for e in state['canvas']]
            self.colorize(colors)
        except:
            pass



    @staticmethod
    def from_file(filename):
        """ Reads a labyrinth from a file. """

        with open(filename, 'rb') as f:
            r = pickle.load(f)
        return r



    def to_file(self, filename):
        """ Saves the labyrinth to a file """
        with open(filename, 'w+') as output:
            pickle.dump(self, output, pickle.HIGHEST_PROTOCOL)
