def generate_image(filename, signature, width, height, randomize):
    with open(f'img/{filename}', 'w') as file:
        file.write(signature)
        for _ in range(height):
            row = ' '.join(randomize() for _ in range(width))
            file.write(f'{row}\n')