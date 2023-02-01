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
def file_head(fh, linecount):
    """
    -------------------------------------------------------
    Prints first linecount lines of fh. Line numbering starts at 0.
    If length of file is shorter than linecount, stops printing after
    last line of file.
    Use: file_head(fh, linecount)
    -------------------------------------------------------
    Parameters:
        fh - file to process (file handle - open for reading)
        linecount - number of lines to print (int > 0)
    Returns:
        None
    -------------------------------------------------------
    """
    current = 0
    line_content = fh.readline()
    while current < linecount and line_content != '':
        print(f'{line_content}', end='')
        line_content = fh.readline()
        current += 1
    return


def file_integers(fh):
    """
    -------------------------------------------------------
    Extracts positive integers from a file into a list of integers.
    Numbers are comma-delimited. Non-numeric tokens are ignored.
    Use: numbers = file_integers(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to process ( (file handle - open for reading)
    Returns:
        numbers - a list of integers from fh (list of int)
    -------------------------------------------------------
    """
    numbers = []
    for i in fh:
        split_values = i.strip().split(',')
        for a in split_values:
            if a.isnumeric():
                if int(a) > 0:
                    numbers.append(int(a))
    return numbers


def file_stats(fh):
    """
    -------------------------------------------------------
    Evaluates the contents of a file.
    Use: ucount, lcount, dcount, wcount = file_stats(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to process (file handle - open for reading)
    Returns:
        ucount - The number of uppercase letters in the file (int)
        lcount - The number of lowercase letters in the file (int)
        dcount - The number of digits in the file (int)
        wcount - The number of whitespace characters in the file (int)
    -------------------------------------------------------
    """
    ucount = 0 
    lcount = 0  
    dcount = 0
    wcount = 0
    for i in fh:
        for a in i:
            if a.isdigit():
                dcount += 1
            elif a.isupper():
                ucount += 1
            elif a.islower():
                lcount += 1
            else:
                wcount += 1
    return ucount, lcount, dcount, wcount


def flatten(matrix):
    """
    -------------------------------------------------------
    Flatten the contents of 2D list matrix. A 'flattened' list is a
    2D list that is converted into a 1D list by rows.
    matrix must be unchanged.
    Use: flat = matrix_flatten(matrix):
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list (2D list of int)
    Returns:
        flat - the flattened version of matrix (list of int)
    -------------------------------------------------------
    """
    flat = []
    for a in matrix:
        for b in a:
            flat.append(b)
    return flat


def matrix_rotate_right(matrix):
    """
    -------------------------------------------------------
    Returns a copy of a 2D matrix rotated to the right.
    a must be unchanged.
    Use: rotated = matrix_rotate_right(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of values (2d list of int/float)
    Returns:
        rotated - the rotated version of matrix (2D list of int/float)
    -------------------------------------------------------
    """
    rotated = []
    for a in range(len(matrix[0])):
        temp_list = []
        for b in range((len(matrix) - 1), -1, -1):
            temp_list.append(matrix[b][a])
        rotated.append(temp_list)
    return rotated


def get_addresses(fh):
    """
    -------------------------------------------------------
    Reads a addresses from fh into a list of addresses.
    Addresses are stored in fh in the form:
        name
        street
        city
        postal code
        --
    Each address in the list of addresses is a list of the form:
    [name, street, city, postal code]
    Use: addresses = get_addresses(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to process (file handle - open for reading)
    Returns:
        addresses - the addresses from fh (list of str)
    -------------------------------------------------------
    """
    addresses = []
    temp_list = []
    for a in fh:
        if a.strip() == '--':
            addresses.append(temp_list)
            temp_list = []
        else:
            temp_list.append(a.strip())
    return addresses