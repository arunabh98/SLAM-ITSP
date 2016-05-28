map_environment = [[0 for i in range(10)] for j in range(10)]
block_visit_frequency = [[0 for i in range(10)] for j in range(10)]
'''
The first two values in bot coordinates stand for x and y values.
The third value denotes the direction in which the bot is facing.
0 stands for North, 1 for East, 2 for South, 3 for West
'''
bot_coordinates = [0, 0, 0]
obstacle_threshold = 0.5
map_width = 10


def get_block_coordinate(bot_coordinates, direction):
    if direction == 0:
        return [bot_coordinates[0] - 1, bot_coordinates[1]]
    if direction == 1:
        return [bot_coordinates[0], bot_coordinates[1] + 1]
    if direction == 2:
        return [bot_coordinates[0] + 1, bot_coordinates[1]]
    if direction == 3:
        return [bot_coordinates[0], bot_coordinates[1] - 1]

def block_frequency_coordinate(coordinates):
    return block_visit_frequency[coordinates[0]][coordinates[1]]


def move(map_environment, block_visit_frequency, bot_coordinates):
    possible_direction = []
    for i in [0, 1]:
        if map_environment[bot_coordinates[0] + i][bot_coordinates[1] + int(not i)] < obstacle_threshold:
            if i == 0:
                possible_direction.append(1)
            else:
                possible_direction.append(2)
        if map_environment[bot_coordinates[0] - i][bot_coordinates[1] - int(not i)] < obstacle_threshold:
            if i == 0:
                possible_direction.append(3)
            else:
                possible_direction.append(0)
    print possible_direction
    min_frequency_blocks_direction = []
    min_frequency_blocks = []
    possible_block_coordinates = []
    for direction in possible_direction:
        possible_block_coordinates.append(get_block_coordinate(bot_coordinates, direction))
    print possible_block_coordinates
    block_frequency_list = []
    for block_coordinate in possible_block_coordinates:
        block_frequency_list.append(block_frequency_coordinate(block_coordinate))
    print block_frequency_list
    min_block_frequency = min(block_frequency_list)
    counter = 0
    for block_frequency in block_frequency_list:
        if block_frequency == min_block_frequency:
            min_frequency_blocks.append(possible_block_coordinates[counter])
            min_frequency_blocks_direction.append(possible_direction[counter])
        counter += 1
    print min_frequency_blocks_direction
    possible_heading_direction = []
    for direction in min_frequency_blocks_direction:
        if direction == bot_coordinates[2]:
            possible_heading_direction.append('F')
        elif abs(bot_coordinates[2] - direction) == 1:
            if bot_coordinates[2] - direction == 1:
                possible_heading_direction.append('L')
            elif bot_coordinates[2] - direction == -1:
                possible_heading_direction.append('R')
        elif abs(bot_coordinates[2] - direction) == 3:
            if bot_coordinates[2] - direction == -3:
                possible_heading_direction.append('L')
            elif bot_coordinates[2] - direction == 3:
                possible_heading_direction.append('R')
        elif abs(bot_coordinates[2] - direction) == 2:
            possible_heading_direction.append('U')
    print possible_heading_direction
# TEST
map_environment = [[0, 0, 0, 0],
                   [0, 0, 1, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0]]
block_visit_frequency = [[0, 1, 0, 0],
                         [2, 0, 0, 0],
                         [0, 1, 0, 0],
                         [0, 0, 0, 0]]
move(map_environment, block_visit_frequency, [1, 1, 3])

'''
0 1 East 1
0 -1 West 3
1 0 South 2
-1 0 North 0

left 
N W -3
E N 1
S E 1
W S 1

right
N E -1
E S -1
S W -1
W N 3

U Turn 
N S -2
E W -2
S N  2
W E  2
'''