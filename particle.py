import numpy as np

class Particle:
	def __init__(self):
		self.position = np.random.randint(1000, size=(3, 1))
		self.velocity = np.random.randint(-50, 50, size=(3, 1))
	
	def get_distance_from_objective(self, objective):
		return np.linalg.norm(np.subtract(self.position, objective))
	
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
