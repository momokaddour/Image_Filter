'''
ECOR 1051: improved edge detection filter
Team Identifer: 60
Mohamed Kaddour
101140829
Winter 2020
'''

from Cimpl import  *

def detect_edges_better(image:Image,threshold) -> Image:
     
     new_image = copy(image)
     
     width = get_width(new_image)
     height = get_height(new_image)     
     
     for x in range(width-1):
          for y in range(height-1):
               
               r1,g1,b1 = get_color(new_image,x,y)
               r2,g2,b2 = get_color(new_image,x+1,y+1)
               
               brightness1 = r1+g1+b1/3
               brightness2 = r2+g2+b2/3
     
               
               if abs(brightness1-brightness2) >= threshold:
                    black = create_color(0,0,0)
                    set_color(new_image, x, y, black)      
               elif abs(brightness1 - brightness2) <= threshold:
                    white = create_color(255,255,255)
                    set_color(new_image, x, y, white)
                    
               
     return new_image

def test_detect_edges_better():
     #Creates the test image
     original = create_image(6, 1)
     set_color(original, 0, 0,  create_color(0, 0, 0))
     set_color(original, 1, 0,  create_color(0, 128, 128))
     set_color(original, 2, 0,  create_color(127, 127, 127))
     set_color(original, 0, 1,  create_color(125, 73, 224))
     set_color(original, 0, 2,  create_color(254, 255, 255))
     set_color(original, 0, 3,  create_color(126, 127, 128))  
     
     actual = create_image(6, 1)
     set_color(actual, 0, 0,  create_color(0, 0, 0))
     set_color(actual, 1, 0,  create_color(0, 255, 255))
     set_color(actual, 2, 0,  create_color(0, 0, 0))
     set_color(actual, 0, 1,  create_color(0, 0, 255))
     set_color(actual, 0, 2,  create_color(255, 255, 255))
     set_color(actual, 0, 3,  create_color(0, 0, 255))    
     
     twot_image = extreme_contrast(original)   
     for x, y, col in twot_image:
         check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(actual, x, y))     
     
                    
            
            




filename = "p2-original.jpg"
filename = copy(load_image(filename))
show(detect_edges_better(filename,30))