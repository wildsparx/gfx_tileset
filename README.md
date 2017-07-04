# gfx_tileset
Library to read the ProGraphx Toolbox tileset format used in DOS games.

http://www.shikadi.net/moddingwiki/ProGraphx_Toolbox_tileset_format

These games had images such as tiles and sprite animation frames stored in tilesets.
A tileset is an array of images of the same size. The file can contain multiple tilesets.

This library lets you extract those images.

## Dependencies
  * python2
  * PIL
  
## Using

### How To Dump the Crystal Caves Tileset

```
python2 dump_crystal_caves_tiles.py /path/to/CAVES/CC1.GFX
```
This will create files like tile19-15.png, meaning the 16th tile in the 20th tileset.
Optionally, if you have ImageMagick, composite them into a sheet like this:
```
montage -geometry +0+0 tile*png all.png
# or with gridlines:
montage -geometry +1+1 tile*png all.png
```

## Tileset and File Format

A file can be padded or unpadded. Unpadded:
```
FILE = TILESET*
TILESET = HEADER + TILE*
HEADER(3 bytes) = nsprites, width_bytes, height_px
  width_pixels = width_bytes/8
TILE = OCTET[width_bytes * height_px]
  an octect is 8 horizontally consecutive pixels
OCTET(5 bytes) = alpha, blue, green, red, intensity
```


Copyright (C) 2017 Asher Blum <asher@wildsparx.com>

