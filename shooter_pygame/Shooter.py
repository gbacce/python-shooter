# Include pygame again, because this is a different file.
import pygame

class Shooter(object):
	# Remember... Classes have 2 parts. 
	# 	1. Attributes
	# 	2. Methods
	# Initiate the starting attributes with __init__
	def __init__(self, screen):
		# It is a good idea to create a variable referring to the character's image. 
		# That way, you can call Shooter.image later in the code instead of writing out pygame.image.load(image). Much easier.
		# Best practice is to start the pathway with ./
		self.image = pygame.image.load('./images/Hero.png')
		# Image is too big. So resize the image. Play with the dimensions as much as you want.
		self.image = pygame.transform.scale(self.image,(207,250))
		self.x = 100
		self.y = 100
		# A screen has to be passed in (not optional) so that the hero can be drawn, since it is part of the draw_me() method.
		# Self.screen will point back to the screen that was created in the main program. 
		self.screen = screen

	# After initiating attributes, define some methods.
	def draw_me(self, screen):
		screen.blit(self.image,[self.x,self.y])

	# Alternatively, this method could be written as:
	# 
	# def draw_me(self):
	# 	self.screen.blit(self.image,[self.x,self.y])
	# 
	# It's cleaner, but less explicit.