import random

def generate_pbm(width, height, filename):
    with open(filename, 'w') as file:
        file.write(f'P1\n{width} {height}\n')
        for _ in range(height):
            row = ' '.join(str(random.randint(0, 1)) for _ in range(width))
            file.write(f'{row}\n')

generate_pbm(100, 100, 'generated-pbm.pbm')    
