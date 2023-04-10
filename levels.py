import pygame
from tiles import Tile
from setting import tile_size
from Player import Player


class Level:
    def __init__(self, level_data, surface):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0

    def setup_level(self, layout):
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * (.5 * tile_size)
                y = row_index * (.5 * tile_size)
                if cell == 'X':
                    tile = Tile((x, y), tile_size)
                    # noinspection PyTypeChecker
                    self.tiles.add(tile)
                if cell == 'P':
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)

    def run(self):
        #level tiles
        self.tiles.update(0)
        self.tiles.draw(self.display_surface)

        #player
        self.player.draw(self.display_surface)
