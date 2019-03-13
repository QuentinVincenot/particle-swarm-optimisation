from swarm import *

import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation


def initialize_plot(swarm, objective):
	plt.ion()
	fig = plt.figure(figsize=(10, 7))
	ax = p3.Axes3D(fig)

	particles_positions_x = []
	particles_positions_y = []
	particles_positions_z = []
	for i in range(len(swarm.particles)):
		particle_i = swarm.particles[i]
		particle_i_position = particle_i.position
		particles_positions_x += [particle_i_position[0, 0]]
		particles_positions_y += [particle_i_position[1, 0]]
		particles_positions_z += [particle_i_position[2, 0]]

	scatterplot = ax.scatter(particles_positions_x, particles_positions_y, particles_positions_z, marker="1",
		color="g", s=50)
	ax.scatter([objective[0]], [objective[1]], [objective[2]], marker="*", color="r", s=100)

	ax.set_xlim3d([0, 1000])
	ax.set_ylim3d([0, 1000])
	ax.set_zlim3d([0, 1000])
	ax.set_xlabel('X')
	ax.set_ylabel('Y')
	ax.set_zlabel('Z')
	ax.set_title('Particle Swarm Optimization (PSO)')
	plt.show()

	return plt, fig, scatterplot

def update_plot(plt, fig, scatterplot, swarm):
	particles_positions_x = []
	particles_positions_y = []
	particles_positions_z = []
	for i in range(len(swarm.particles)):
		particle_i = swarm.particles[i]
		particle_i_position = particle_i.position
		particles_positions_x += [particle_i_position[0, 0]]
		particles_positions_y += [particle_i_position[1, 0]]
		particles_positions_z += [particle_i_position[2, 0]]

	plt.pause(0.01)
	scatterplot._offsets3d = (particles_positions_x, particles_positions_y, particles_positions_z)
	fig.canvas.draw()
