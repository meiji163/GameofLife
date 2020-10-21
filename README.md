# Game of Life
A game of life application written using PyGame.

![rpentomino](https://media.giphy.com/media/EA1yHtJbvWXDx2dWNr/giphy.gif)

Conway's game of life is a cellular automaton. Each cell has 8 neighbors, and is either alive or dead. Each step, the status of the cell is updated. If the cell is dead and has three alive neighbors, it becomes alive. If the cell is alive and has three live neighbors it keeps living. All other cells die. There are several interesting open questions; for example, do there exist [oscillators](https://www.conwaylife.com/wiki/Oscillator) of every period?
## Install
The only requirements are Python 3.8 and [PyGame](https://www.pygame.org/wiki/GettingStarted), which can be installed with pip

```
python3 -m pip install -U pygame --user
git clone https://github.com/meiji163/GameofLife && cd GameofLife
python3 gameOfLife.py --help 
```
## Usage
```
python3 gameOfLife.py [-h] [--size WIDTH HEIGHT] [--demo {glider,spaceship,rpentomino,fifteencycle}] [-p]
optional arguments:
  -h, --help            show this help message and exit
  --size, -s WIDTH HEIGHT
                        set the width and height
  --demo {glider,spaceship,rpentomino,fifteencycle}
                        example starting states
  -p, --periodic        toggle periodic boundary conditions
```

The default size is 120x80 cells. Periodic boundary conditions means the opposite sides of the grid are identified, so that it is topologically a torus. It is disabled by default. The demos are a examples of a few cool initial states.
```
python3 gameOfLife.py --demo rpentomino #example usage
``` 
## Controls
* Spacebar - Toggle edit mode
* Left Click - Kill or bring to life a cell when in edit mode
* Up/Down arrows - Increase/decrease game speed

## Todo
* Load/save states from files
* Add an options menu
* Add more demos
* Add zoom and scroll feature for larger cell grids
