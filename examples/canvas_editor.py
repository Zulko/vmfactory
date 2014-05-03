# This script shows how to make a canvas with the editor,
# save it, and load it later ::
    
from vmfactory import Vmaze
from vmfactory.canvas import canvas_editor
canvas = canvas_editor() # will open an interactive session.
# For when the session has ended:
maze = Vmaze(canvas)
maze.to_file('mycanvas.can')

# Later:
from vmfactory import Vmaze_NHT
maze_nht = Vmaze_NHT.from_file('mycanvas.can')
maze_nht.draw_quick()