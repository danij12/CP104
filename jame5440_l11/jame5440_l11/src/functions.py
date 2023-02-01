"""
-------------------------------------------------------
Lab/Assignment  Testing
-------------------------------------------------------
Author:  Daniel James
ID:      210265440
Email:   jame5440@mylaurier.ca
Version: 2021-10-08
-------------------------------------------------------
"""
#1, 2, 6, 13, 15
from random import randint,uniform,choice

def generate_matrix_num(rows, cols, low, high, value_type):
    """
    -------------------------------------------------------
    Generates a 2D list of numbers of the given type, 'float' or 'int'.
    (To generate random float number use random.uniform and to
    generate random integer number use random.randint)
    Use: matrix = generate_matrix_num(rows, cols, low, high, value_type)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the list (int > 0)
        cols - number of columns (int > 0)
        low - low value of range (float)
        high - high value of range (float > low)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        matrix - a 2D list of random numbers (2D list of float/int)
    -------------------------------------------------------
    """
    matrix = []
    for i in range(rows):
        temp_list = []
        for i in range(cols):
            if value_type == 'float':
                # Import uniform like above
                temp_list.append(uniform(low, high))
            # This could've been an else statement
            # Import randint like above
            elif value_type == 'int':
                temp_list.append(randint(low, high))
        matrix.append(temp_list)
    return matrix


def generate_matrix_char(rows, cols):
    """
    -------------------------------------------------------
    Generates a 2D list of random lower case letter ('a' - 'z') values
    Use: matrix = generate_matrix_char(rows, cols)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the generated matrix (int > 0)
        cols - number of columns in the generated matrix (int > 0)
    Returns:
        matrix - a 2D list of random characters (2D list of str)
    -------------------------------------------------------
    """
    matrix = []
    for i in range(rows):
        temp_list = []
        for i in range(cols):
            temp_list.append(chr(randint(97, 122)))
        matrix.append(temp_list)
    return matrix


def stats(matrix):
    """
    -------------------------------------------------------
    Returns statistics on a 2D list.
        Use: smallest, largest, total, average = stats(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list of float/int)
    Returns:
        smallest - the smallest number in matrix (float/int)
        largest - the largest number in matrix (float/int)
        total - the total of the numbers in matrix (float/int)
        average - the average of numbers in matrix (float/int)
    -------------------------------------------------------
    """
    smallest = int(matrix[0][0])
    largest = int(matrix[0][0])
    total = 0 
    count = 0 
    for a in range(len(matrix)):
        for b in matrix[a]:
            if type(b) == int:
                int_num = int(b)
            else:
                int_num = float(b)
            if smallest>int_num:
                smallest = int_num
            if int_num>largest:
                largest = int_num
            total+=int_num
            count+=1
        
    
    return smallest,largest,total,total/count

def scalar_multiply(matrix, num):
    """
    -------------------------------------------------------
    Update matrix by multiplying each element of matrix by num.
    Use: scalar_multiply(matrix, num)
    -------------------------------------------------------
    Parameters:
        matrix - the matrix to multiply (2D list of int/float)
        num - the number to multiply by (int/float)
    Returns:
        None
    ------------------------------------------------------
    """
    
    for a in range(len(matrix)):
        for b in range(len(matrix[a])):
            matrix[a][b] *= num
            
          
    return matrix

def matrix_equal(matrix1, matrix2):
    """
    -------------------------------------------------------
    Compares two matrices to see if they are equal - i.e. have the
    same contents in the same locations.
    Use: equal = matrix_equal(matrix1, matrix2)
    -------------------------------------------------------
    Parameters:
        matrix1 - the first matrix (2D list of ?)
        matrix2 - the second matrix (2D list of ?)
    Returns:
        equal - True if matrix1 and matrix2 are equal,
            False otherwise (boolean)
    ------------------------------------------------------
    """
    equal = True
    i = 0
    if len(matrix1) == len(matrix2):
        while i < len(matrix1) and equal:
            if len(matrix1[i]) != len(matrix2[i]):
                equal = False
            else:
                equal = True
            i += 1
        i = 0 
        while i < len(matrix1) and equal:
            j = 0
            while j < len(matrix1[i]):
                if matrix1[i][j] != matrix2[i][j]:
                    equal = False
                j += 1
            i += 1
    else:
        equal = False
    return equal