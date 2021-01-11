'''
ECOR 1051: two and three tone filters
Mohamed Kaddour
101140829
Winter 2020
'''


from Cimpl import choose_file, load_image, copy, create_color, set_color,\
                  show, Image, get_color, create_image



def check_equal(description: str, outcome, expected) -> None:
    """
    Print a "passed" message if outcome and expected have same type and
    are equal (as determined by the == operator); otherwise, print a 
    "fail" message.
    
    Parameter description should provide information that will help us
    interpret the test results; e.g., the call expression that yields
    outcome.
    
    Parameters outcome and expected are typically the actual value returned
    by a call expression and the value we expect a correct implementation
    of the function to return, respectively. Both parameters must have the same
    type, which must be a type for which == is used to determine if two values
    are equal. Don't use this function to check if floats, lists of floats,
    tuples of floats, etc. are equal. 
    """
    outcome_type = type(outcome)
    expected_type = type(expected)
    if outcome_type != expected_type:
        
        # The format method is explained on pages 119-122 of 
        # 'Practical Programming', 3rd ed.
        
        print("{0} FAILED: expected ({1}) has type {2}, " \
              "but outcome ({3}) has type {4}".
              format(description, expected, str(expected_type).strip('<class> '), 
                      outcome, str(outcome_type).strip('<class> ')))
    elif outcome != expected:
        print("{0} FAILED: expected {1}, got {2}".
              format(description, expected, outcome))
    else:
        print("{0} PASSED".format(description))
    print("------")

'''
Function Name: two_tone
Author: Mohamed Kaddour
'''
def two_tone (image:Image,colour1:str,colour2:str) -> Image:
    '''Returns a filtered image consisting of the two colours passed in as 
    strings.
    
    >>> two_tone(filename, "red", "blue")
    -> Displays proper image
    >>> two_tone(filename, "green", "purple") 
    -> Displays incorrect image
    '''
    
    
    col1 = [0,0,0]
    col2 = [0,0,0]
    
    if colour1 == "black":
        col1 = [0,0,0]
    elif colour1 == "white":
        col1 = [255,255,255]
    elif colour1 == "red":
        col1 = [255,0,0]
    elif colour1 == "lime":
        col1 = [0,255,0]
    elif colour1 == "blue":
        col1 = [0,0,255]
    elif colour1 == "yellow":
        col1 = [255,255,0]
    elif colour1 == "cyan":
        col1 = [0,255,255]
    elif colour1 == "magenta":
        col1 = [255,0,255]
    elif colour1 =="gray":
        col1 = [128,128,128]
        
    if colour2 == "black":
        col2 = [0,0,0]
    elif colour2 == "white":
        col2 = [255,255,255]
    elif colour2 == "red":
        col2 = [255,0,0] 
    elif colour2 == "lime":
        col2 = [0,255,0]
    elif colour2 == "blue":
        col2 = [0,0,255]
    elif colour2 == "yellow":
        col2 = [255,255,0]
    elif colour2 == "cyan":
        col2 = [0,255,255]
    elif colour2 == "magenta":
        col2 = [255,0,255]
    elif colour2 =="gray":
        col2 = [128,128,128]
    
    
    new_image = copy(image)
    new_colour = create_color(0,0,0)
    
    for pixel in image:
        x, y, (r, g, b) = pixel 
        avg = (r + b + g)/3
        if 0 <= avg <= 127:
            new_colour = create_color(col1[0],col1[1],col1[2])
            set_color(new_image, x, y, new_colour)
        elif 128 <= avg <= 255:
            new_colour = create_color(col2[0],col2[1],col2[2])
            set_color(new_image, x, y, new_colour)
        
    return new_image


