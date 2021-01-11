from Cimpl import choose_file, load_image, copy, create_color, set_color,\
                  show, Image, get_color

def black_channel(image:Image) -> Image:
    '''Return a copy of the provided image that is completley red, (r,0,0).
    Each pixel of the image must be red
    >>> image = load_image(choose_file()) 
    >>> red_image = red_channel(image)
    >>> show(red_image)
    '''
    
    new_image = copy(image)
    for pixel in image:
        x, y, (r, g, b) = pixel  
        r = 30
        black = create_color(r,0,0)
        set_color(new_image, x, y, black)
    return new_image


show(black_channel(copy(load_image("Bear.jpg"))))

