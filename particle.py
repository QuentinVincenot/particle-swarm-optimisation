import numpy as np

class Particle:
	def __init__(self):
		self.position = np.random.randint(1000, size=(3, 1))
		self.velocity = np.random.randint(-50, 50, size=(3, 1))
	
	def get_distance_from_objective(self, objective):
		return np.linalg.norm(np.subtract(self.position, objective))
	
	def print(self):
		print(self.position, self.velocity)
