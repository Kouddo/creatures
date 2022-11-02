import numpy as np

class Creature:
	def __init__(self, startpos, neurons, speed = 1):
		self.x = startpos[0]
		self.y = startpos[1]
		self.speed = speed
		self.neurons = neurons
		self.Alive = True

	def move(self, gamespace):
		direction = 360*(np.matmul(self.get_distances(gamespace), self.neurons)[0])
		self.x += np.cos(direction) * self.speed
		self.y += np.sin(direction) * self.speed
		self.check_dead(gamespace)


	def get_distances(self, gamespace):
		#up dist, right dist, down dist, left dist
		return np.array([(gamespace.xdim - self.x)/gamespace.xdim, (gamespace.ydim - self.y)/gamespace.ydim, self.x/gamespace.xdim, self.y/gamespace.ydim])


	def check_dead(self, gamespace):
		if not gamespace.xdim > self.x > 0:
			self.Alive = False
		elif not gamespace.ydim > self.y > 0:
			self.Alive = False
	#input is 4 neurons, how far each side is from the edge 
	#output is 1 neuron, direction to move 