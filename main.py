# This file was created by Ewan Cortes

# TITLE = Soldier Runner

# Goals
'''
Create a game like the google dinasour game in which the player has to make it
as far as possible along the track going right

However, change the overall design and add mobs

Mobs will try to attack the player as he moves across the screen

The player will be able to shoot at the mobs but will have to do so before the 
player gets off screen

The player gets off screen by staying still as the ground moves (left) or player moves right
''' 

import pygame as pg
from singleton import Singleton
from camera import Camera
from level import *
import settings as config


class game(Singleton):
    def __init__(self) -> None:
        self.alive = True
        self.window = pg.display.set_mode(config.DISPLAY,config.FLAGS)
		self.clock = pg.time.Clock()
        self.camera = Camera()
		self.lvl = Level()
		self.player = Player(
			config.HALF_XWIN - config.PLAYER_SIZE[0]/2,# X POS
			config.HALF_YWIN + config.HALF_YWIN/2,#      Y POS
			*config.PLAYER_SIZE,# SIZE
			config.PLAYER_COLOR#  COLOR
		)

        self.score_pos = pg.math.Vector2(10,10)

		self.gameover_txt = config.LARGE_FONT.render("Game Over",1,config.GRAY)
		self.gameover_rect = self.gameover_txt.get_rect(
			center=(config.HALF_XWIN,config.HALF_YWIN))
		
        def close(self):
		self.alive = False
		

        def reset(self):
		self.camera.reset()
		self.lvl.reset()
		self.player.reset()
		
        def events(self):
		########## User Events ##########
		for event in pg.event.get():
			if event.type == pg.QUIT:
				self.close()
			elif event.type == pg.KEYDOWN:
				if event.key == pg.K_ESCAPE:
					self.close()
				if event.key == pg.K_RETURN and self.player.dead:
					self.reset()
			self.player.handle_event(event)
			
        # Sets up how the game updates
	def update(self):
		########## UPDATE ##########
		self.player.update()
		self.lvl.update()

		if not self.player.dead:
			self.camera.update(self.player.rect)
			# This will calculate score and update UI txt
			self.score = - self.camera.state.y//50
			self.score_txt = config.SMALL_FONT.render(
				str(self.score)+" m", 1, config.GRAY)
	
    # Sets up the display
	def render(self):
		self.window.fill(config.YELLOW)
		self.lvl.draw(self.window)
		self.player.draw(self.window)

		# This is more user interface
		if self.player.dead:
			self.window.blit(self.gameover_txt,self.gameover_rect)# gameover txt
		self.window.blit(self.score_txt, self.score_pos)# score txt

		pg.display.update()# This will allow the window to update allowing for camera scrolling
		self.clock.tick(config.FPS)# This sets up the tick rate and FPS

    # Set up the main game loop
	def run(self):
		############### MAIN GAME LOOP ###############
        while self.__alive:
			self._event_loop()
			self._update_loop()
			self._render_loop()
		pg.quit()



# This starts the game through this "if" statement
if __name__ == "__main__":
	########## PROGRAM STARTS HERE ##########
	game = Game()
	game.run()
