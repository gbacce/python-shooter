# The reason you have access to this module is because you reason
# $ pip install pygame
# Pygame is NOT a core module (unlike math or random)
import pygame
# Import the Shooter class from shooter.
from Shooter import Shooter
# Import the check_events function that replaces some code in the main game loop.
from game_functions import check_events

# The core game functionality/loop. This is where everything lives initially.
def run_game():
	# Init all of the pygame code
	pygame.init()
	# Set up a tuple for the screen size (horizontal,vertical)
	screen_size = (1000,800)
	# Set up a tuple for the background color
	background_color = (82,111,53)

	# Set a caption on the terminal window
	pygame.display.set_caption("Python Shooter")

	# Create a pygame screen to use
	screen = pygame.display.set_mode(screen_size)
	# Instantiate a shooter object
	the_shooter = Shooter(screen)

	# Main game loop. Runs forever... (or until it sees a break)
	while 1:
		screen.fill(background_color)

		check_events()

		# Draw the shooter
		the_shooter.draw_me(screen)

		# Clear the screen for the next time through the loop.
		pygame.display.flip()

# Run the game code
run_game()