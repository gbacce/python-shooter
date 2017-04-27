import pygame
# Import the sys module so we can exit the program.
# Once we move the code and import sys in the game_functions page, we can take it out of the game.py page since the part of the code that uses it is now on this page.
import sys

def check_events():


	###This was originally in the main while loop when we first stared writing the code, but we moved it to the game_functions page to clean up the code.
		# The escape hatch from the while loop
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				# The user clicked the red x. Get out of the loop and kill the game.
				sys.exit()