from Cimpl import choose_file, load_image, copy, create_color, set_color,\
                  show, Image, get_color, create_image

from T60_P4_improved_edge_detection import detect_edges_better


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
    
    

def test_detect_edges_better():
    '''Tests the pixels in a made up image to see if the function works
    properly but comparing the original image when passed through the function
    with the expected colour. Prints out the pixel and whether the test passed
    or failed.
    >>>test_detect_edges_better
    Checking pixel @(0, 0) PASSED
    ------
    Checking pixel @(1, 0) PASSED
    ------
    Checking pixel @(2, 0) PASSED
    ------
    Checking pixel @(0, 1) PASSED
    ------
    Checking pixel @(1, 1) PASSED
    ...
    ...
    '''
    
    original = create_image(3, 3)
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(22, 35, 21))
    set_color(original, 0, 1,  create_color(12, 33, 41))
    set_color(original, 2, 0,  create_color(55, 83, 26))
    set_color(original, 1, 1,  create_color(12, 33, 41))
    set_color(original, 1, 2,  create_color(85, 98, 72))
 
    
    expected = create_image(3, 3)
    set_color(expected, 0, 0,  create_color(255, 255, 255))
    set_color(expected, 1, 0,  create_color(255, 255, 255))
    set_color(expected, 0, 1,  create_color(0, 0, 0)) 
    set_color(expected, 2, 0,  create_color(55, 83, 26)) 
    set_color(expected, 1, 1,  create_color(0, 0, 0)) 
    set_color(expected, 1, 2,  create_color(85, 98, 72)) 
    '''NOTE: Can't expect pixels (2,0) and (1,2) because there are no pixels
    defined that are below or to the right of them (No 3 pixel defined in x or
    or y). '''
    
    
    threshold = 30 #Assumed threshold 
    test_edge = detect_edges_better(original,threshold)   
    for x, y, col in test_edge:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                   col, get_color(expected, x, y))     

test_detect_edges_better()