from particle import *

class Swarm:
	def __init__(self, pop_length):
		self.particles = []
		for i in range(pop_length):
			self.particles += [Particle()]

	def print(self):
		for i in range(len(self.particles)):
			self.particles[i].print()
