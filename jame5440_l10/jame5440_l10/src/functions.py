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
#1, 2, 6, 9, 12
def customer_record(fh, n):
    """
    -------------------------------------------------------
    Find the n-th record in a comma-delimited sequential file.
    Records are numbered starting with 0.
    Use: result = customer_record(fh, n)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        n - the number of the record to return (int > 0)
    Returns:
        result - a list of the fields of the n-th record if it exists,
            an empty list otherwise (list)
    -------------------------------------------------------
    """
    person = fh.readline()
    count = 0
    final_list = []
    count2 = 0 
    while count != n:
        person = fh.readline()
        count +=1
    final_list = person.strip().split(',')
    if final_list == ['']:
        final_list = []
    return final_list

def customer_by_id(fh, id_number):
    """
    -------------------------------------------------------
    Find the record for a given ID in a sequential file.
    Use: result = customer_by_id(fh, id_number)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        id_number - the id_number to match (str)
    Returns:
        result - the record with id_number if it exists,
            an empty list otherwise (list)
    -------------------------------------------------------
    """
    person = fh.readline()
    final_list = []
    count = 0 
    
    while person != '' and count!=1:
        if id_number in person:
            final_list = person.strip().split(',')
            count = 1
        else:
            person = fh.readline()
    return final_list


def number_stats(fh):
    """
    -------------------------------------------------------
    Returns statistics on the numbers in a file.
    Assumes file is not empty.
    Use: smallest, largest, total, average = number_stats(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        smallest - smallest number (int)
        largest - largest number (int)
        total - sum of all the numbers in the file (int)
        average - average of all the numbers (float)
    ------------------------------------------------------
    """
    smallest = None
    largest = None
    average = 0 
    count = 0 
    total = 0 
    for a in fh:
        number = int(a.strip())
        if count == 0:
            smallest = number
            largest = number
        if number>largest:
            largest = number
        if number<smallest:
            smallest = number
        count +=1
        total += number
    return smallest,largest,total,total/count
   
def count_frequency_value(fh, value):
    """
    -------------------------------------------------------
    Counts the number of appearances of value in fh.
    Use: count = count_frequency_value(fh, value)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        value - the value to count (int)
    Returns:
        count - the number of appearance of value in fh (int)
    ------------------------------------------------------
    """
    count = 0
    line = (fh.readline())
    while line != '':
        line = line.strip()
        if int(line) == value:
            count+=1
        line = fh.readline()
    return count

def find_shortest(fh):
    """
    -------------------------------------------------------
    Finds the first word with shortest length in fh.
    Assumes file is not empty.
    Use: word = find_shortest(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        word - the first word with the shortest length in fh (str)
    ------------------------------------------------------
    """
    word = fh.readline()
    shortest = word.strip()
    
    while word != '':
        word = word.strip()
        if len(word)<len(shortest):
            shortest = word        
        word = fh.readline()
            
    return shortest