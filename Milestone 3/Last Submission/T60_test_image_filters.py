'''
ECOR 1051
Winter 2020
Team Identifier: 60
Test Filters

Team Members:
Mohamed Kaddour (TL)
Adam Burger
Kiyara Desilva 
Taekwan Oh
'''
from Cimpl import choose_file, load_image, copy, create_color, set_color,\
                  show, Image, get_color, create_image, get_width, get_height

import T60_image_filters


#FROM PROVIDED 1051 SAMPLE FILTERS


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
    
    
#MILESTONE 1 TEST FUNCTIONS:

def test_red_channel () -> None:
    
    '''Function Name: Test Red Channel
    Author: Adam Burger 101141832
    '''    
    '''Takes in an image and checks each pixel to ensure it is red. Prints
    out pixels being tested, RGB values and "pass" or "fail"
    >>>test_red_channel(red_image)
    Testing Pixels: 541 445 RGB: 104 0 0
    Passed
    .......
    ...
    '''
    
    original = create_image(6, 1)
    set_color(original, 0, 0,  create_color(12, 44, 122))
    set_color(original, 1, 0,  create_color(0, 128, 128))
    set_color(original, 2, 0,  create_color(127, 127, 127))
    set_color(original, 3, 0,  create_color(125, 73, 224))
    set_color(original, 4, 0,  create_color(254, 255, 255))
    set_color(original, 5, 0,  create_color(126, 127, 128))   
    
    image = red_channel(original)
    print("Testing Red Image...")
    for pixel in image:
        x, y, (r, g, b) = pixel
        print ("Testing Pixels:",x,y,"RGB:", r,g,b)
        if (g==0 and b==0):
            print("Passed")
        else:
            print("Failed")
            

def test_green_channel () -> None:
    '''Function Name: Test Green Channel
    Author: Kiyara Desilva 101165279
    '''    
    '''Takes in an image and checks each pixel to ensure it is green. Prints
    out pixels being tested, RGB values and "pass" or "fail"
    >>test_green_channel(green_image)
    Testing Pixels: 310 402 RGB: 0 6 0
    Passed
    ........
    ...
    '''
    
    original = create_image(6, 1)
    set_color(original, 0, 0,  create_color(12, 44, 122))
    set_color(original, 1, 0,  create_color(0, 128, 128))
    set_color(original, 2, 0,  create_color(127, 127, 127))
    set_color(original, 3, 0,  create_color(125, 73, 224))
    set_color(original, 4, 0,  create_color(254, 255, 255))
    set_color(original, 5, 0,  create_color(126, 127, 128))   
    
    image = green_channel(original)    
    print("Testing Green Image...")
    for pixel in image:
        x, y, (r, g, b) = pixel
        print ("Testing Pixels:",x,y,"RGB:", r,g,b)
        if (r==0 and b==0):
            print("Passed")
        else:
            print("Failed")


def test_blue_channel () -> None:
    
    '''Function Name: Blue Channel Test
    Author: Taekwan Oh 101148069
    '''    
    '''Takes in an image and checks each pixel to ensure it is blue. Prints
    out pixels being tested, RGB values and "pass" or "fail"
    Testing Pixels: 253 463 RGB: 0 0 88
    Passed
    ........
    ...
    '''  
    
    original = create_image(6, 1)
    set_color(original, 0, 0,  create_color(12, 44, 122))
    set_color(original, 1, 0,  create_color(0, 128, 128))
    set_color(original, 2, 0,  create_color(127, 127, 127))
    set_color(original, 3, 0,  create_color(125, 73, 224))
    set_color(original, 4, 0,  create_color(254, 255, 255))
    set_color(original, 5, 0,  create_color(126, 127, 128))   
    
    image = blue_channel(original)    
    print("Testing Green Image...")
    for pixel in image:
        x, y, (r, g, b) = pixel
        print ("Testing Pixels:",x,y,"RGB:", r,g,b)
        if (r==0 and g==0):
            print("Passed")
        else:
            print("Failed")
            

