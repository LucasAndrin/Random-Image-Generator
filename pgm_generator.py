from random import randint
from img_generator import generate_image

def generate_pgm(width, height, intensity, filename):
    def randomize():
        return str(randint(0, intensity))
    
    generate_image(
        f'{width}x{height}x{intensity}.ppm',
        f'P2\n{width} {height}\n{intensity}\n',
        width,
        height,
        randomize
    )

generate_pgm(100, 100, 16, 'generated-pgm.pgm')
