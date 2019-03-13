from particle import *

class Swarm:
	def __init__(self, pop_length):
		self.particles = []
		for i in range(pop_length):
			self.particles += [Particle()]

	def update_particles_positions(self):
		number_of_particles = len(self.particles)
		for i in range(number_of_particles):
			current_particle = self.particles[i]
			current_particle.update_position();

	def print(self):
		for i in range(len(self.particles)):
			self.particles[i].print()
