from random import Random
from pprint import pprint
from level import Level
from constants import *
import random
import string

randstr_set = string.ascii_letters + string.digits

def randstr(length=5, persudo=None):
    persudo = persudo or random
    return ''.join(persudo.sample(randstr_set, length))

class MazeGenerator:
    def __init__(self, size=None, seed=None):
        self.seed = seed or randstr(5)
        self.persudo = Random(self.seed)
        self.size = size or [self.persudo.randint(10,40), self.persudo.randint(10,40)]
        self.data = []
        self.generated = False
        for r in range(self.size[0]):
            row = []
            for c in range(self.size[1]):
                row.append(BLOCK_WALL)
            self.data.append(row)

    def __set(self, point, value):
        x, y = point
        self.data[x][y] = value

    def __get(self, point):
        return self.data[point[0]][point[1]]

    def __arounds(self, point):
        x,y = point
        result = []
        if x+1 < self.size[0]:
            result.append((x+1,y))
        if x-1 >= 0:
            result.append((x-1,y))
        if y+1 < self.size[1]:
            result.append((x,y+1))
        if y-1 >= 0:
            result.append((x,y-1))
        return result

    def preview(self):
        print('Seed: '+self.seed)
        print('Size: '+repr(self.size))
        print()
        for row in self.data:
            for col in row:
                print('#' if col==BLOCK_WALL else ' ', end='')
            print()

    def generate(self):
        if self.generated:
            return False
        self.start = self.persudo.randint(0, self.size[0]-1), self.persudo.randint(0, self.size[1]-1)
        self.__set(self.start, BLOCK_AIR)
        walls = []
        visited = []
        visited.append(self.start)
        last = [0,0]
        arounds = self.__arounds(self.start)
        for a in arounds:
            if self.__get(a) == BLOCK_WALL and a not in walls:
                walls.append(a)

        while len(walls):
            w = self.persudo.choice(walls)
            if w in visited:
                walls.remove(w)
                continue
            visited.append(w)
            around = self.__arounds(w)
            pass_count = 0
            for a in around:
                if self.__get(a) == BLOCK_AIR:
                    pass_count += 1
            if pass_count <= 1:
                self.__set(w, BLOCK_AIR)
                last = w
                walls.remove(w)
                for a in around:
                    if self.__get(a) == BLOCK_WALL and a not in walls:
                        walls.append(a)

        self.__set(self.start, BLOCK_PLAYER)
        self.__set(last, BLOCK_EXIT)

        self.generated = True

    def to_level(self, name=None, viewfield=2):
        if not self.generated:
            self.generate()
        name = name or 'Random Level ({})'.format(self.seed)
        level = Level(self.data, self.size, name, viewfield=viewfield)
        return level
