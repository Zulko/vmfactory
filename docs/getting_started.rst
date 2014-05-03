Getting started
================

``vmfactory`` is written to make it easy to generate and store Viennese Mazes. In a typical script, we generate or load a canvas (a maze without colors), we initialize it with random colors, we optimize these colors to make the maze difficult/interesting, and we generate a report: ::
    
    from vmfactory import Vmaze_NHT, squares_canvas
    
    canvas = squares_canvas(4,4)
    maze = Vmaze_NHT(canvas, start = 0, goal = 15)
    maze.colorize( maze.random_colors() )
    maze.anneal(100,20) # optimize the maze
    maze.make_report().savefig('myreport.png')


Generating a canvas
--------------------

You also have the possibility of editing your own canvas with the canvas editor.

Choosing the right kind of maze
--------------------------------


Optimizing the maze
-----------------------

For a longer description of Viennese Mazes and how they can be programatically generated, refer to this blog post, or to the details in the reference manual.

Making a report
----------------

