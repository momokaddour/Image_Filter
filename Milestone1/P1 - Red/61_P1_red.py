'''
ECOR 1051: red-channel Filter
Mohamed Kaddour
101140829
Winter 2020
'''

from Cimpl import choose_file, load_image, copy, create_color, set_color,\
                  show, Image, get_color


def red_channel(image:Image) -> Image:
    '''Return a copy of the provided image that is completley red, (r,0,0).
    Each pixel of the image must be red
    >>> image = load_image(choose_file()) 
    >>> red_image = red_channel(image)
    >>> show(red_image)
    '''
    
    new_image = copy(image)
    for pixel in image:
        x, y, (r, g, b) = pixel        
        red = create_color(r,0,0)
        set_color(new_image, x, y, red)
    return new_image


def green_channel(image:Image) -> Image:
    '''Return a copy of the provided image that is completley green, (0,g,0).
    Each pixel of the image must be green
    >>> image = load_image(choose_file()) 
    >>> green_image = green_channel(image)
    >>> show(green_image)
    '''
    
    new_image = copy(image)
    for pixel in image:
        x, y, (r, g, b) = pixel        
        green = create_color(0,g,0)
        set_color(new_image, x, y, green)
    return new_image


def blue_channel(image:Image) -> Image:
    '''Return a copy of the provided image that is completley blue, (0,0,b).
    Each pixel of the image must be blue.
    >>> image = load_image(choose_file()) 
    >>> blue_image = blue_channel(image)
    >>> show(blue_image)
    '''
    
    new_image = copy(image)
    for pixel in image:
        x, y, (r, g, b) = pixel        
        green = create_color(0,0,b)
        set_color(new_image, x, y, green)
    return new_image    


def test_red_channel (image:Image) -> None:
    print("Testing Red Image...")
    failed_pixels = []
    passed = False
    for pixel in image:
        x, y, (r, g, b) = pixel
        #print ("Testing Pixels:",x,y,"RGB:", r,g,b)
        if (g==0 and b==0):
            passed = True
        else:
            #print("FAIL")
            pix = x,y
            failed_pixels.append(pix)
    
    if len(failed_pixels) > 0:
        print("Test Failed...Failed Pixels:")
        print(failed_pixels)        
    else:
        print("Test Passed")
            


image = load_image(choose_file())
red_image = red_channel(image)
show(red_image)
test_red_channel(red_image)

image = load_image(choose_file())
green_image = green_channel(image)
show(green_image)

image = load_image(choose_file())
blue_image = blue_channel(image)
show(blue_image)


def combine(red_image:Image, green_image:Image, blue_image:Image) -> Image:
    '''Takes in three images, a red one, a green one and a blue one and returns
    one image which is the a combination of all three
    >>> combined_image = combine(red_image, green_image, blue_image)
    >>> show(combined_image)
    '''
    
    new_image = copy(red_image)
    for pixel in new_image:     
        x, y, (r,b,g) = pixel
        r1,g1,b = get_color(green_image,x,y)
        r1,g,b1 = get_color(blue_image,x,y)
        original = create_color(r,g1,b1)
        set_color(new_image, x, y, original)  
    return new_image

def combine_test(red_image,green_image,blue_image,combined_image):
   
    print("Testing Combined Image...")
    failed_pixels = []
    passed = False
    for pixel in combined_image:
        x, y, (r, g, b) = pixel
        comb_pix = r,g,b
        r1,g,b = get_color(red_image,x,y)
        r,g1,b = get_color(green_image,x,y)
        r,g,b1 = get_color(blue_image,x,y)
        acc_pix = (r1,g1,b1)
        #print ("Testing Pixels:",x,y,"RGB:",comb_pix,"with RGB:", acc_pix) 
        if (acc_pix) == (comb_pix):
            passed = True
            #print("PASSED")
        else:
            #print("FAILED")
            pix = x,y
            failed_pixels.append(pix)
            
    if len(failed_pixels) > 0:
        print("Test Failed...Failed Pixels:")
        print(failed_pixels)        
    else:
        print("Test Passed")


combined_image = combine(red_image, green_image, blue_image)
show(combined_image)
combine_test(r_image, g_image, b_image, combined_image)
        
    
        