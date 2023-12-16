import pygame
import spritesheet
import os

pygame.init()



run_image = pygame.image.load('Run.png').convert_alpha()
jump_image = pygame.image.load('Idle.png').convert_alpha()
slide_image = pygame.image.load('Shot_2.png').convert_alpha()
run_sheet = spritesheet.SpriteSheet(run_image)
jump_sheet = spritesheet.SpriteSheet(jump_image)
slide_sheet = spritesheet.SpriteSheet(slide_image)
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

slide1 = slide_sheet.get_image(0, 24, 24, 3, BLACK)
slide2 = slide_sheet.get_image(1, 24, 24, 3, BLACK)
slide3 = slide_sheet.get_image(2, 24, 24, 3, BLACK)
slide4 = slide_sheet.get_image(3, 24, 24, 3, BLACK)

