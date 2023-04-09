import pygame
from tiles import Tile
from setting import tile_size


class Level:
    def __init__(self, level_data, surface):
        self.tiles = pygame.sprite.Group()
        self.display_surface = surface
        self.setup_level(level_data)

    def setup_level(self, layout):
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                if cell =='X':
                    x = row_index
                    y = col_index
                    tile = Tile((x, y), tile_size)
                    # noinspection PyTypeChecker
                    self.tiles.add(tile)


    def run(self):
        self.tiles.draw(self.display_surface)


