import random


def get_non_repeating_random_2d_list(rows, cols):
    n = rows * cols
    temp = []
    while len(temp) < n:
        x = random.randint(1, 16)
        if x not in temp:
            temp.append(x)
    
    result = [[None for i in range(cols)] for j in range(rows)]

    index = 0
    for i in range(rows):
        for j in range(cols):
            result[i][j] = temp[index]
            index += 1

    return result