'''Function Name: three_tone
Author: Mohamed Kaddour'''
def three_tone (image:Image,colour1:str,colour2:str,colour3:str) -> Image:
    '''Returns a filtered image consisting of the three colours passed in as 
    strings.
    
    >>> two_tone(filename, "red", "blue", "black")
    -> Displays proper image
    >>> two_tone(filename, "green", "purple", "orange") 
    -> Displays incorrect image
    '''
    
    
    col1 = [0,0,0]
    col2 = [0,0,0]
    col3 = [0,0,0]
    
    if colour1 == "black":
        col1 = [0,0,0]
    elif colour1 == "white":
        col1 = [255,255,255]
    elif colour1 == "red":
        col1 = [255,0,0]
    elif colour1 == "lime":
        col1 = [0,255,0]
    elif colour1 == "blue":
        col1 = [0,0,255]
    elif colour1 == "yellow":
        col1 = [255,255,0]
    elif colour1 == "cyan":
        col1 = [0,255,255]
    elif colour1 == "magenta":
        col1 = [255,0,255]
    elif colour1 =="gray":
        col1 = [128,128,128]
        
    if colour2 == "black":
        col2 = [0,0,0]
    elif colour2 == "white":
        col2 = [255,255,255]
    elif colour2 == "red":
        col2 = [255,0,0] 
    elif colour2 == "lime":
        col2 = [0,255,0]
    elif colour2 == "blue":
        col2 = [0,0,255]
    elif colour2 == "yellow":
        col2 = [255,255,0]
    elif colour2 == "cyan":
        col2 = [0,255,255]
    elif colour2 == "magenta":
        col2 = [255,0,255]
    elif colour2 =="gray":
        col2 = [128,128,128]    
        
    if colour3 == "black":
        col3 = [0,0,0]
    elif colour3 == "white":
        col3 = [255,255,255]
    elif colour3 == "red":
        col3 = [255,0,0] 
    elif colour3 == "lime":
        col3 = [0,255,0]
    elif colour3 == "blue":
        col3 = [0,0,255]
    elif colour3 == "yellow":
        col3 = [255,255,0]
    elif colour3 == "cyan":
        col3 = [0,255,255]
    elif colour3 == "magenta":
        col3 = [255,0,255]
    elif colour3 =="gray":
        col3 = [128,128,128]    
    
    new_image = copy(image)
    new_colour = create_color(0,0,0)
    
    for pixel in image:
        x, y, (r, g, b) = pixel 
        avg = (r + b + g)/3
        if 0 <= avg <= 84:
            new_colour = create_color(col1[0],col1[1],col1[2])
            set_color(new_image, x, y, new_colour)
        elif 85 <= avg <= 170:
            new_colour = create_color(col2[0],col2[1],col2[2])
            set_color(new_image, x, y, new_colour)
        elif 170 <= avg <= 255:
            new_colour = create_color(col3[0],col3[1],col3[2])
            set_color(new_image, x, y, new_colour)            
        
    return new_image
    
    
def test_two_tone():
    ''' tests the two-tone filter, assuming the two strings passed in are 
    black and white respectivley 
    >>>test_two_tone()
    Checking pixel @(0, 0) PASSED
    ------
    Checking pixel @(1, 0) PASSED
    ------
    '''
    #Creates the test image
    original = create_image(6, 1)
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(0, 0, 1))
    set_color(original, 2, 0,  create_color(127, 127, 127))
    set_color(original, 3, 0,  create_color(125, 73, 224))
    set_color(original, 4, 0,  create_color(254, 255, 255))
    set_color(original, 5, 0,  create_color(255, 255, 255))    
    
    #Proper Image after two_tone is applied
    actual = create_image(6, 1)
    set_color(actual, 0, 0,  create_color(0, 0, 0))
    set_color(actual, 1, 0,  create_color(0, 0, 0))
    set_color(actual, 2, 0,  create_color(0, 0, 0))
    set_color(actual, 3, 0,  create_color(255, 255, 255))
    set_color(actual, 4, 0,  create_color(255, 255, 255))
    set_color(actual, 5, 0,  create_color(255, 255, 255))    
    
    twot_image = two_tone(original, 'black', 'white')   
    for x, y, col in twot_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(actual, x, y))
        
def test_three_tone():
    ''' tests the three-tone filter, assuming the two strings passed in are 
    black and white and gray respectivley 
    >>>test_three_tone()
    
    '''
    #Creates the test image
    original = create_image(6, 1)
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(85, 88, 95))
    set_color(original, 2, 0,  create_color(127, 127, 127))
    set_color(original, 3, 0,  create_color(189, 172, 224))
    set_color(original, 4, 0,  create_color(254, 255, 255))
    set_color(original, 5, 0,  create_color(87, 28, 25))    
    
    #Proper Image after three_tone is applied
    actual = create_image(6, 1)
    set_color(actual, 0, 0,  create_color(0, 0, 0))
    set_color(actual, 1, 0,  create_color(255, 255, 255))
    set_color(actual, 2, 0,  create_color(255, 255, 255))
    set_color(actual, 3, 0,  create_color(128, 128, 128))
    set_color(actual, 4, 0,  create_color(128, 128, 128))
    set_color(actual, 5, 0,  create_color(0, 0, 0))    
    
    threet_image = three_tone(original, 'black', 'white', 'gray')   
    for x, y, col in threet_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(actual, x, y))
        

filename = "p2-original.jpg"
filename = copy(load_image(filename))
twop_img = two_tone(filename, "black", "white")
show(twop_img)
threep_img = three_tone(filename, "magenta", "white", "cyan")
show(threep_img)
test_two_tone()
print("-------------------------------------------------------")
test_three_tone()