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

#
# 0--1--2
# |  |  |
# 3--4--5
#

levels.append({ 'canvas': [(0,1, {'color_num':0}),
                          (0,3, {'color_num':1}),
                          (1,2, {'color_num':2}),
                          (1,4, {'color_num':0}),
                          (2,5, {'color_num':0}),
                          (3,4, {'color_num':2}),
                          (4,5, {'color_num':0})],
                          
                'nodes_pos': {0: (0,1), 1: (1,1), 2: (2,1),
                              3: (0,0), 4: (1,0), 5: (2,0)},
                'start':0, 'goal': 5
              })


# ===  LEVEL 4 ======================================================

#
# Six-branches star
#


levels.append({
  'start': 0,

  'goal': 12,

  'canvas' :[
    (0, 2, {'color_num': 1}),
    (0, 3, {'color_num': 1}),
    (1, 2, {'color_num': 1}),
    (1, 7, {'color_num': 0}),
    (2, 3, {'color_num': 1}),
    (2, 6, {'color_num': 2}),
    (2, 7, {'color_num': 1}),
    (3, 4, {'color_num': 2}),
    (3, 5, {'color_num': 2}),
    (3, 6, {'color_num': 0}),
    (4, 5, {'color_num': 0}),
    (5, 11, {'color_num': 1}),
    (5, 10, {'color_num': 0}),
    (5, 6, {'color_num': 0}),
    (6, 7, {'color_num': 0}),
    (6, 9, {'color_num': 0}),
    (6, 10, {'color_num': 0}),
    (7, 8, {'color_num': 0}),
    (7, 9, {'color_num': 0}),
    (8, 9, {'color_num': 0}),
    (9, 10, {'color_num': 0}),
    (9, 12, {'color_num': 2}),
    (10, 11, {'color_num': 2}),
    (10, 12, {'color_num': 2})],

  'nodes_pos':{
    0 : [0.474, 0.895],
    1 : [0.316, 0.789],
    2 : [0.421, 0.789],
    3 : [0.526, 0.789],
    4 : [0.632, 0.789],
    5 : [0.579, 0.684],
    6 : [0.474, 0.684],
    7 : [0.368, 0.684],
    8 : [0.316, 0.579],
    9 : [0.421, 0.579],
    10 : [0.526, 0.579],
    11 : [0.632, 0.579],
    12 : [0.474, 0.474]}})


# ===  LEVEL 5 ======================================================






# ===  LEVEL 6 ======================================================





# ===  LEVEL 7 ======================================================





# ===  LEVEL 8 ======================================================

# Losange-shaped level, like in my blog post.

levels.append({
  'start': 0,

  'goal': 12,

  'canvas' :[
    (0, 1, {'color_num': 0}),
    (0, 2, {'color_num': 1}),
    (0, 3, {'color_num': 1}),
    (1, 8, {'color_num': 0}),
    (1, 2, {'color_num': 1}),
    (1, 7, {'color_num': 2}),
    (2, 3, {'color_num': 1}),
    (2, 6, {'color_num': 1}),
    (3, 4, {'color_num': 0}),
    (3, 5, {'color_num': 0}),
    (4, 11, {'color_num': 2}),
    (4, 5, {'color_num': 2}),
    (5, 11, {'color_num': 2}),
    (5, 6, {'color_num': 2}),
    (6, 10, {'color_num': 2}),
    (6, 7, {'color_num': 0}),
    (7, 8, {'color_num': 0}),
    (7, 9, {'color_num': 0}),
    (8, 9, {'color_num': 0}),
    (9, 10, {'color_num': 0}),
    (9, 12, {'color_num': 0}),
    (10, 11, {'color_num': 2}),
    (10, 12, {'color_num': 0}),
    (11, 12, {'color_num': 2})],

  'nodes_pos':{
    0 : [0.273, 0.455],
    1 : [0.364, 0.545],
    2 : [0.364, 0.455],
    3 : [0.364, 0.364],
    4 : [0.455, 0.273],
    5 : [0.455, 0.364],
    6 : [0.455, 0.455],
    7 : [0.455, 0.545],
    8 : [0.455, 0.636],
    9 : [0.545, 0.545],
    10 : [0.545, 0.455],
    11 : [0.545, 0.364],
    12 : [0.636, 0.455]}} )

