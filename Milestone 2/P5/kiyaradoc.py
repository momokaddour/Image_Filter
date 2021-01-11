
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
    
    
def flip_vertical(image: Image) -> Image:
    """ Returns a vertically flipped copy of the image.
   
    image = load_image(choose_file())
    new_vertical = flip_vertical(image)
    show(new_vertical
    """
    new_image_vertical = copy(image)
   
    width = get_width(new_image_vertical) 
    height = get_height(new_image_vertical)
   
    for w in range(width):
        for h in range(height//2):
            color1 = get_color(new_image_vertical, w, h)
            color2 = get_color(new_image_vertical, w, height -h-1)
            
            set_color(new_image_vertical, w, height-h-1, color1)  
            set_color(new_image_vertical, w, h, color2)            
    return new_image_vertical


def test_flip_vertical() -> None:
    """ Returns Pass or Fail if the image is correctly flipped vetically
    test_flip_vertical()
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
    
    for x, y, col in flipped_vertical: # tests each colour of each pixel of the filtered sample image and compares it to the expected image
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')', col, get_color(expected, x, y))   
    
test_flip_vertical()