def stacked_cubes():
  """ A canvas made of losanges reminding stacked cubes.
  To see what it looks like, type:

  >>> Vmaze(**stacked_cubes() ).draw_quick()
  """

  return {
  
  'start': None,

  'goal': None,

  'canvas' :[
    (0, 1),
    (0, 2),
    (1, 3),
    (1, 4),
    (2, 3),
    (2, 5),
    (3, 7),
    (4, 6),
    (4, 7),
    (5, 8),
    (5, 7),
    (6, 9),
    (6, 11),
    (7, 9),
    (7, 10),
    (7, 12),
    (8, 10),
    (8, 13),
    (9, 14),
    (10, 15),
    (11, 14),
    (12, 15),
    (12, 14),
    (13, 15),
    (14, 16),
    (14, 17),
    (15, 16),
    (15, 18),
    (16, 19),
    (17, 19),
    (18, 19)],

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
    19 : [0.474, 0.368]}}