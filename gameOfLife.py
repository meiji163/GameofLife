import pygame
from lib.main import *
from lib.demos import *
from lib.gameClass import game_of_life
import argparse

# Conway's game of life written using pygame 
# Contact: Meijke Balay ()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = ("Conway's game of life is a cellular automaton. Each cell has 8 neighbors, and is either alive or dead. Each step, the status of the cell is updated. If the cell is dead and has three alive neighbors, it becomes alive. If the cell is alive and has three live neighbors it keeps living. All other cells die.\n\
                     --- Controls ---\n\
    Spacebar - Toggle edit mode. While in edit mode, click on a cell to kill it/bring it to life.\n\
    Up/Down arrows - Increase/decrease game speed."),\
                    formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("--size","-s", nargs = 2, type = int, default = [120,80], help = "set the width and height")
    parser.add_argument("--demo", choices = ["glider", "spaceship", "rpentomino","fifteencycle"], help = "example starting states")
    parser.add_argument("-p","--periodic", action = "store_true", help = "toggle periodic boundary conditions")
    args = parser.parse_args()
    
    if len(args.demo)!=0:
        for d in demos:
            if args.demo == d:
                game = game_of_life(60,40, demos[d], True)
    else:
        game = game_of_life(args.size[0],args.size[1],set(),args.periodic)
    
    pygame.init()
    mainloop(game)
    pygame.quit()
