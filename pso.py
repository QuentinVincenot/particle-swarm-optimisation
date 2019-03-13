from particle import *

import numpy as np


def initialize_problem():
	swarm = generate_random_population()
	objective = generate_random_objective()
	return swarm, objective

def generate_random_population():
	swarm = Swarm(100)
	return swarm

def generate_random_objective():
	return np.random.randint(1000, size=(3, 1))


swarm, objective = initialize_problem()
