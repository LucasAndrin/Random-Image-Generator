def generate_heart(width, height, filename):
    data = f'P1\n{width} {height}\n'
    
    def inside_of_heart(x, y):
        x = (x - width // 2) / (width // 2)
        y = (y - height // 3) / (height // 3)
        return (x**2 + y**2 - 1)**3 - x**2 * y**3 <= 0

    for y in range(height):
        row = ''
        for x in range(width):
            if inside_of_heart(x, y):
                row += '1 '
            else:
                row += '0 '
        data += row.strip() + '\n'

    with open(filename, 'w') as file:
        file.write(data)

width = 100
height = 100
filename = 'heart.pbm'

generate_heart(width, height, filename)