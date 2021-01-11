from Cimpl import choose_file, load_image, copy, create_color, set_color,\
                  show, Image, get_color, create_image, get_width, get_height


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
        

def detect_edges_better(image:Image,threshold:float) -> Image:
    '''
    Author: Mohamed Kaddour
    Student ID: 101140829
    '''
    ''' Takes in an original image as well as a thershold as a float and 
    returns and an image with the improved edge detection filter applied
    based on the value of the threshold. This filter compares the brightness
    of a pixel's neighbouring pixels and then prints on a filter similar to
    that of a pencil drawing.
    >>>show(detect_edges_better(filename,15))
    [Displays proper image]
    
    '''
     
    new_image = copy(image)
    
    width = get_width(new_image)
    height = get_height(new_image)     
    
    for x in range(width-1):
        for y in range(height-1):
              
            r1,g1,b1 = get_color(new_image,x,y)
            r2,g2,b2 = get_color(new_image,x+1,y)
            r3,g3,b3 = get_color(new_image,x,y+1)
            
            brightness1 = (r1+g1+b1)/3
            brightnessv = (r2+g2+b2)/3
            brightnessr = (r3+g3+b3)/3
  
            
            if abs(brightness1-brightnessv) >= threshold or abs(brightness1-brightnessr) >= threshold:
                black = create_color(0,0,0)
                set_color(new_image, x, y, black)      
            else: 
                white = create_color(255,255,255)
                set_color(new_image, x, y, white)
                  
               
    return new_image   

filename = "p2-original.jpg"
filename = copy(load_image(filename))
show(detect_edges_better(filename,15))
test_detect_edges_better()