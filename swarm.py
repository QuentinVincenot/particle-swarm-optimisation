from particle import *

class Swarm:
	def __init__(self, pop_length):
		self.particles = []
		for i in range(pop_length):
			self.particles += [Particle()]
		self.best_position = np.random.randint(1000, size=(3, 1))
		self.best_fitness = math.inf
	
	def update_particles_best_fitness(self, objective):
		number_of_particles = len(self.particles)
		for i in range(number_of_particles):
			current_particle = self.particles[i]
			current_particle.update_best_fitness(objective)

	def update_swarm_best_fitness(self, objective):
		number_of_particles = len(self.particles)
		temporary_best_position = np.random.randint(1000, size=(3, 1))
		temporary_best_fitness = math.inf
		for i in range(number_of_particles):
			current_particle = self.particles[i]
			current_particle_best_fitness = current_particle.best_fitness
			if current_particle_best_fitness < temporary_best_fitness:
				temporary_best_position = current_particle.best_position
				temporary_best_fitness = current_particle.best_fitness
		self.best_position = temporary_best_position
		self.best_fitness = temporary_best_fitness

	def update_particles_velocities(self):
		number_of_particles = len(self.particles)
		for i in range(number_of_particles):
			current_particle = self.particles[i]
			current_particle.update_velocity(self.best_position);

	def update_particles_positions(self):
		number_of_particles = len(self.particles)
		for i in range(number_of_particles):
			current_particle = self.particles[i]
			current_particle.update_position();

	def print(self):
		for i in range(len(self.particles)):
			self.particles[i].print()
