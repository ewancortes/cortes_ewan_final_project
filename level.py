# This File was Created By Ewan Cortes

# Import randint from random and Surface from pygame
from random import randint
from pygame import Surface
import pygame as pg

# Import "asyncio"
# Asyncio is a Python library that's used to write concurrent code with async and await syntax. 
# It's used primarily in I/O-bound tasks, such as web page development or fetching data from APIs.
import asyncio

# Import the required files for the level
from singleton import Singleton
from sprite import Sprite
import settings as config

# This will return True when there is a change of: P(X=True)=1/x
chance = lambda x: not randint(0,x)


# This class sets up the bonus sprite
class Bonus(Sprite):
	
	WIDTH = 15
	HEIGHT = 15

	def __init__(self, parent:Sprite,color=config.GRAY,
			force=config.PLAYER_BONUS_JUMPFORCE):

		self.parent = parent
		super().__init__(*self._get_inital_pos(),
			Bonus.WIDTH, Bonus.HEIGHT, color)
		self.force = force
	
	def _get_inital_pos(self):
		x = self.parent.rect.centerx - Bonus.WIDTH//2
		y = self.parent.rect.y - Bonus.HEIGHT
		return x,y


# This class will represent the platforms in the game and inherits the Sprite class
# Should only be instantiated by a Level instance
# Can have a bonus spring or broke on player jump
class Platform(Sprite):
	
	# This will override the inherited (constructor: Sprite.__init__)
	def __init__(self, x:int, y:int, width:int, height:int,
			initial_bonus=False,breakable=False):

		color = config.PLATFORM_COLOR
		if breakable:color = config.PLATFORM_COLOR_LIGHT
		super().__init__(x,y,width,height,color)


		self.breakable = breakable
		self.__level = Level.instance
		self.__bonus = None
		if initial_bonus:
			self.add_bonus(Bonus)

	# This is a getter for __bonus if it is Public so it remains private
	@property
	def bonus(self):return self.__bonus

    # This function will safely add a bonus to the platform
    # Parameter: bonus_type determines the type of bonus to add
	def add_bonus(self,bonus_type:type) -> None:
		assert issubclass(bonus_type,Bonus), "Not a valid bonus type !"
		if not self.__bonus and not self.breakable:
			self.__bonus = bonus_type(self)
	
    # This function will safely remove a platform's bonus after if it is captured or screen
	def remove_bonus(self) -> None:
		self.__bonus = None

    # This function is called in update if a player collides with something (this is safe to override)
	def onCollide(self) -> None:
		if self.breakable:
			self.__level.remove_platform(self)

		
	# This function overrides inheritance: Sprite.draw()
    # Similar to Sprite.draw() this function draws the platform's bonus if it has one
    # Parameter: surface pygame.Surface creates the surface to draw on
	def draw(self, surface:Surface) -> None:
		# check if out of screen: should be deleted
		super().draw(surface)
		if self.__bonus:
			self.__bonus.draw(surface)
		if self.camera_rect.y+self.rect.height>config.YWIN:
			self.__level.remove_platform(self)




# This class is used to represent the level the player is on
# Used to manage updates and the creation of platforms 
# (Can be accessed through "Singleton")
class Level(Singleton):
	
	# This is a constructor called on the new instance: Level()
	def __init__(self):
		self.platform_size = config.PLATFORM_SIZE
		self.max_platforms = config.MAX_PLATFORM_NUMBER
		self.distance_min = min(config.PLATFORM_DISTANCE_GAP)
		self.distance_max = max(config.PLATFORM_DISTANCE_GAP)

		self.bonus_platform_chance = config.BONUS_SPAWN_CHANCE
		self.breakable_platform_chance = config.BREAKABLE_PLATFORM_CHANCE

		self.__platforms = []
		self.__to_remove = []

		self.__base_platform = Platform(
			config.HALF_XWIN - self.platform_size[0]//2,# X POSITION OF THE PLATFORMS
			config.HALF_YWIN + config.YWIN/3, #           Y POSITION OF THE PLATFORMS
			*self.platform_size)#                               SIZE OF THE PLATFORMS
	

	# This is a getter for __platforms if it is Public so it remains private
	@property
	def platforms(self) -> list:
		return self.__platforms

    # This is an asynchronous management of the creation of platforms
	async def _generation(self) -> None:
		
		# This will check how many platforms are needed to be created
		nb_to_generate = self.max_platforms - len(self.__platforms)
		for _ in range(nb_to_generate):
			self.create_platform()
		

    # This function will create the first platform or a new platform
	def create_platform(self) -> None:
		if self.__platforms:
			# This will generate a new platform with a random location:
			# Set the X POSITION along the screen WIDTH
			# Set the Y POSITION starting from last platform y pos +random offset
			offset = randint(self.distance_min,self.distance_max)
			self.__platforms.append(Platform(
				randint(0,config.XWIN-self.platform_size[0]),#       X POSITION OF PLATFORMS
				self.__platforms[-1].rect.y-offset,#                 Y POSITION OF PLATFORMS
				*self.platform_size, #                                     SIZE OF PLATFORMS
				initial_bonus=chance(self.bonus_platform_chance),# This sets up platforms with bonuses
				breakable=chance(self.breakable_platform_chance))),#  This sets up breakable platforms
		else:
			# Just in case there are no platforms this will set up a base one
			self.__platforms.append(self.__base_platform)


    # This function will remove platforms
    # Parameter: plt Platform removes platforms
    # The return boolean returns True if a platform is removed successfully
	def remove_platform(self,plt:Platform) -> bool:
		if plt in self.__platforms:
			self.__to_remove.append(plt)
			return True
		return False


    # This function is only called when the game restarts or the player dies
	def reset(self) -> None:
		self.__platforms = [self.__base_platform]


    # This function is called every frame in the main game loop for the creation of new platforms
	def update(self) -> None:
		for platform in self.__to_remove:
			if platform in self.__platforms:
				self.__platforms.remove(platform)
		self.__to_remove = []
		asyncio.run(self._generation())


    # This function is called every frame in the main loop and draws each platform
    # Parameter: surface pygame.Surface creates the surface to draw on
	def draw(self,surface:Surface) -> None:
		for platform in self.__platforms:
			platform.draw(surface)