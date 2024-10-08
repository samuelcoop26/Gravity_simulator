import pygame
import time
from physics import Physics

class Simulation:
	physics=Physics()

	def __init(self):
		self.run, self.space, self.bodies = None, None, None
	
	def environment(self, body_list):
		self.bodies = body_list
		space_plane_size = (1000, 800)  # width, height of canvas
		self.run = True

	# setting up pygame
		pygame.init()
		pygame.display.set_caption("Orbit simulator")
		self.space = pygame.display.set_mode(space_plane_size)

    # setting up physics engine
		self.physics.define_bodies(body_list)

	def show_environment(self):
		while self.run:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.run = False

			self.space.fill((0, 0, 0))

			net_force = self.physics.force()
			for i, body in enumerate(self.bodies):
				body.force = net_force[i]

			for body in self.bodies:
				body.draw(self.space)

			for body in self.bodies:
				body.move()        
			
			time.sleep(0.0005)
			pygame.display.update()
