'''
ECOR 1051
Milestone 3
2020-04-02
Team Identifier: 60
Image Filters

Team Members:
Mohamed Kaddour (TL)
Adam Burger
Kiyara Desilva 
Taekwan Oh

PUSHED
'''

from Cimpl import choose_file, load_image, copy, create_color, set_color,\
                  show, Image, get_color, create_image, get_width, get_height

#FROM PROVIDED 1051 SAMPLE FILTERS
def grayscale(image: Image) -> Image:
    """Return a grayscale copy of image.
   
    >>> image = load_image(choose_file())
    >>> gray_image = grayscale(image)
    >>> show(gray_image)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:

        # Use the pixel's brightness as the value of RGB components for the 
        # shade of gray. These means that the pixel's original colour and the
        # corresponding gray shade will have approximately the same brightness.
        
        brightness = (r + g + b) // 3
        
        # or, brightness = (r + g + b) / 3
        # create_color will convert an argument of type float to an int
        
        gray = create_color(brightness, brightness, brightness)
        set_color(new_image, x, y, gray)      
    return new_image


#HELPER FUNCTION FOR THE POSTERIZING FUNCTION
def _adjust_component(val: int) -> int:     
    '''
    Takes in an integer and returns an integer depending on the value
    of the passed in integer. The goal is to determine in which quadrant
    the specific pixel lies.
    >>>_adjust_component(22)
    31
    >>>_adjust_components(188)
    159
    '''
    new_val = 0
    
    if val <= 63:
        new_val = 31
    elif val <= 127:
        new_val = 95
    elif val <= 191:
        new_val = 159
    elif val <= 255:
        new_val = 223
    return new_val


#MILESTONE 1 FILTERS INCLUDE: RED, BLUE, GREEN, COMBINE


def red_channel(image:Image) -> Image:
    
    ''' Function Name: Red Channel
    Author: Adam Burger 101141832
    '''    
    '''Return a copy of the provided image that is completley red, (r,0,0).
    Each pixel of the image must be red
    >>> image = load_image(choose_file()) 
    >>> red_image = red_channel(image)
    >>> show(red_image)
    '''                
    
    new_image = copy(image)
    for pixel in new_image:
            x, y, (r,g,b) = pixel
    new_image = copy(image)
    for pixel in image:
            x, y, (r,g,b) = pixel
            red = create_color(r,0,0)
            set_color(new_image,x,y, red)
    return new_image    



def green_channel(image:Image) -> Image:
    '''Function Name: Green Channel
    Author: Kiyara Desilva 101165279
    '''    
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
    '''Function Name: Blue Channel
    Author: Taekwan Oh 101148069
    '''   
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

def combine(red_image:Image, green_image:Image, blue_image:Image) -> Image:
    '''Function Name: Combine 
    Author: Mohamed Kaddour 101140829
    '''    
    '''Takes in three images, a red one, a green one and a blue one and returns
    one image which is the a combination of all three
    >>> combined_image = combine(red_image, green_image, blue_image)
    >>> show(combined_image)
    '''
    
    new_image = copy(red_image)
    
    for pixel in new_image:     
        x, y, (r,g,b) = pixel
        r1,g1,b = get_color(green_image,x,y)
        r1,g,b1 = get_color(blue_image,x,y)
        original = create_color(r,g1,b1)
        set_color(new_image, x, y, original)  
    return new_image


#MILESTONE 2, P4 FILTERS INCLUDE: TWO AND THREE TONE, EXTREME CONTRAST, 
#SEPIA TINTING, POSTERIZING. 


def two_tone (image:Image,colour1:str,colour2:str) -> Image:
    '''
    Function Name: Two Tone
    Author: Mohamed Kaddour 101140829
    '''    
    '''Returns a filtered image consisting of the two colours passed in as 
    strings from a list of colors:
    black
    white
    red
    lime
    yellow
    cyan
    magenta
    gray
    >>> two_tone(filename, "red", "blue")
    -> Displays proper image.
    >>> two_tone(filename, "green", "purple") 
    -> Displays incorrect image.
    '''
    
    
    colours = {'black':(0,0,0), 'white':(255,255,255), 'red':(255,0,0), 'lime':
               (0,255,0), 'blue':(0,0,255), 'yellow':(255,255,0), 'cyan':
               (0,255,255), 'magenta':(255,0,255), 'gray':(128,128,128)}
    

    
    new_image = copy(image)
    new_colour = create_color(0,0,0)
    rgb = (0,0,0)
    
    for pixel in image:
        x, y, (r, g, b) = pixel 
        avg = (r + b + g)/3
        if 0 <= avg <= 127:
            rgb = colours[colour1]
            new_colour = create_color(rgb[0],rgb[1],rgb[2])
            set_color(new_image, x, y, new_colour)
        elif 128 <= avg <= 255:
            rgb = colours[colour2]
            new_colour = create_color(rgb[0],rgb[1],rgb[2])
            set_color(new_image, x, y, new_colour)
        
    return new_image

def three_tone (image:Image,colour1:str,colour2:str,colour3:str) -> Image:
    ''''
    Function Name: Three Tone
    Author: Mohamed Kaddour 101140829
    
    '''    
    '''Returns a filtered image consisting of the three colours passed in as 
    strings from a list of colors:
    black
    white
    red
    lime
    yellow
    cyan
    magenta
    gray
    >>> three_tone(filename, "red", "blue")
    -> Displays proper image.
    >>> three_tone(filename, "green", "purple") 
    -> Displays incorrect image.
    '''    
    
    colours = {'black':(0,0,0), 'white':(255,255,255), 'red':(255,0,0), 'lime':
               (0,255,0), 'blue':(0,0,255), 'yellow':(255,255,0), 'cyan':
               (0,255,255), 'magenta':(255,0,255), 'gray':(128,128,128)} 
    
    new_image = copy(image)
    new_colour = create_color(0,0,0)
    rgb = (0,0,0)
    
    for pixel in image:
        x, y, (r, g, b) = pixel 
        avg = (r + b + g)/3
        if 0 <= avg <= 84:
            rgb = colours[colour1]
            new_colour = create_color(rgb[0],rgb[1],rgb[2])
            set_color(new_image, x, y, new_colour)
        elif 85 <= avg <= 170:
            rgb = colours[colour2]
            new_colour = create_color(rgb[0],rgb[1],rgb[2])
            set_color(new_image, x, y, new_colour)
        elif 170 <= avg <= 255:
            rgb = colours[colour3]
            new_colour = create_color(rgb[0],rgb[1],rgb[2])
            set_color(new_image, x, y, new_colour)            
        
    return new_image


def extreme_contrast(image:Image) -> Image:
    '''
    Function Name: Extreme Contrast
    Author: Taekwan Oh 101148069
    '''
    '''
    Returns an extremely contrasted copy of the image passed in by looking 
    at the brightness of each colour in each pixel in the passed in image.
    >>>show(extreme_contrast(filename))
    displays expected image
    '''
    
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


def sepia(original:Image) -> Image:
    """
    Function Name: Sepia
    Author: Kiyara De Silva 101165279
    """
    """
    Returns a greyscale image where the red and blue components are adjusted 
    so the image is slightly yellowish
    >>>show(sepia(filename))
    displays expected image
    """
    
    gray_image = grayscale(original)
    new_image = copy(gray_image)
    
    for pixel in gray_image:
        x, y, (r, g, b) = pixel
        
        if r < 63:
            new_colour_filter = create_color(r *1.1, g , b *0.9)
            set_color (new_image, x, y, new_colour_filter)  
            
        elif 63 <= r <= 191:
            new_colour_filter = create_color(r *1.15, g , b *0.85)
            set_color (new_image, x, y, new_colour_filter)  
            
        else:
            new_colour_filter = create_color(r *1.08, g , b *0.93)
            set_color (new_image, x, y, new_colour_filter)         
    
    return new_image

def posterize(image: Image) -> Image:
    ''' Function Name: Posterize 
    Author: Adam Burger 101141832
    '''       
    """
    Returns a copy of the image passed in with the posterize filter applied.
    Uses the _adjust_component function.
    >>>posterize(filename)
    [Displays expected image]
    """

    new_image = copy(image)
    for pixel in image:
        x, y, (r, g, b) = pixel
        set_color(new_image, x, y, create_color(_adjust_component(r),
                                                _adjust_component(g),
                                                _adjust_component(b)))

    return new_image

#MILESTONE 2, P5 FILTERS INCLUDE: EDGE DETECTION, IMPROVED EDGE DETECTION,
#VERTICAL FLIPPING, HORIZONTAL FLIPPING.

def detect_edges(image:Image,threshold:float) -> Image:
    '''
    Function Name: Detect Edges
    Author: Adam Burger 101141832
    '''
    ''' Takes in an original image as well as a thershold as a float and 
    returns and an image with the edge detection filter applied
    based on the value of the threshold. This filter compares the brightness
    of a pixel's lower pixels and then prints on a filter similar to
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
            r2,g2,b2 = get_color(new_image,x,y+1)
            
            brightness1 = (r1+g1+b1)/3
            brightnessv = (r2+g2+b2)/3
  
            
            if abs(brightness1-brightnessv) >= threshold:
                black = create_color(0,0,0)
                set_color(new_image, x, y, black)      
            else: 
                white = create_color(255,255,255)
                set_color(new_image, x, y, white)
                  
               
    return new_image  

def detect_edges_better(image:Image,threshold:float) -> Image:
    '''
    Function Name: Detect Edges Better
    Author: Mohamed Kaddour 101140829
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


def flip_horizontal(image:Image) ->Image:
    '''
    Function Name: Flip Horizontal 
    Author: Taekwan Oh 101148069
    '''
    """ Returns a horizontally flipped copy of the image.
    >>>show(flip_horizontal(filename))
    [displays expected image]
    """
    new_image_horizontal = copy(image)
   
    width = get_width(new_image_horizontal) - 1 # rotates the height of image
    height = get_height(new_image_horizontal) - 1 # rotates the width of image
   
    for h in range(height):
        for w in range((width//2)+1):
            color1 = get_color(image, w, h)
            color2 = get_color(image, width-w-1, h)
            set_color(new_image_horizontal, width-w-1, h, color1)
            set_color(new_image_horizontal, w, h, color2)
    return new_image_horizontal

def flip_vertical(image: Image) -> Image:
    '''
    Function Name: Flip Vertical
    Author: Kiyara De Silva 101165279
    '''
    """ Returns a vertically flipped copy of the image.
    >>>show(flip_vertical(filename))
    [displays expected image]
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

