from random import randint
from img_generator import generate_image

def generate_pbm(width, height, filename):
    def randomize():
        return str(randint(0, 1))
    
    generate_image(
        filename,
        f'P1\n{width} {height}\n',
        width,
        height,
        randomize
    )

generate_pbm(100, 100, 'generated-pbm.pbm')
