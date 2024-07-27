# Import necessary libraries

import pygame
import sys
import random
import math
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Angry Birds")

# Load bird images
player_bird_image = pygame.image.load("E:\SEMESTER 8\Computer Graphics\lab\pird.png").convert_alpha() # Replace path if needed
enemy_bird_image = pygame.image.load("E:\SEMESTER 8\Computer Graphics\lab\pig.png").convert_alpha() # Replace path if needed 
crash_sound = pygame.mixer.Sound("E:\SEMESTER 8\Computer Graphics\lab\8d82b5_Angry_Birds_Rio_Rock_Collision_Sound_Effect.mp3")
game_sound = pygame.mixer.Sound("E:\SEMESTER 8\Computer Graphics\lab\Cherry Blossom Theme - Angry Birds Seasons (2012).mp3")
game_over_sound = pygame.mixer.Sound("E:\SEMESTER 8\Computer Graphics\lab\cvideogame-death-sound-43894.mp3")
win_sound = pygame.mixer.Sound("E:\SEMESTER 8\Computer Graphics\lab\level-up-47165.mp3")
sling_sound = pygame.mixer.Sound("E:\SEMESTER 8\Computer Graphics\lab\8d82b5_Angry_Birds_Slingshot_Stretched_Sound_Effect.mp3")

def playsoundwin():
	win_sound.play(0,2,0)

def playsoundlose():
	game_over_sound.play(0,2,0)

# Load background image
background_image = pygame.image.load("E:\SEMESTER 8\Computer Graphics\lab\Cherry_Blossom_background.webp") # Replace path if needed

# Scale the background image to fit the screen dimensions
#background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Bird class
class Bird(pygame.sprite.Sprite):
	def __init__(self, x, y, image, scale):
		super().__init__()
		#self.image = image
		self.image = pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
		self.mask = pygame.mask.from_surface(self.image)  # Create a mask from the image
		self.velocity = [0, 0]
		self.dragging = False
		self.drag_start_pos = (0, 0)

	def update(self):
		if self.dragging:
			mouse_pos = pygame.mouse.get_pos()
			self.rect.centerx = mouse_pos[0]
			self.rect.centery = mouse_pos[1]
		else:
			self.rect.x += self.velocity[0]
			self.rect.y += self.velocity[1]

	def start_drag(self):
		self.dragging = True
		self.drag_start_pos = self.rect.center

	def end_drag(self):
		self.dragging = False
		mouse_pos = pygame.mouse.get_pos()
		direction = math.atan2(self.drag_start_pos[1] - mouse_pos[1], self.drag_start_pos[0] - mouse_pos[0])
		speed = 15
		self.velocity = [speed * math.cos(direction), speed * math.sin(direction)]

	def hit_enemy(self):
		global score
		score += 100 # Increase the score by 100 when an enemy is hit

# Button class
class Button(pygame.sprite.Sprite):
	def __init__(self, x, y, image, action, scale):
		super().__init__()
		self.image = pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.mask = pygame.mask.from_surface(self.image)  # Create a mask from the image
		self.action = action

