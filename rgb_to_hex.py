# Coding Night - Submission Kyle de Vos
# Challenge - Convert rgb to Hexadecimal
# -------------------------------------------------------------

# Helper Function
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

# Helper Function


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

# Helper Function
def convert_decimal_to_hex(number):
    """Convert a validated decimal number (0-15) to its hexadecimal equivalent.

    Parameter:
    ----------
    number: int
        number to be converted to hexadecimal

    Return:
    -------
    Hexademical number (string) or message for 'invalid'
    """
    # check if number is valid
    verified_number = verify_number(number)

    # check if number had a non-numeric input
    if verified_number == '-1':
        # non-numeric was recieved, terminate check
        return "invalid"

    # list to hold hexadecimal place value

    # if
    hex_list = []

    # begin conversion of number to hexadecimal
    while verified_number >= 16:
        # retrieve remainder for hexadecimal conversion
        remainder = verified_number % 16
        # convert to hexadecimal and append to list
        hex_list.insert(0, return_hex(remainder))
        # remove converted component
        verified_number = int(verified_number/16)

    # final check for remaining conversion to hex
    if verified_number > 0:
        hex_list.insert(0, return_hex(verified_number))
    elif verified_number == 0:
        hex_list.insert(0, '00')
    else:
        hex_list.insert(0, '0')

    return hex_list


# Main Function
def rgbToHex(number1, number2, number3):
    """Controlling Function to convert three decimal numbers to hexadecimal functions

    Parameters:
    -----------
    number1:
        first integer for conversion to hex
    number2:
        second integer for conversion to hex
    number3:
        third integer for conversion to hex
    """
    # perform conversions from decimal to hex
    convert1 = convert_decimal_to_hex(number1)
    convert2 = convert_decimal_to_hex(number2)
    convert3 = convert_decimal_to_hex(number3)

    # perform check if any input was invalid
    if 'invalid' in convert1 or 'invalid' in convert2 or 'invalid' in convert3:
        return "invalid"

    else:
        # return completed hexadecimal number
        combined_list = convert1 + convert2 + convert3
        return "".join(combined_list)
