from .Vmaze import Vmaze
import networkx as nx

def _compute_graph_HT(self):
    """ This help function is used in Vmaze_HT and Vmaze_NHT """

    graph = nx.DiGraph()
        
    for n1,n2,c in self.edges(data=True):
        for i in range(3):
            if (i+c['color_num'] % 3) != 2:

                if n1 != self.goal:
                    if n2 == self.goal:
                        graph.add_edge((n1,i), self.goal)
                    else:
                        graph.add_edge((n1,i), (n2,(i+1)%3))

                if n2 != self.goal:
                    if n1 == self.goal:
                        graph.add_edge((n2,i), self.goal)
                    else:
                        graph.add_edge((n2,i), (n1,(i+1)%3))
            
    graph.start = (self.start,0)
    graph.goal = self.goal
    
    return graph

class Vmaze_HT(Vmaze):


    def compute_graph(self):
        
        """ Computes the states graph of the maze.

        This function is useful to solve and score the maze.
        """

        return _compute_graph_HT(self)


    def format_solution(self, graph_solution):
        """ Make the solution of Vmaze.solve() human-readable.
        
        This function differs in classes Vmaze and Vmaze_NHT.
        """

        return ( [graph_solution[0]] +
                 [n[0] for n in graph_solution[1:-1]]+
                 [graph_solution[-1]])