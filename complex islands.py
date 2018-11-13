from random import randint
from opensimplex import OpenSimplex
tmp = OpenSimplex(seed=randint(1, 100000))

#Import for main program
from PIL import Image
from tkinter import filedialog
from math import sqrt


#Initialise width / height
width = 1000
height = 1000

#Import gradient picture - 200*1 image used to texture perlin noise
#R,G,B,Alpha
gradient = Image.open("image.png")
gradlist = list(gradient.getdata())

#Create new image
img = Image.new('RGBA', (width, height), color=(255, 255, 255, 255))

def pixel(x,y):
    distance = sqrt(abs(x - 3)**2 + abs(y - 3)**2)
    simplex = -distance * 1.3
    for r in range(0, 12):
        simplex += (tmp.noise2d(x * 1.28**r,y * 1.28**r) / (r+1) * 2.56)
    simplex -= 3*(abs(x - 5.8) + abs(x - 0.2) + abs(y - 5.8) + abs(y - 0.2) - 12)
    simplex -= 2*(abs(2*x - 11) + abs(2*x - 1) + abs(2*y - 11) + abs(2*y - 1) - 20)

    def NormalNew(simplex):
        #Colours
        if 0 <= simplex <= 1.1:
            return (69,107,85,255)
        elif 1.1 < simplex <= 2.5:
            return(69,83,85,255)
        elif 2.5 < simplex <= 3.2:
            return(88,88,64,255)
        elif 3.2 < simplex <= 3.8:#hgh 131 130 108
            return (99,108,84,255)
        elif 3.8 < simplex <= 4.4:
            return (106,117,108,255)
        elif 4.4 < simplex <= 5.2:
            return (112,126,131,255)
        elif simplex > 5.2:
            return (234,234,234,255)
        elif -0.13 <= simplex < 0:
            return (203,182,160,255)
        elif -0.26 <= simplex < -0.13:
            return (221,203,117,255)
        elif -0.42 <= simplex < -0.26:
            return (12,128,247,255)
        elif -0.58 <= simplex < -0.42:
            return (12,128,247,255)
        elif -1 <= simplex < -0.58:
            return (0,65,130,255)
        elif -1.5 <= simplex < -1:
            return (0,51,102,255)
        elif simplex < -1.5:
            return (0,36,72,255)
        else:
            raise Exception("This shouldn't happen Jack.")

    def NormalOld(simplex):
        # Colours
        if 0 <= simplex <= 1.1:
            return (61, 97, 10, 255)
        elif 1.1 < simplex <= 2.5:
            return (14, 84, 30, 255)
        elif 2.5 < simplex <= 3.2:
            return (59, 80, 36, 255)
        elif 3.2 < simplex <= 3.8:
            return (104, 75, 46, 255) #72 81 57
        elif 3.8 < simplex <= 4.4:
            return (84, 82, 76, 255)
        elif 4.4 < simplex <= 5.2:
            return (114, 112, 100, 255)
        elif simplex > 5.2:
            return (230, 230, 230, 255)
        elif -0.13 <= simplex < 0:
            return (255, 204, 102, 255)
        elif -0.26 <= simplex < -0.13:
            return (221, 203, 117, 255)
        elif -0.42 <= simplex < -0.26:
            return (12, 128, 247, 255)
        elif -0.58 <= simplex < -0.42:
            return (12, 128, 247, 255)
        elif 1 <= simplex < -0.58:
            return (0, 65, 130, 255)
        elif simplex < 1:
            return (0, 51, 102, 255)
        else:
            raise Exception("This shouldn't happen Jack.")

    return NormalNew(simplex)

img.putdata([pixel(x / width * 6, y / height * 6) for x in range(width) for y in range(height)])
img.save(filedialog.asksaveasfilename() + ".png", "PNG")


#img.putdata([gradlist[int(tmp.noise2d(x / width * 10, y / height * 10) * 150 + 75) - int(abs(x-(0.5 * width)) / 1.2) - int(abs(y-(0.5 * height)) / 1.2)] for x in range(width) for y in range(height)])
#print(asarray([[gradlist[int(round((octavePerlin(x, y, z, 4, 2)*100) + 100))] for x in range(width)]for y in range(height)]))
#output = Image.fromarray(asarray([[gradlist[int(round((octavePerlin(x, y, z, 4, 2)*100) + 100))] for x in range(width)]for y in range(height)]), mode='RGBA')
#output.save(filedialog.asksaveasfilename() + ".png")