# ===  LEVEL 9 ======================================================

# 4x4 square

levels.append({
  'start': 0,

  'goal': 15,

  'canvas' :[
    (0, 1, {'color_num': 1}),
    (0, 4, {'color_num': 1}),
    (1, 2, {'color_num': 0}),
    (1, 5, {'color_num': 0}),
    (2, 3, {'color_num': 2}),
    (2, 6, {'color_num': 1}),
    (3, 7, {'color_num': 0}),
    (4, 8, {'color_num': 2}),
    (4, 5, {'color_num': 2}),
    (5, 6, {'color_num': 0}),
    (5, 9, {'color_num': 0}),
    (6, 10, {'color_num': 2}),
    (6, 7, {'color_num': 2}),
    (7, 11, {'color_num': 1}),
    (8, 9, {'color_num': 0}),
    (8, 12, {'color_num': 1}),
    (9, 10, {'color_num': 2}),
    (9, 13, {'color_num': 0}),
    (10, 11, {'color_num': 2}),
    (10, 14, {'color_num': 2}),
    (11, 15, {'color_num': 2}),
    (12, 13, {'color_num': 0}),
    (13, 14, {'color_num': 1}),
    (14, 15, {'color_num': 2})],

  'nodes_pos':{
    0 : [0.000, 3.000],
    1 : [1.000, 3.000],
    2 : [2.000, 3.000],
    3 : [3.000, 3.000],
    4 : [0.000, 2.000],
    5 : [1.000, 2.000],
    6 : [2.000, 2.000],
    7 : [3.000, 2.000],
    8 : [0.000, 1.000],
    9 : [1.000, 1.000],
    10 : [2.000, 1.000],
    11 : [3.000, 1.000],
    12 : [0.000, 0.000],
    13 : [1.000, 0.000],
    14 : [2.000, 0.000],
    15 : [3.000, 0.000]}} )


# ===  LEVEL 10 ======================================================

# Stacked cube

levels.append({
  'start': 0,

  'goal': 19,

  'canvas' :[
    (0, 1, {'color_num': 1}),
    (0, 2, {'color_num': 1}),
    (1, 3, {'color_num': 0}),
    (1, 4, {'color_num': 2}),
    (2, 3, {'color_num': 2}),
    (2, 5, {'color_num': 1}),
    (3, 7, {'color_num': 1}),
    (4, 6, {'color_num': 0}),
    (4, 7, {'color_num': 2}),
    (5, 8, {'color_num': 0}),
    (5, 7, {'color_num': 2}),
    (6, 9, {'color_num': 1}),
    (6, 11, {'color_num': 2}),
    (7, 9, {'color_num': 2}),
    (7, 10, {'color_num': 2}),
    (7, 12, {'color_num': 2}),
    (8, 10, {'color_num': 2}),
    (8, 13, {'color_num': 1}),
    (9, 14, {'color_num': 1}),
    (10, 15, {'color_num': 0}),
    (11, 14, {'color_num': 0}),
    (12, 15, {'color_num': 2}),
    (12, 14, {'color_num': 1}),
    (13, 15, {'color_num': 0}),
    (14, 16, {'color_num': 1}),
    (14, 17, {'color_num': 2}),
    (15, 16, {'color_num': 1}),
    (15, 18, {'color_num': 0}),
    (16, 19, {'color_num': 1}),
    (17, 19, {'color_num': 0}),
    (18, 19, {'color_num': 0})],

  'nodes_pos':{
    0 : [0.474, 0.895],
    1 : [0.421, 0.842],
    2 : [0.526, 0.842],
    3 : [0.474, 0.789],
    4 : [0.421, 0.737],
    5 : [0.526, 0.737],
    6 : [0.368, 0.684],
    7 : [0.474, 0.684],
    8 : [0.579, 0.684],
    9 : [0.421, 0.632],
    10 : [0.526, 0.632],
    11 : [0.368, 0.579],
    12 : [0.474, 0.579],
    13 : [0.579, 0.579],
    14 : [0.421, 0.526],
    15 : [0.526, 0.526],
    16 : [0.474, 0.474],
    17 : [0.421, 0.421],
    18 : [0.526, 0.421],
    19 : [0.474, 0.368]}})



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
