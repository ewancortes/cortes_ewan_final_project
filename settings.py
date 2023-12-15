import pygame
import spritesheet
import os

pygame.init()


W, H = 1920, 1080
win = pygame.display.set_mode((W,H))
pygame.display.set_caption('Side Scroller')

bg = pygame.image.load(os.path.join('images','bg.png')).convert()
run_image = pygame.image.load('images/Solder1/Run.png').convert_alpha()
jump_image = pygame.image.load('images/Soldier1/Idle.png').convert_alpha()
run_sheet = spritesheet.SpriteSheet(run_image)
jump_sheet = spritesheet.SpriteSheet(jump_image)
BLACK = (0, 0, 0)

run1 = run_sheet.get_image(0, 24, 24, 3, BLACK)
run2 = run_sheet.get_image(1, 24, 24, 3, BLACK)
run3 = run_sheet.get_image(2, 24, 24, 3, BLACK)
run4 = run_sheet.get_image(3, 24, 24, 3, BLACK)
run5 = run_sheet.get_image(4, 24, 24, 3, BLACK)
run6 = run_sheet.get_image(5, 24, 24, 3, BLACK)
run7 = run_sheet.get_image(6, 24, 24, 3, BLACK)
run8 = run_sheet.get_image(7, 24, 24, 3, BLACK)

jump1 = jump_sheet.get_image(0, 24, 24, 3, BLACK)
jump2 = jump_sheet.get_image(1, 24, 24, 3, BLACK)
jump3 = jump_sheet.get_image(2, 24, 24, 3, BLACK)
jump4 = jump_sheet.get_image(3, 24, 24, 3, BLACK)
jump5 = jump_sheet.get_image(4, 24, 24, 3, BLACK)
jump6 = jump_sheet.get_image(5, 24, 24, 3, BLACK)

