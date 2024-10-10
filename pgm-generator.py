import random

def generate_pgm(width, height, shades, filename):
    with open(filename, 'w') as file:
        file.write(f'P2\n{width} {height}\n{shades}\n')
        for _ in range(height):
            row = ' '.join(str(random.randint(0, 1)) for _ in range(width))
            file.write(f'{row}\n')

generate_pgm(100, 100, 16, 'generated-pgm.pgm')
