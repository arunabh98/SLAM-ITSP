from math import *

# Each block will be a square of side 20cm
map_environment = [[0 for i in range(10)] for j in range(10)]
block_visit_frequency = [[0 for i in range(10)] for j in range(10)]
'''
The first two values in bot coordinates stand for x and y values.
The third value denotes the direction in which the bot is facing.
0 stands for North, 1 for East, 2 for South, 3 for West
'''
bot_coordinates = [0, 0, 0]
obstacle_threshold = 0.5
map_width = 4
block_width = 20.0
bot_absolute_location = [0, 0] # Exact X and Y coordinate kept track by stepper motor


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
        if (bot_coordinates[0] + i) < map_width and (bot_coordinates[1] + int(not i)) < map_width:
            if map_environment[bot_coordinates[0] + i][bot_coordinates[1] + int(not i)] < obstacle_threshold:
                if i == 0:
                    if bot_coordinates[1] + int(not i) < 10:
                        possible_direction.append(1)
                else:
                    if bot_coordinates[0] + i < 10:
                        possible_direction.append(2)
        if map_environment[bot_coordinates[0] - i][bot_coordinates[1] - int(not i)] < obstacle_threshold:
            if i == 0:
                if bot_coordinates[1] - int(not i) >= 0:
                    possible_direction.append(3)
            else:
                if bot_coordinates[0] - i >= 0:
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

'''
Variable to hold the distances by the Ultrasonic sensors. First
Value in the array will be the front facing sensor,
second - right sensor, third - bottom sensor, fourth - left sensor
'''
sensor_readings = [0, 0, 0, 0]
absolute_direction_sensors = [0, 1, 2, 3]
absolute_distance = [0, 0, 0, 0]


def landmark_update(map_environment, bot_coordinates, sensor_readings, bot_absolute_location):
    absolute_direction_sensors[0] = bot_coordinates[2]
    absolute_direction_sensors[1] = (bot_coordinates[2] + 1) % 4
    absolute_direction_sensors[3] = (bot_coordinates[2] - 1) % 4
    if bot_coordinates[2] < 2:
        absolute_direction_sensors[2] = bot_coordinates[2] + 2
    else:
        absolute_direction_sensors[2] = bot_coordinates[2] - 2
    print absolute_direction_sensors
    for counter in range(4):
        absolute_distance[absolute_direction_sensors[counter]] = sensor_readings[counter]
    print absolute_distance
    counter = 0
    for distance in absolute_distance:
        obstacle_location = get_obstacle_location(bot_absolute_location, counter, distance)
        print obstacle_location
        map_environment[int(obstacle_location[0])][int(obstacle_location[1])] += 0.5
        counter += 1
    for x in map_environment:
        print x

def get_obstacle_location(bot_absolute_location, direction, distance):

    if direction == 0:
        obstacle_x = bot_absolute_location[0] - distance
        obstacle_y = bot_absolute_location[1]
    if direction == 1:
        obstacle_x = bot_absolute_location[0]
        obstacle_y = bot_absolute_location[1] + distance
    if direction == 2:
        obstacle_x = bot_absolute_location[0] + distance
        obstacle_y = bot_absolute_location[1]
    if direction == 3:
        obstacle_x = bot_absolute_location[0]
        obstacle_y = bot_absolute_location[1] - distance
    obstacle_block_x = floor(obstacle_x/block_width)
    obstacle_block_y = floor(obstacle_y/block_width)
    return [obstacle_block_x, obstacle_block_y]



# TEST
map_environment = [[0, 0, 0, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0]]
block_visit_frequency = [[0, 0, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 1, 0]]
sensor_readings = [15, 30, 30, 20]
# move(map_environment, block_visit_frequency, [3, 3, 0])
landmark_update(map_environment, [1, 1, 0], sensor_readings, [30, 30])

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