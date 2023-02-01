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
#    2, 4, 7, 10, 12
def url_categorize(url):
    """
    -------------------------------------------------------
    Returns whether a url represents a business, a non-profit, or another
    type of organization.
    Use: url_type = url_categorize(url)
    -------------------------------------------------------
    Parameters:
        url - the web address of the organization (str)
    Returns:
        url_type - the organization type (str)
            'business' if url ends with 'com'
            'non-profit' if url ends with 'org'
            'other' if url ends with something else
    ------------------------------------------------------
    """
 
    if 'com' in url and len(url)-3 == url.index('com'):
        type = 'business'
    elif 'org' in url and len(url)-3 == url.index('org'):
        type = 'non-profit'
    else:
        type = 'other'
    return type

def validate_code(product_code):
    """
    -------------------------------------------------------
    Parses a given product code and prints whether the various parts are valid.
    A product code has three parts:
        The first three letters describe the product category and must
        all be in upper case.
        The next four digits are the product ID.
        The remaining characters describe the product's qualifiers,
        such as colour, size, etc. and always begins with an uppercase letter.
    Use: validate_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a product code (str)
    Returns:
        None
    -------------------------------------------------------
    """
    product_category  =  product_code[0:3]
    product_digit = product_code[3:7]
    product_qualifiers = product_code[7:]
    print()
    if product_category.isupper() and len(product_category)==3:
         print(f'Category {product_category} is valid.')
    else: 
        print(f'CategOry {product_category} is not valid.')
    if product_digit.isdigit() and len(product_digit)==4:
        print(f'ID {product_digit} is valid.')
    else:
        print(f'ID {product_digit} is not valid.')
     
    if product_qualifiers and product_qualifiers[0].isupper():
        print(f'QualifIer {product_qualifiers} is valid.')
    else:
        print(f'QualifIer {product_qualifiers} is not valid.')
        
    return 

def vowel_count(s):
    """
    -------------------------------------------------------
    Counts the number of vowels in a string. Does not include 'y'.
    Use: count = vowel_count(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        count - the number of vowels in s (int)
    -------------------------------------------------------
    """
    count = 0 
    for a in s:
        if a in 'aeiouAEIOU':
            count+=1
    return count
        
def text_analyze(txt):
    """
    -------------------------------------------------------
    Analyzes txt and returns the number of uppercase letters,
    lowercase letters, digits, and number of whitespaces in txt.
    Use: uppr, lowr, dgts, whtspc = text_analyze(txt)
    -------------------------------------------------------
    Parameters:
        txt - the text to be analyzed (str)
    Returns:
        uppr - number of uppercase letters in txt (int >= 0)
        lowr - number of lowercase letters in txt (int >= 0)
        dgts - number of digits in txt (int >= 0)
        whtspc - number of white spaces in the text (spaces, tabs, linefeeds) (int >= 0)
    ------------------------------------------------------
    """
    uppr = 0 
    lowr = 0
    dgts = 0
    whtspc = 0
    for a in txt:
        if a.isupper() == True:
            uppr += 1
        elif a.islower() == True:
            lowr += 1
        elif a == ' ':
            whtspc += 1
        elif a.isdigit() == True:
            dgts += 1
            
    return uppr,lowr,dgts,whtspc  


def comma_period_replace(s):
    """
    -------------------------------------------------------
    Replaces all the commas with a period in s.
    Use: out = comma_period_replace(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        out - s with all commas replaced by a period (str)
    ------------------------------------------------------
    """
    new_string = s.replace(',','.')
    
    return new_string
            
      
   