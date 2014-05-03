from .Vmaze import Vmaze
from .Vmaze_HT import _compute_graph_HT
import networkx as nx


class Vmaze_NHT(Vmaze):
    """

    A special class of Viennese Maze in which half-turns are not
    allowed (you cannot go twice in a row through the same traffic
    light).

    See Vmaze for more doc.

    """
    


    def compute_graph(self):
        """ Computes the states maze of the graph. """
        
        graph_ht = _compute_graph_HT(self)
        
        if ( (not (graph_ht.start in graph_ht)) or
             (graph_ht.successors(graph_ht.start) == [])):
            # Means start completely blocked: return empty graph
            return nx.DiGraph()
            
            
        graph_nht = nx.DiGraph()
        graph_nht.start = self.start
        graph_nht.goal = self.goal
        
        for n1,n2 in graph_ht.edges():
            if n2 != graph_ht.goal:
                for n3 in graph_ht.successors(n2):
                    if n3 == self.goal:
                        graph_nht.add_edge((n2,n1),self.goal)
                    elif (n3[0] != n1[0]):
                        graph_nht.add_edge((n2,n1),(n3,n2))
                    
        for n1 in graph_ht.successors(graph_ht.start):
            graph_nht.add_edge(graph_nht.start,
                                   (n1,graph_ht.start))
        
        return graph_nht

    

    def solve_rec(self, solutions_cutoff = None):
        """ Solve the maze using a recursive function.

        This is slow (slower than solving using the states graph)
        and not very useful, but it was nice to code.

        """
    
        all_solutions = []

        def rec(node,d, path, seen):
            

            if node == self.goal:
                all_solutions.append(path+[node])
                if solutions_cutoff is not None:
                    if len(all_solutions)>= solutions_cutoff:
                        raise StopIteration
                return


            new_nodes = [n for n in self.neighbors(node)
                    if (((self[n][node]["color_num"]+d) % 3) != 2)]

            if d==0:
                for new_node in new_nodes:
                    rec(new_node, d+1, path+[node], seen + [node])
                return
            
            if (node,d%3, path[-1]) in seen:
                return # LOOP !
            
            new_nodes = [n for n in new_nodes if n != path[-1]]

            for n in new_nodes:
                rec(n , d+1, path+[node],
                    seen + [(node, d%3, path[-1])])
        
        try:
            rec( self.start, 0, [], [])
        except StopIteration:
            pass


        return all_solutions



    def format_solution(self, graph_solution):

        return ([graph_solution[0]] +
                [n[0][0] for n in graph_solution[1:-1]]+
                [graph_solution[-1]]) 






if __name__ == '__main__':

    edges = [(0, 1), (1, 8), (8, 9), (9, 12), (12, 11),
             (11, 4), (4, 3), (3, 0), (1, 2), (2, 3),
             (3, 5), (5, 11), (11, 10), (10, 9), (9, 7),
             (7, 1), (2, 6), (6, 7), (5, 6), (6, 10), (0,2),
             (7,8), (10,12), (5,4)]
    start, goal = 0,12 
             
                
    G = Vmaze_NHT(edges, start, goal)
    G.colorize( G.random_colors())
    G.anneal(200,10)
    
    
    print( G.score )
    sol = G.solve_graph()[0]
    print sol
    print( G.fancy_solution( G.format_solution(sol)) )

    
    try:
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(1, figsize=(6,5))
        G.draw_quick(ax=ax)
        fig.tight_layout()
        plt.show()
    except ImportError:
        print( "Matplotlib not installed, display impossible." )