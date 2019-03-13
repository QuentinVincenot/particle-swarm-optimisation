import numpy as np
import math

class Particle:
	def __init__(self):
		self.position = np.random.randint(1000, size=(3, 1))
		self.velocity = np.random.randint(-50, 50, size=(3, 1))
		self.best_position = self.position
		self.best_fitness = math.inf
	
	def get_distance_from_objective(self, objective):
		return np.linalg.norm(np.subtract(self.position, objective))
	
	def update_best_fitness(self, objective):
		current_fitness = self.get_distance_from_objective(objective)
		if current_fitness < self.best_fitness:
			self.best_position = self.position
			self.best_fitness = current_fitness

	def update_velocity(self, swarm_best_position):
		velocity_factor = 0.4
		cognitive_intelligence = 0.6
		collective_intelligence = 0.8
		random_factor_1 = 2 * np.random.random_sample() - 1
		random_factor_2 = 2 * np.random.random_sample() - 1
		new_velocity = velocity_factor * self.velocity
		new_velocity += cognitive_intelligence * random_factor_1 * (np.subtract(self.best_position, self.position))
		new_velocity += collective_intelligence * random_factor_2 * (np.subtract(swarm_best_position, self.position))
		self.velocity = new_velocity

	def update_position(self):
		self.position = np.round(np.add(self.position, self.velocity))
		self.keep_inbounds()
	
	def keep_inbounds(self):
		if self.position[0]>1000:
			self.position[0] = 1000
		if self.position[0]<0:
			self.position[0] = 0
		if self.position[1]>1000:
			self.position[1] = 1000
		if self.position[1]<0:
			self.position[1] = 0
		if self.position[2]>1000:
			self.position[2] = 1000
		if self.position[2]<0:
			self.position[2] = 0
	
	def print(self):
		print(self.position, self.velocity)
