'''
ECOR 1051: two tone filter
Team Identifer: 60
Mohamed Kaddour
101140829
Winter 2020
'''

from Cimpl import choose_file, load_image, copy, create_color, set_color,\
                  show, Image, get_color, create_image



def two_tone (image:Image,colour1:str,colour2:str) -> Image:
    '''
    Function Name: two_tone
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


filename = "p2-original.jpg"
filename = copy(load_image(filename))
twop_img = two_tone(filename, "black", "white")
show(twop_img)