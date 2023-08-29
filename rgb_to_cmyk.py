# Coding Night - Submission Kyle de Vos
# Challenge - Convert rgb to cmyk
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
    
def rgbToCmyk(number1, number2, number3):

    # check for valid rgb inputs
    number1 = verify_number(number1)
    if number1 == "invalid":
        return ["invalid"]
    
    number2 = verify_number(number2)
    if number2 == "invalid":
        return ["invalid"]
    
    number3 = verify_number(number3)
    if number3 == "invalid":
        return ["invalid"]
    
    # all numbers are valid, convert to equivalent range
    red = number1/255
    green = number2/255
    blue = number3/255
    
    # Convert rgb to Cmyk
    # Formula from: wizlogo, Referenced on 29 August 2023
    # Available from: https://wizlogo.com/rgb-to-cmyk

    # calculate black key colour:
    k = 1 - max(red, green, blue)
    # calculate cyan
    c = (1- red - k) / (1 - k)
    # calculate magenta
    m = (1 - green - k) / (1 - k)
    # calculate yellow
    y = (1 - blue - k) / (1 - k)

    return [int(round(c*100, 0)), int(round(m*100, 0)), int(round(y*100, 0)), int(round(k*100, 0))]

# Testing
# print(rgbToCmyk(255, 255, 255))
# print(rgbToCmyk(100, 50, 75))
    
    