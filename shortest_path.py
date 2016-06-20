def optimum_policy(grid,goal,cost):
    delta = [[-1, 0 ], # go up
             [ 0, -1], # go left
             [ 1, 0 ], # go down
             [ 0, 1 ]] # go right


    delta_name = [0, 3, 2, 1]
    value = [[99 for row in range(len(grid[0]))] for col in range(len(grid))]
    value1 = [[[99 for k in xrange(4)] for j in xrange(len(grid[0]))] for i in xrange(len(grid))]
    policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    change = True
    while change:
        change = False

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if goal[0] == x and goal[1] == y:
                    if value[x][y] > 0:
                        value[x][y] = 0

                        change = True

                elif grid[x][y] == 0:
                    for a in range(len(delta)):
                        x2 = x + delta[a][0]
                        y2 = y + delta[a][1]

                        if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
                            v2 = value[x2][y2] + cost
                            if v2 < value[x][y]:
                                change = True
                                value[x][y] = v2
                                policy[x][y] = delta_name[a]
    policy[goal[0]][goal[1]] = 9
    return policy