def combine_test() -> None:
    '''Function Name: Combine Test Function
    Author: Mohamed Kaddour 101140829
    '''    
    '''
    Takes in the three images being combined and checks if their combination 
    is equal to that of the combined image. Prints out the pixel being tested
    and the RGB values. 
    >>>combine_test(r_image, g_image, b_image, combined_image)
    Testing Combined Image...
    Testing Pixels: 225 473 RGB: (151, 144, 90) with RGB: (151, 144, 90)
    ...
    ...
    ...
    '''
    
    original_image = create_image(2,1)
    set_color(original_image, 0, 0,  create_color(85, 44, 12))
    set_color(original_image, 1, 0,  create_color(24, 128, 18)) 
    
    combined_image=combine(red_channel(original_image),
                           green_channel(original_image),
                           blue_channel(original_image))
    
        
    print("Testing Combined Image...")
    for pixel in combined_image:
        x, y, (r, g, b) = pixel
        comb_pix = r,g,b
        acc_pix = get_color(original_image,x,y)
        print ("Testing Pixels:",x,y,"RGB:",comb_pix,"with RGB:", acc_pix) 
        if (acc_pix) != (comb_pix):
            print("FAILED")
        else:
            print("PASSED")

    
#MILESTONE 2 TEST FUNCTIONS:
        

def test_two_tone() -> None:
    '''Function Name: Two Tone Test
    Author: Taekwan Oh 101148069  '''  
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
        
def test_three_tone() -> None:
    '''Function Name: Three Tone Test
    Author: Taekwan Oh 101148069  '''     
    ''' tests the three-tone filter, assuming the two strings passed in are 
    black and white and gray respectivley.
    >>>test_three_tone()
    Checking pixel @(0, 0) PASSED
    ------
    Checking pixel @(1, 0) PASSED
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


def test_extreme_contrast() -> None:
    '''
    Function Name: Test Extreme Contrast
    Author: Mohamed Kaddour 101140829
    tests the the extreme_contrast functions using two sample images
    >>>test_extreme_contrast()
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
    
    ec_image = extreme_contrast(original)   
    for x, y, col in ec_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(actual, x, y))
        
def test_sepia() -> None: 
    '''Function Name: Test Sepia
    Author: Adam Burger 101141832
    '''
    """ Test function for the sepia filter which uses two sample
    images as well as the check_equal() function.
     >>>sample_test()
    Checking pixel @(0, 0) PASSED
    ------
    Checking pixel @(1, 0) PASSED
    ------
    """
    original = create_image(3, 2)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(90, 90, 90))
    set_color(original, 2, 0, create_color(255, 255, 255))
    set_color(original, 0, 1, create_color(10, 10, 10))
    set_color(original, 1, 1, create_color(0, 0, 0))
    set_color(original, 2, 1, create_color(90, 90, 90))
    
    expected = create_image(3, 2)
    set_color(expected, 0, 0, create_color(0, 0, 0))
    set_color(expected, 1, 0, create_color(103, 90, 76))
    set_color(expected, 2, 0, create_color(255, 255, 237))
    set_color(expected, 0, 1, create_color(11, 10, 9))
    set_color(expected, 1, 1, create_color(0, 0, 0))
    set_color(expected, 2, 1, create_color(103, 90, 76))
    
    new_image = sepia(original)
    for x, y, col in new_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y))
        
def test_posterize() -> None:
    '''Function Name: Test Posterize 
    Author: Kiyara Desilva 101165279
    '''     
    '''
    Tests the posterize filter function by using a sample image and 
    comparing it with the expected image. 
    >>>test_posterize
    Checking pixel @(0, 0) PASSED
    ------
    Checking pixel @(1, 0) PASSED
    ------
    Checking pixel @(2, 0) PASSED
    '''

    original = create_image(3, 1)
    set_color(original, 0, 0, create_color(177, 177, 177)) 
    set_color(original, 1, 0, create_color(0, 0, 0))
    set_color(original, 2, 0, create_color(58, 223, 144))
  

    expected = create_image(3, 1)
    set_color(expected, 0, 0, create_color(159, 159, 159))
    set_color(expected, 1, 0, create_color(31, 31, 31))
    set_color(expected, 2, 0, create_color(31, 223, 159))

    pimage = posterize(original)

    for x, y, col in pimage:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y))

