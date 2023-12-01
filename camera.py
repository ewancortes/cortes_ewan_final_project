from pygame import Rect
from pygame.sprite import Sprite

from singleton import Singleton
import settings as config

class Camera(Singleton):

	def __init__(self, lerp=5,width=config.XWIN, height=config.YWIN):
		self.state = Rect(0, 0, width, height)
		self.lerp = lerp
		self.center = width//2
		self.maxdistance = self.center

	def reset(self) -> None:
		self.state.y = 0
		self.maxdistance = self.center

	def apply_rect(self,rect:Rect) -> Rect:
		return rect.move((0,-self.state.topleft[1]))

	def apply(self, target:Sprite) -> Rect:
		return self.apply_rect(target.rect)
	

	def update(self, target:Rect) -> None:
		if(target.y<self.maxdistance):
			self.lastdistance = self.maxdistance
			self.maxdistance = target.x
		speed = ((self.state.y+self.center)-self.maxdistance)/self.lerp
		self.state.x-=speed
