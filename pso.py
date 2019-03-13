from swarm import *

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

def optimize_problem(swarm, objective):
	print("Starting optimization problem...\nOptimization problem objective : [{}, {}, {}]\n"
		.format(objective[0], objective[1], objective[2]))
	
	iteration_number = 0
	while swarm.has_finished_searching(objective, iteration_number) == False:
		iteration_number += 1

	print(iteration_number)


swarm, objective = initialize_problem()
optimize_problem(swarm, objective)
