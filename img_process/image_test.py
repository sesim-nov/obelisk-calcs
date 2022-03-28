import grid_gen
from PIL import Image, ImageDraw
from math import pi

if __name__ == "__main__":
    im = Image.open("../../vid/frame_0001.jpg")
    draw = ImageDraw.Draw(im)

    grid = grid_gen.make_grid([37.5,36.5], -1.5*pi/180, [835,435])
    for pt in grid: 
        pixel_value = im.getpixel(tuple(pt))
        pixel_norm = sum(pixel_value)
        print("{} -- {}".format(pixel_value, pixel_norm))
        color = (255,0,0) if pixel_norm > 500 else (255,255,0)
        draw.regular_polygon((*pt, 8), 3, rotation=30, fill=color)

    im.save("/tmp/alignment-test.jpg")
    im.show()

