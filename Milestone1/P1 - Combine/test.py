from Cimpl import*

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
        blue = create_color(0,0,b)
        set_color(new_image, x, y, blue)
    return new_image    


def test_blue_channel (image:Image) -> None:
    print("Testing Blue Image...")
    for pixel in image:
        x, y, (r, g, b) = pixel
        print ("Testing Pixels:",x,y,"RGB:", r,g,b)
        if (g==0 and r==0):
            print("Pass")
        else:
            print("FAIL")  
    
filename = 'p2-original.jpg' 
image = copy(load_image(filename))
new_image = blue_channel(image)
show(new_image)
test_blue_channel(new_image)
