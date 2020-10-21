
class game_of_life():
    def __init__(self, width, height, init=set(), periodic = False):
        self.width = width
        self.height = height
        self.alive = init
        self.stop = False
        self.periodic = periodic
    
    def neighbors(self, p):
        if self.periodic: 
            nbrs = { ((p[0]+i)%self.width, (p[1]+j)%self.height) for i in [-1,0,1] for j in [-1,0,1]}
        else:
            nbrs = { (p[0]+i,p[1]+j) for i in [-1,0,1] for j in [-1,0,1] 
                    if p[0] < self.width+ 10 and p[1] < self.height+ 10}
        nbrs.discard(p)
        return nbrs

    def is_alive(self, p):
        return p in self.alive
    
    def flip(self, p):
        if self.is_alive(p):
            self.alive.discard(p)
        else:
            self.alive.add(p)

    def update(self):
        a = self.alive.copy()
        for p in self.alive:
            for q in self.neighbors(p):
                a.add(q) 
        next_alive = set() 
        for p in a: 
            alive_nbrs = [ q for q in self.neighbors(p) if self.is_alive(q) ]
            if (self.is_alive(p) and 1<len(alive_nbrs)<4) or (len(alive_nbrs) == 3):
                    next_alive.add(p)
        if self.alive == next_alive:
            self.stop = True
        self.alive = next_alive

    def display(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.is_alive((i,j)):
                    print("#", end = " ")
                else:
                    print(" ", end = " ")
            print("\n")

def fifteen_cycle(x,y):
    fc = {(x,y),(x,y+1),(x+1,y+2),(x-1,y+2),(x,y+3),(x,y+4),(x,y-1),(x,y-2),(x+1,y-3),(x-1,y-3),(x,y-4),(x,y-5)}
    return fc

glider = {(2,0),(2,1),(2,2),(1,2),(0,1)}
canoe = {(3,5),(3,6),(4,6),(5,5),(6,4),(7,3),(7,2),(6,2)}
spaceship = { (0,8),(0,6),(1,5),(2,5),(3,5),(4,5),(4,6),(4,7),(3,8)}
Rpentomino = {(10,10),(10,9),(10,11),(9,10),(11,9)}
