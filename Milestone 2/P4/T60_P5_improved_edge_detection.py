'''
ECOR 1051: Improved Edge Detection Filter
Team Identifer: 60
Mohamed Kaddour
101140829
Winter 2020
'''

from Cimpl import choose_file, load_image, copy, create_color, set_color,\
                  show, Image, get_color, create_image, get_width, get_height



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