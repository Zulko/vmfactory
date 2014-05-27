import time
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

class Game:
    """
    
    A Game is an interactive view of a Viennese Maze:

    >>> game = Game( some_maze )
    >>> game.play()

    Although Viennese Mazes are logical puzzles which can be solved
    by hand using smart tricks, this interactive view can help.
    
    """

    def __init__(self, maze, ax=None):
        
        if ax is None:
            fig, ax = plt.subplots(1)
        
        self.ax = ax
        self.maze = maze
        self.current_maze = maze.copy()
        self.states_graph = maze.compute_graph()
        self.previous_positions = []
        self.r_click = .5
        self.update(self.states_graph.start)
        self.draw()
    
    def play(self):
        
        while True:
            pos = plt.ginput(1,timeout=-1)[0]
            node = self.which_clicked(pos)

            if node is None:
                continue
                
            elif node == self.position[0]:
            
                # clicking on self will undo last move
                if self.previous_positions != []:
                
                    self.update( self.previous_positions.pop() )
                    self.switch_colors(antisense=True)
                    self.draw()
                
            else:
                
                if node in self.next_pos:
                    self.previous_positions.append(self.position)
                    self.update( self.next_pos[node] )
                    self.switch_colors()
                    self.draw()
                    if self.position == self.states_graph.goal:
                        break
                        
        self.ax.set_title("Congrats, you win !")
        self.ax.figure.canvas.draw()
    
    
    def update(self, position):
        
        self.position = position
        accessible = nx.neighbors(self.states_graph, self.position)
        self.next_pos = { s[0] : s for s in accessible }
    
    
    def switch_colors(self, antisense = False):
        """ Switches all colors in the graph 0->1->2->0 """
        
        s = (-1) if antisense else (+1) 
        new_colors = [((c+s) % 3) for c in self.current_maze.colors]
        self.current_maze.colorize(new_colors)
    
    
    def draw(self):
        
        current_node = self.position[0]

        self.ax.clear()
        self.current_maze.draw_fancy(ax= self.ax)


        nx.draw_networkx_nodes(self.maze, self.maze.nodes_pos,
                               [current_node], ax=self.ax,
                               linewidths=3.5, node_color='white',
                               node_shape='s', node_size= 800)

        nx.draw_networkx_nodes(self.maze, self.maze.nodes_pos,
                               self.next_pos.keys(), ax=self.ax,
                               linewidths=3.5, node_color='white')
        
        
        shape,lw = (('o', 3.5) if (self.maze.goal in self.next_pos)
                     else ('h', None))
            
        nx.draw_networkx_nodes(self.maze, self.maze.nodes_pos,
                               [self.maze.goal], ax=self.ax,
                               node_shape=shape, node_color='y',
                               linewidths=lw, node_size= 800)
        
        
        self.ax.figure.canvas.draw()
    


    def which_clicked(self, pos):
        
        def distance(p1, p2):
            x1,y1 = p1
            x2, y2 = p2
            return np.sqrt( (x1-x2)**2 + (y1-y2)**2 )
        
        def dist(node):
            return distance(self.maze.nodes_pos[node], pos)
        
        nodes = self.maze.nodes()
        return nodes[np.argmin( map(dist, nodes) ) ]
    
        

def campaign(mazes, figsize=(7,7)):
    
    fig, ax  = plt.subplots(1, figsize=figsize)
    
    for maze in mazes:
        if hasattr(maze, 'title'):
            ax.set_title(maze.title)
        game = Game(maze, ax=ax)
        game.play()
    
