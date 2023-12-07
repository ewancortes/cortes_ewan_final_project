import pygame as pg
import os

W, H = 800, 437
win = pg.display.set_mode((W,H))
pg.display.set_caption('Side Scroller')

bg = pg.image.load(os.path.join('images','DinoWallpaper.png')).convert()
bgX = 0
bgX2 = bg.get_width()


run = [pg.image.load(os.path.join('images', str(x) + '.png')) for x in range(8,16)]
jump = [pg.image.load(os.path.join('images', str(x) + '.png')) for x in range(1,8)]
slide = [pg.image.load(os.path.join('images', 'DinoDuck1.png')),
         pg.image.load(os.path.join('images', 'DinoDuck2.png')),
         pg.image.load(os.path.join('images', 'DinoDuck2.png')),
         pg.image.load(os.path.join('images', 'DinoDuck2.png')), 
         pg.image.load(os.path.join('images', 'DinoDuck2.png')),
         pg.image.load(os.path.join('images', 'DinoDuck2.png')), 
         pg.image.load(os.path.join('images', 'DinoDuck2.png')),
         pg.image.load(os.path.join('images', 'DinoDuck2.png')), 
         pg.image.load(os.path.join('images', 'DinoDead.png')),
         pg.image.load(os.path.join('images', 'DinoDead.png')), 
         pg.image.load(os.path.join('images', 'DinoStart.png'))
         ]
fall = pg.image.load(os.path.join('images','DinoDead.png')) # NEW

rotate = [pg.image.load(os.path.join('images', 'LargeCactus1.PNG')),
          pg.image.load(os.path.join('images', 'LargeCactus2.PNG')),
          pg.image.load(os.path.join('images', 'SmallCactus1.PNG')),
          pg.image.load(os.path.join('images', 'SmallCactus2.PNG'))
          ]


img = pg.image.load(os.path.join('images', 'Bird1.png'))

jumpList = [1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,-1,-1,-1,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4]