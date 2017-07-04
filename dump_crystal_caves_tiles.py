# Copyright (C) 2017 Asher Blum
import gfx_tileset
import sys

if __name__ == '__main__':
  ifn = sys.argv[1]
  tile_sets = gfx_tileset.read_all_tile_sets_no_padding(open(ifn))
  for i, tiles in enumerate(tile_sets):
    prefix = "tile%d" % i
    gfx_tileset.write_tile_set_to_pngs(prefix, tiles)

