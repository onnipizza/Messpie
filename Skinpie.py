import random
from PIL import Image

def generate_random_image():
    img = Image.new("RGB", (64, 64), (255, 255, 255))
    pixels = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pixels[i, j] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return img

img = generate_random_image()
img.save("64x64.png")