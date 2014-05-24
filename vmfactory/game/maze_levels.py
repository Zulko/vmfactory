from vmfactory import Vmaze_NHT

levels = []

# ===  LEVEL 1 ======================================================

# 0--1--2--4

levels.append({ 'canvas': [(0,1, {'color_num':0}),
                          (1,2, {'color_num':2}),
                          (2,3, {'color_num':1})],
                'nodes_pos': {0: (0,0),
                              1: (1,0),
                              2: (1,1),
                              3: (2,1)},
                'start': 0, 'goal': 3
               })

# ===  LEVEL 2 ======================================================


#   1--4
#  /    \
# 0-- 2--6
#  \    /
#   3--5

levels.append({ 'canvas': [(0,1, {'color_num':1}),
                          (0,2, {'color_num':0}),
                          (0,3, {'color_num':1}),
                          (1,4, {'color_num':0}),
                          (2,6, {'color_num':1}),
                          (3,5, {'color_num':2}),
                          (4,6, {'color_num':0}),
                          (6,5, {'color_num':1})],
                'nodes_pos': {0: (0,0), 1: (1,1),
                              2: (1.5,0), 3: (1,-1),
                              4: (2,1), 5: (2,-1), 6:(3,0)},
                'start':0, 'goal': 6
              })



# ===  LEVEL 3 ======================================================

levels.append({ 'canvas': [(0,1, {'color_num':1}),
                          (0,2, {'color_num':0}),
                          (0,3, {'color_num':1}),
                          (1,4, {'color_num':0}),
                          (2,6, {'color_num':1}),
                          (3,5, {'color_num':2}),
                          (4,6, {'color_num':2}),
                          (6,5, {'color_num':1})],
                'nodes_pos': {0: (0,0), 1: (1,1),
                              2: (1.5,0), 3: (1,-1),
                              4: (2,1), 5: (2,-1), 6:(3,0)},
                'start':0, 'goal': 6
              })


# ===  LEVEL 1 ======================================================



#=====================================================================
#=====================================================================
#=====================================================================


def to_maze(level, title):
    
    maze = Vmaze_NHT(level['canvas'],
                     start= level['start'],
                     goal= level['goal'],
                     nodes_pos = level['nodes_pos'])
    maze.title = title
    return maze

maze_levels = [ to_maze(level, "LEVEL %d / %d"%(i,len(levels)))
                for i, level in enumerate(levels) ]
