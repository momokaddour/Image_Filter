from Cimpl import choose_file, load_image, copy, create_color, set_color,\
                  show, Image, get_color, create_image


def extreme_contrast(image:Image) -> Image:
    
    new_image = copy(image)
    for pixel in image:
        x, y, (r, g, b) = pixel 
        if 0<=r<=127:
            r = 0
        elif 128<=r<=255:
            r = 255
        if 0<=g<=127:
            g = 0
        elif 128<=g<=255:
            g = 255        
        if 0<=b<=127:
            b = 0
        elif 128<=b<=255:
            b = 255   
        new_colour = create_color(r,g,b)
        set_color(new_image, x, y, new_colour)
    return new_image
        


'''Obtained from the [test_grayscale.py] file off of cuLearn'''
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

def test_extreme_contrast():
    ''' tests the two-tone filter, assuming the two strings passed in are 
    black and white respectivley.
    >>>test_two_tone()
    Checking pixel @(0, 0) PASSED
    ------
    Checking pixel @(1, 0) PASSED
    ------
    '''
    #Creates the test image
    original = create_image(6, 1)
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(0, 128, 128))
    set_color(original, 2, 0,  create_color(127, 127, 127))
    set_color(original, 3, 0,  create_color(125, 73, 224))
    set_color(original, 4, 0,  create_color(254, 255, 255))
    set_color(original, 5, 0,  create_color(126, 127, 128))    
    
    #Proper Image after extreme contrast is applied
    actual = create_image(6, 1)
    set_color(actual, 0, 0,  create_color(0, 0, 0))
    set_color(actual, 1, 0,  create_color(0, 255, 255))
    set_color(actual, 2, 0,  create_color(0, 0, 0))
    set_color(actual, 3, 0,  create_color(0, 0, 255))
    set_color(actual, 4, 0,  create_color(255, 255, 255))
    set_color(actual, 5, 0,  create_color(0, 0, 255))    
    
    twot_image = extreme_contrast(original)   
    for x, y, col in twot_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(actual, x, y))

filename = "p2-original.jpg"
filename = copy(load_image(filename))
threep_img = extreme_contrast(filename)
show(threep_img)
test_extreme_contrast()