from csv import reader # allows to read csv file
import pygame
from settings import tile_size

def import_csv_layout(path): # defines function for importing the terrain
    terrain_map = []
    with open(path) as map: # opens path as a map function
        level = reader(map, delimiter = ',')
        for row in level:
            terrain_map.append(list(row)) # adds row data to terrain list as a list
        return terrain_map


def import_cut_graphics(path):
    surface = pygame.image.load(path).convert_alpha() # loads image based on whatever texture path is used
    tile_num_x = int(surface.get_size()[0] / tile_size) # finds width of image and cuts into appropriate tile sizez
    tile_num_y = int(surface.get_size()[1] / tile_size)     # finds height of image and cuts into appropriate tile sizes


    cut_tiles = []
    for row in range(tile_num_y):
        for col in range(tile_num_x):
            x = col * tile_size
            y = row * tile_size
            new_surf = pygame.Surface((tile_size, tile_size)) #creates new, blank surface of 64x64
            new_surf.blit(surface, (0,0), pygame.Rect(x,y,tile_size,tile_size)) #blits image on to the new surface (only the small piece that we wanted to use)
            cut_tiles.append(new_surf)

    return cut_tiles


