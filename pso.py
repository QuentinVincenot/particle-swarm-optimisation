import numpy as np

def generate_random_objective():
	return np.random.randint(1000, size=(3, 1))

objective = generate_random_objective()
print(objective)