# Create player bird
player_bird = Bird(100, SCREEN_HEIGHT // 2, player_bird_image , 0.3)


# Create enemy birds
enemy_birds = pygame.sprite.Group()
for _ in range(10):
	x = random.randint(SCREEN_WIDTH // 2, SCREEN_WIDTH - 50)
	y = random.randint(50, SCREEN_HEIGHT - 50)
	enemy_bird = Bird(x, y, enemy_bird_image,0.3)
	enemy_birds.add(enemy_bird)

# Calculating button positions 
button_margin = 10
button_top = button_margin
button_left = button_margin
button_spacing = 5

# Initialize player's score
score = 0

# Calculate 1 inch offset in pixels (assuming standard DPI of 96)
score_position = (800, 50)

# Create buttons
quit_button_image = pygame.image.load("E:\SEMESTER 8\Computer Graphics\lab\exit7.png").convert_alpha()	 # Replace path if needed
refresh_button_image = pygame.image.load("E:\SEMESTER 8\Computer Graphics\lab\qresfresh4-removebg-preview.png") .convert_alpha()# Replace path if needed

quit_button = Button(button_left, button_top + 30, quit_button_image, "quit",0.35)
refresh_button = Button(button_left + quit_button_image.get_width()-100 + button_spacing, button_top, refresh_button_image, "refresh",0.3)

# Game loop
clock = pygame.time.Clock()

# Initialize game state
try_again_counter = 0
max_try_again = 3
level_cleared = False
game_over = False

while True:
	for event in pygame.event.get():
		game_sound.play()
		
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		# ... (Event handling code for buttons and player bird dragging remains the same)
		if event.type == pygame.MOUSEBUTTONDOWN:
			if quit_button.rect.collidepoint(event.pos):
				# Quit button clicked - exit the game
				pygame.quit()
				sys.exit()

			elif refresh_button.rect.collidepoint(event.pos):
				# Refresh button clicked - reset game
				player_bird.rect.center = (100, SCREEN_HEIGHT // 2) # Reset player bird position
				player_bird.velocity = [0, 0]

				enemy_birds.empty()
				for _ in range(10):
					x = random.randint(SCREEN_WIDTH // 2, SCREEN_WIDTH - 50)
					y = random.randint(50, SCREEN_HEIGHT - 50)
					enemy_bird = Bird(x, y, enemy_bird_image,0.3)
					enemy_birds.add(enemy_bird)

				# Reset flags
				level_cleared = False
				game_over = False
				try_again_counter = 0
				score = 0

			elif player_bird.rect.collidepoint(event.pos):
				# Player bird clicked - start dragging
				sling_sound.play()
				player_bird.start_drag()

		elif event.type == pygame.MOUSEBUTTONUP:
			if player_bird.dragging:
				# Release the player bird
				player_bird.end_drag()
				sling_sound.stop()

				if not hits:
					try_again_counter += 1 # Increment try_again_counter when no hits occur
			else:
				break

	# Update enemy bird positions and collisions
	hits = pygame.sprite.spritecollide(player_bird, enemy_birds, True)

	if hits:
		crash_sound.play()
		for hit_enemy in hits:
			hit_enemy.hit_enemy() 
	crash_sound.stop()
	# Call hit_enemy method to update score and reset enemy position

	# Reset enemy birds that go out of the screen
	for enemy_bird in enemy_birds:
		if enemy_bird.rect.right < 0:
			enemy_bird.rect.left = SCREEN_WIDTH
			enemy_bird.rect.top = random.randint(50, SCREEN_HEIGHT - 50)

	# Reset player bird to origin position if it goes out of the screen
	if player_bird.rect.left > SCREEN_WIDTH or player_bird.rect.right < 0 or \
			player_bird.rect.top > SCREEN_HEIGHT or player_bird.rect.bottom < 0:
		player_bird.rect.center = (100, SCREEN_HEIGHT // 2)
		player_bird.velocity = [0, 0]

	# Clear the screen and draw the background
	screen.blit(background_image, (0, 0))

	# Update and draw player bird
	player_bird.update()
	screen.blit(player_bird.image, player_bird.rect)

	# Update and draw enemy birds
	enemy_birds.update()
	enemy_birds.draw(screen)

	# Display font
	font = pygame.font.Font(None, 50)

	# Score font
	score_font = pygame.font.Font(None, 36)

	# Draw and update player's score
	score_text = score_font.render(f"Score: {score}", True, (0, 0, 0))
	screen.blit(score_text, score_position) # Display score at specified position

	# Draw buttons
	screen.blit(quit_button.image, quit_button.rect)
	screen.blit(refresh_button.image, refresh_button.rect)


# Display "Level Cleared" if score is 500
	if score >= 1000:
		level_cleared_text = font.render("LEVEL CLEARED", True, (0, 0, 0))
		text_rect = level_cleared_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
		screen.blit(level_cleared_text, text_rect)
		level_cleared = True # Update the level_cleared flag
		#game_sound.stop()
		#playsoundwin()

	
	if score == 0 and try_again_counter >= max_try_again:
		game_over_text = font.render("GAME OVER - REPLAY", True, (0, 0, 0))
		text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
		screen.blit(game_over_text, text_rect)
		game_over = True # Update the game_over flag
		#game_sound.stop()
		#playsoundlose()

	pygame.display.flip()
	clock.tick(60)

pygame.quit()
