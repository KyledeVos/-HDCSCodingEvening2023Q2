# Coding Night - Submission Kyle de Vos
# -------------------------------------------------------------

def verify_number(number):
    """Check if a number is a valid Integer between 0-255. Convert negative numbers to 0
    and numbers > 255 to 255. Non-Numeric numbers are not handled with return -1
    
    Parameters:
    -----------
    number: int 
        number to be verified

    Return:
    -------
    original number if valid, 0 for negative numbers, 255 for numbers larger than 255 or '-1'
    for non-numeric inputs
    """
    try:
        # check for non-numeric input
        valid_int = int(number)

        if number > 255:
            # return max allowed number
            return 255
        elif number < 0:
            # return min allowed number
            return 0
        else:
            # number is valid
            return number

    # return '-1' to indicate non-numeric input
    except ValueError:
            return '-1'


def return_hex(number):
    """Convert a Received Number (verified to be between 0 and 15) to the hexadecimal equivalent
    
    Parameter:
    ----------
    number: int
        number to be converted to hexadecimal equivalent
    """
    # for numbers greater than 10, convert to equivalent letters
    if number > 9:
        if number == 10:
            return 'A'
        elif number == 11:
            return 'B'
        elif number == 12:
            return 'C'
        elif number == 13:
            return 'D'
        elif number == 14:
            return 'E'
        elif number == 15:
            return 'F'
        # numbers less than 10, return number as string
    else:
        return str(number)
    

def convert_decimal_to_hex(number):
    """Convert a validated decimal number (0-15) to its hexadecimal equivalent.
    
    Parameter:
    ----------
    number: int
        number to be converted to hexadecimal
    """
    # check if number is valid
    verified_number = verify_number(number)
    
    # check if number had a non-nunmeric input
    if verified_number == '-1':
        # non-numeric was recieved, terminate check
        print("An input was recieved that was non-numeric. Conversion cannot be completed")
        return
    
    # number is a valid int, perform conversion to hexadecimal equivalent
    return return_hex(verified_number)



    

    
