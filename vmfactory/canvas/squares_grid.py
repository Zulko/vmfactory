import networkx as nx

def squares_grid(x_grid=4, y_grid=4):
    """
    Generates a canvas mades of a squared grid.
    

    Examples
    =========


    >>> canvas = squares_canvas(4,4) # produces
    >>>            +-+-+-+
    >>>            | | | |
    >>>            +-+-+-+
    >>>            | | | |
    >>>            +-+-+-+
    >>>            | | | |
    >>>            +-+-+-+
    >>> G = Vmaze_NHT(canvas, start=0, goal=15)

    """
    dist = lambda n1, n2 : ((n1[0]-n2[0])**2 +
                            (n1[1]-n2[1])**2 )
    tonum = lambda n: n[0]+4*(3-n[1])

    nodes_coord = [(i,j) for i in range(x_grid)
                         for j in range(y_grid)]

    nodes = map(tonum, nodes_coord)

    nodes_pos = {tonum(n): n for n in nodes_coord}

    edges_coord = [(n1,n2) for n1 in nodes_coord
                           for n2 in nodes_coord
                           if (tonum(n1)< tonum(n2))
                              and (dist(n1,n2) < 2)]

    edges = [(tonum(n1),tonum(n2)) for n1,n2 in edges_coord ]
    
    result = nx.Graph(edges)
    for n in result.nodes():
        result.node[n]['pos'] = nodes_pos[n]
    return result
