from creature import Creature
from gamespace import GameSpace

import numpy as np
import random

def rand_position():
	return [random.randrange(gamespace.xdim), random.randrange(gamespace.ydim)]

def init_neurons():
	return np.random.rand(4,1)

def forward_cycle(creaturelist, gamespace):
	for i in creaturelist:
		i.move(gamespace)

if __name__ == "__main__":
	gamespace = GameSpace(100, 100)
	creaturelist = [Creature(rand_position(), init_neurons()) for i in range(100)]
	for i in range(100):
		forward_cycle(creaturelist, gamespace)

	creaturelist = [i for i in creaturelist if i.Alive]

	print(len(creaturelist))
