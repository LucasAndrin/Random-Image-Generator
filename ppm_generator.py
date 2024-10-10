from random import randint
from img_generator import generate_image

def generate_ppm(width, height, intensity):
    def randomize_rgb():
        return ' '.join(str(randint(0, intensity)) for _ in range(3))

    generate_image(
        f'{width}x{height}x{intensity}.ppm',
        f'P3\n{width} {height}\n{intensity}\n',
        width,
        height,
        randomize_rgb
    )

generate_ppm(100, 100, 15)
generate_ppm(1000, 1000, 255)
