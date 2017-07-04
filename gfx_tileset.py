# Copyright (C) 2017 Asher Blum
import math
from PIL import Image
from PIL import ImageDraw
import sys

HI_BIT = 128
PIXEL_WHITE = 255
PIXEL_MEDIUM = 127

def _read_octet(ifh):
  '''Read 8 pixels from 5 bytes; return 8x5 matrix of 1/0 bool'''
  pixels = []
  buf = ifh.read(5)
  buf = [ord(i) for i in buf]
  pixels = []
  for i in range(8):
    pixel = []
    for j in range(5):
      pixel.append((buf[j] & HI_BIT)/HI_BIT)
      buf[j] <<= 1
    pixels.append(pixel)
  return pixels

def _read_octet_rgb(ifh):
  '''Return 8 RGB tuples'''
  ipixels = _read_octet(ifh)
  res = []
  for pixel in ipixels:
    intens = PIXEL_WHITE if pixel[4] else PIXEL_MEDIUM 
    opixel = [] # in RGB
    for ind in [3, 2, 1]: # input is backwards
      opixel.append(pixel[ind] * intens)
    res.append(tuple(opixel)) 
  return res
    
def read_tile(width, height, ifh):
  '''Return a PIL image'''
  im = Image.new('RGB', (width*8, height))
  draw = ImageDraw.Draw(im)
  opixels = im.load()
  for i in range(height):
    for j in range(width):
      ipixels = _read_octet_rgb(ifh)
      for k, ipix in enumerate(ipixels):
        x = j*8 + k
        opixels[x, i] = ipix
  return im

def read_tile_set(ifh):
  '''Return a list<image>, all of same size'''
  mbuf = ifh.read(3)
  if len(mbuf) < 3:
    return None
  mbuf = [ord(i) for i in mbuf]
  nsprites, width_bytes, height_px = mbuf
  return [read_tile(width_bytes, height_px, ifh) for i in range(nsprites)]

def read_all_tile_sets_no_padding(ifh):
  '''Return list<list<image>>; assume no padding between tilesets'''
  tile_sets = []
  while True:
    nts = read_tile_set(ifh)
    if nts is None:
      return tile_sets
    tile_sets.append(nts)

def write_tile_set_to_pngs(prefix, tiles):
  for i , tile in enumerate(tiles):
    tile.save("%s-%d.png" % (prefix, i))

