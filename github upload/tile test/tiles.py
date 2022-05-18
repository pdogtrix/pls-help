import pygame

class Tile (pygame.sprite.Sprite): 
    def __init__(self, size, x, y): # makes a tile with the attributes given
        super().__init__() #initialize and inherrit proper sprite information
        self.image = pygame.Surface((size, size))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = (x, y))

    def update(self, shift):
        self.rect.x += shift # shifts all tiles 


class StaticTile(Tile): # inherits from Tile class
    def __init__(self, size, x, y, surface):
        super().__init__(size, x, y)
        self.image = surface