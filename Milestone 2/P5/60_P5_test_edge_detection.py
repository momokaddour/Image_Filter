'''
ECOR 1051: Edge Detection Filter Test
Team Identifer: 60
Mohamed Kaddour
101140829
Winter 2020
'''


from Cimpl import choose_file, load_image, copy, create_color, set_color,\
                  show, Image, get_color, create_image, get_width, get_height

from T60_P5_detect_edges import detect_edges

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
    
    
def test_detect_edges():
    '''
    Author: Mohamed Kaddour
    Student ID: 101140829
    
    '''
    '''Tests the pixels in a made up image to see if the function works
    properly by comparing the original image when passed through the function
    with the expected colour. Prints out the pixel and whether the test passed
    or failed.
    >>>test_detect_edges_better
    Checking pixel @(0, 0) PASSED
    ------
    Checking pixel @(1, 0) PASSED
    ------
    Checking pixel @(0, 1) PASSED
    ------
    Checking pixel @(0, 2) PASSED
    ------
    Checking pixel @(1, 2) PASSED
    ...
    ...
    '''
    
    original = create_image(2, 6)
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 0, 1,  create_color(55, 35, 29))
    set_color(original, 0, 2,  create_color(22, 12, 43))
    set_color(original, 0, 3,  create_color(55, 83, 26))
    set_color(original, 0, 4,  create_color(123, 85, 200))
    set_color(original, 0, 5,  create_color(122, 82 ,211))
 
    
    expected = create_image(2, 6)
    set_color(expected, 0, 0,  create_color(0, 0, 0))
    set_color(expected, 0, 1,  create_color(255, 255, 255))
    set_color(expected, 0, 2,  create_color(255, 255, 255)) 
    set_color(expected, 0, 3,  create_color(0, 0, 0)) 
    set_color(expected, 0, 4,  create_color(255, 255, 255)) 
    set_color(expected, 0, 5,  create_color(122, 82, 211)) 
    
    
    threshold = 30 #Assumed threshold 
    test_edge = detect_edges(original,threshold)   
    for x, y, col in test_edge:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                   col, get_color(expected, x, y))   
        
        
test_detect_edges()