def test_detect_edges() -> None:
    '''
    Function Name: Test Edge Detection
    Author: Mohamed Kaddour 101140829
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

def test_detect_edges_better() -> None:
    '''Function Name: Detect Edges Better Test
    Author: Adam Burger 101141832'''
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
        
def test_flip_vertical() -> None:
    '''Function Name: Flip Vertical Test
    Author: Taekwan Oh 101148069
    '''
    """ Returns Pass or Fail if the image is correctly flipped vetically
    test_flip_vertical().
    >>>test_flip_vertical()
    Checking pixel @(0, 0) PASSED
    ------
    Checking pixel @(1, 0) PASSED
    ------
    Checking pixel @(2, 0) PASSED
    """
    original = create_image(3, 2)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(90, 90, 90))
    set_color(original, 2, 0, create_color(255, 255, 255))
    set_color(original, 0, 1, create_color(10, 10, 10))
    set_color(original, 1, 1, create_color(0, 0, 0))
    set_color(original, 2, 1, create_color(90, 90, 90))
    
    expected = create_image(3, 2)
    set_color(expected, 0, 0, create_color(10, 10, 10))
    set_color(expected, 1, 0, create_color(0, 0, 0))
    set_color(expected, 2, 0, create_color(90, 90, 90))
    set_color(expected, 0, 1, create_color(0, 0, 0))
    set_color(expected, 1, 1, create_color(90, 90, 90))
    set_color(expected, 2, 1, create_color(255, 255, 255))
    
    flipped_vertical = flip_vertical(original)
    
    for x, y, col in flipped_vertical: 
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')'
                    , col, get_color(expected, x, y)) 


def test_flip_horizontal()-> None:
    '''Function Name: Test Flip Horizontal 
    Author: Kiyara Desilva 101165279
    '''    
    """Returns Pass or Fail if the image is correctly flipped horizontally
    >>>test_flip_horizontal() 
    Checking pixel @(0, 0) PASSED
    ------
    Checking pixel @(1, 0) PASSED
    ------
    Checking pixel @(2, 0) PASSED
    """

    original = create_image(3,2)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(40, 40, 40))
    set_color(original, 2, 0, create_color(255, 255, 255))
    set_color(original, 0, 1, create_color(100, 100, 100))
    set_color(original, 1, 1, create_color(0, 0, 0))
    set_color(original, 2, 1, create_color(40, 40, 40))
    
    
    expected = create_image(3,2)
    set_color(expected, 0, 0, create_color(40, 40, 40))
    set_color(expected, 1, 0, create_color(0, 0, 0))
    set_color(expected, 2, 0, create_color(255, 255, 255))
    set_color(expected, 0, 1, create_color(100, 100, 100))
    set_color(expected, 1, 1, create_color(0, 0, 0))
    set_color(expected, 2, 1, create_color(40, 40, 40))
    
    flipped_horizontal = flip_horizontal(original)
    
    for x, y, col in  flipped_horizontal:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')'
                    , col, get_color(expected, x, y)) 
 
        

test_red_channel()
print("------------------------------------------")
test_green_channel()
print("------------------------------------------")
test_blue_channel()
print("------------------------------------------")
combine_test()
print("------------------------------------------")
test_two_tone()
print("------------------------------------------")
test_three_tone()
print("------------------------------------------")
test_extreme_contrast()
print("------------------------------------------")
test_sepia()
print("------------------------------------------")
test_posterize()
print("------------------------------------------")
test_detect_edges()
print("------------------------------------------")
test_detect_edges_better()
print("------------------------------------------")
test_flip_vertical()
print("------------------------------------------")
test_flip_horizontal()
print("------------------------------------------")