__author__ = "Chris"

import random
import copy
import time


def get_matrix_dimension():
    """dimension of matrix

    Returns:
        n: dimension of matrix
    """
    n = int(input("Size of n x n matrix?\n> "))
    return n

def create_matrix(n):
    """Function to create a matrix

    Args:
        n: dimension of matrix

    Returns:
        matrix: final matrix
    """
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(n):
            matrix[i].append(random.randint(0, 9))
    print(matrix, "\n")
    
    string = "["    
    for k in range(n - 1):
        string += str(matrix[k]) + "\n "
    string += str(matrix[n - 1]) + "]"
    print(string)
    return matrix


def optimal_way(matrix, x, y):
    """Function to find the optimal way
    
    Args:
        matrix: final matrix
        x: row
        y: column
    
    Returns:
        costs: costs of the optimal way
        path: path of the optimal way
    """
    
    
    n = len(matrix)
    path_r = path_l = path_u = path_d = []
    costs = matrix[x][y]
    new_matrix = copy.deepcopy(matrix)
    new_matrix[x][y] = - 1
    right = left = up = down = 10 * n ** 2
    
    if x == n - 1 and y == n - 1:
        return costs, [(x, y)]
    if x < n - 1 and matrix[x+1][y] != - 1:
        down, path_d = optimal_way(new_matrix, x + 1, y)
    if y < n - 1 and matrix[x][y+1] != - 1:
        right, path_r = optimal_way(new_matrix, x, y + 1)
    if x > 0 and matrix[x-1][y] != - 1:
        up, path_u = optimal_way(new_matrix, x - 1, y)
    if y > 0 and matrix[x][y-1] != - 1:
        left, path_l = optimal_way(new_matrix, x, y - 1)
    
    if right <= down and right <= up and right <= left:
        return right + costs, [(x, y)] + path_r
    elif left <= down and left <= up and left <= right:
        return left + costs, [(x, y)] + path_l
    elif up <= down and up <= right and up <= left:
        return up + costs, [(x, y)] + path_u
    else:
        return down + costs, [(x, y)] + path_d

start_time = time.time()
dim = get_matrix_dimension()
print(optimal_way(create_matrix(dim), 0, 0))
end_time = time.time()
delta = end_time - start_time
print(delta)

if __name__ == "__main__":
    try:
        get_matrix_dimension(x)
    except:
        print("ValueError: invalid literal for int() with base 10: 'x'")
    try:
        create_matrix(n)
    except:
        print("NameError: name 'n' is not defined")
    try:
        optimal_way(matrix, x, y)
    except:
        print("NameError: name 'matrix' is not defined")
