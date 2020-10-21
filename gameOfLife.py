import pygame
from lib.main import *
from lib.demos import *
from lib.gameClass import game_of_life
import argparse

# Conway's game of life written using pygame 
# by Meijke B.

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = ("Conway's game of life.\n\
                     --- Controls ---\n\
    * Spacebar - Toggle edit mode\n\
    * Left Click - Kill or bring to life a cell when in edit mode\n\
    * Up/Down arrows - Increase/decrease game speed"),\
                    formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("--size","-s", nargs = 2, type = int, default = [120,80], help = "set the width and height")
    parser.add_argument("--demo", choices = list(demos), help = "example starting states")
    parser.add_argument("-p","--periodic", action = "store_true", help = "toggle periodic boundary conditions")
    args = parser.parse_args()
    
    if args.demo!=None:
        periodic = True
        if args.demo == "glidergun":
            periodic = False
        game = game_of_life(60,40, demos[args.demo], periodic)
    else:
        game = game_of_life(args.size[0],args.size[1],set(),args.periodic)
    
    pygame.init()
    mainloop(game)
    pygame.quit()
