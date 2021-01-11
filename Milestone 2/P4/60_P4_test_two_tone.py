
from Cimpl import choose_file, load_image, copy, create_color, set_color,\
                  show, Image, get_color, create_image

from T60_P4_two_tone import two_tone


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
    

def test_two_tone():
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
test_two_tone()