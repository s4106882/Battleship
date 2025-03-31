import random

visual_grid = []
for i in range(10):
    visual_grid.append(['~'] * 10)

def print_grid():
    print(f'{" ":^4}', end='')
    for x in range(1, 11):
        print(f'{x:^4}', end='')
    print()
    for y in range(10):
        print(f'{y + 1:^4}', end='')
        for x in range(10):
            print(f'{visual_grid[y][x]:^4}', end='')
        print()
print_grid()

def create_grid():
    coords_list = []
    for x in range(1, 11):
        for y in range(1, 11):
            coords = (x, y)
            coords_list.append(coords)
    return coords_list
    
def update_grid(coordinate, hit):
    x, y = coordinate
    if hit == True:
        visual_grid[y - 1][x - 1] = 'X'
        print_grid()
    else:
        visual_grid[y - 1][x - 1] = 'O'
        print_grid()

def enemy_ship(grid):
    grid_copy = grid[:]
    ranges = [(0, 5), (0, 4), (0, 3), (0, 3), (0, 2)]
    picked_spots = []
    prev_x, prev_y = 0, 0
    for start, end in ranges:
        ships = list(range(start, end))
        i = 0
        prev_x, prev_y = random.randint(1, 10), random.randint(1, 10)
        while i < len(ships):
            x = random.randint(1, 10)
            y = random.randint(1, 10)
            random_coord = (x, y)
            if random_coord in grid_copy:
                if (((x == prev_x + 1) or (x == prev_x - 1)) and (y == prev_y)) or (((y == prev_y + 1) or (y == prev_y - 1)) and (x == prev_x)) or len(picked_spots) == 0:
                    prev_x = x
                    prev_y = y
                    picked_spots.append(random_coord)
                    grid_copy.remove(random_coord)
                    i+=1
    return picked_spots

def user_coord(enemy_pos):
    hit = None
    while True:
        user_coordinate = (int(input()), int(input()))
        x, y = user_coordinate
        if (x > 10 or x < 1) or (y > 10 or y < 1):
            print('Coordinate out of range.')
        elif user_coordinate not in grid:
            print('Coordinate already guessed.')
        else:
            break
    if user_coordinate in enemy_pos:
        hit = True
        print('A hit, cap\'n!')
        update_grid(user_coordinate, hit)
        enemy_position.remove(user_coordinate)
        return user_coordinate
    else:
        hit = False
        print('A miss! Work harder ya scallywags!')
        update_grid(user_coordinate, hit)
        return user_coordinate

grid = create_grid()
enemy_position = enemy_ship(grid)

def main():
    while len(enemy_position) > 0:
        user_coordinate = user_coord(enemy_position)
        grid.remove(user_coordinate)
        
        if len(enemy_position) == 0:
            print('Congrats, Captain! We got them all!')
main()