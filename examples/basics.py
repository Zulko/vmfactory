#This is the basic script to make a maze:
    
from vmfactory import Vmaze_NHT
from vmfactory.canvas import squares_grid

canvas = squares_grid(4,4) # nodes will be numbered 0..15
# NHT means no half-turns (can't pass a light twice in a row) 
maze = Vmaze_NHT(canvas, start = 0, goal = 15)
maze.colorize( maze.random_colors() )
maze.anneal(200,20) # optimize the maze
maze.make_report().savefig('myreport.png')