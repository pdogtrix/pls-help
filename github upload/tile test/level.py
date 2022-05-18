import pygame
from support import import_csv_layout, import_cut_graphics
from settings import tile_size
from tiles import Tile, StaticTile
count = 0

class Level:
    def __init__(self, level_data, surface):
        # general setup
        self.display_surface = surface
        self.world_shift = 0 
        self.count = 0

        #terrain setup
        terrain_layout = import_csv_layout(level_data['terrain']) # import path from csv file
        self.terrain_sprites = self.create_tile_group(terrain_layout, 'terrain') #terrain specifies what texture is being loaded for the value in the terrain list

        #bg_platform setup
        bg_platform_layout = import_csv_layout(level_data['bg_platform'])
        self.bg_platform_sprites = self.create_tile_group(bg_platform_layout, 'bg_platform')


    def create_tile_group(self,layout,type):
        sprite_group = pygame.sprite.Group()

        for row_index, row in enumerate(layout): # seperates each row, gives it an index value, and then gives the values in each row
            for col_index, val in enumerate(row): #for every value in the row, assign a coloumb, and gives the values in each coloumb
                print(col_index + '\n' + val) # trying to DEBUG
                if val != '-1': # if value isn't nothing. 1 is a string because the values are imported as strings of numbers, rather than number values
                    x = col_index * tile_size
                    y = row_index * tile_size

                    if type == 'terrain':
                        terrain_tile_list = import_cut_graphics('graphics/terrain/mega tile set.png')
                        sprite = Tile(tile_size,x,y)
                        sprite_group.add(sprite)
                    

                    # if type == 'bg_platform' and (val == 74 or val == 75 or val == 76 or val == 148 or val == 149 or val == 150):
                    #     bg_platform_tile_list = import_cut_graphics('graphics/terrain/mega tile set.png')
                    #     tile_surface = bg_platform_tile_list[int(val)]
                    #     sprite = StaticTile(tile_size, x, y, tile_surface)
                    #     sprite_group.add(sprite)

   


        return sprite_group

    def run(self): # run the entire game
        self.terrain_sprites.update(self.world_shift) # moves all tiles in the desired direction
        self.terrain_sprites.draw(self.display_surface)

        #bg_platform
      #  self.bg_platform_sprites.update(self.world_shift)
       # self.bg_plaftorm_sprites.draw(self.display_surface)