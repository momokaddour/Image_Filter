#Group 130
#Creator: Cam Frohar

from Cimpl import *

'''-----------------------Defining all Filters----------------------------'''
def extreme_contrast(picture): 
    """ Returns a copy of an image in which the contrast between the pixels has been maximized.
    >>> extreme_contrast(image)
    """

    
    pic = copy(picture)   
     
    for x,y, (r,g,b) in pic:
        if 0 <= r <= 127:
            r = 0
        if 0 <= g <= 127:
            g = 0
        if 0 <= b <= 127:
            b = 0
        if 128 <= r <= 255:
            r = 255
        if 128 <= g <= 255:
            g = 255
        if 128 <= b <= 255:
            b = 255
        contrast_color = create_color(r,g,b)
        set_color(new_image,x,y, contrast_color)
    return pic



#Sepia
def sepia(picture):
    """Return new image with a sepia filter given the original image.
    """
  
    pic = copy(picture)       
    
    for x, y, (r, g, b) in pic:
        
        if r < 63:
            DG_pixel = create_color(r*1.1, g, b*0.9)
            set_color(image, x, y,DG_pixel)
                 
        elif 63 <= r <= 191:
            MG_pixel = create_color(r*1.15, g, b*0.85)
            set_color(image, x, y,MG_pixel)          
                
        elif r > 191:   
            LG_pixel = create_color(r*1.08, g, b*0.93)
            set_color(image, x, y,LG_pixel)          
    
    return pic



#Posterize
def _adjust_component(color:tuple)->list:
    '''This function creates a list with the appropriate RGB values
     to posterize the image'''
     
    lst= []
     
    for t in color:
    
        if t>=0 and t<=63:
            lst.append(31)
        if t>=64 and t<=127:
            lst.append(95)
        if t>=128 and t<=191:
            lst.append(159)
        if t>=192 and t<=255:
            lst.append(223)    
          
            return tuple(lst)




def posterize(picture):
    '''This sets the rgb values to those of the list created in 
    (_adjust_component)'''
    
    pic = copy(picture)
      
    for x, y, (r,g,b) in pic:
         
        rnew,gnew,bnew = _adjust_component((r,g,b))
        new_color = create_color(rnew,gnew,bnew) 
        set_color(pic, x,y, new_color)
    
    return pic


    

#Two-Tone
def two_tone(picture,color1:str,color2:str):
    '''Function takes two colors. If brightness of pixel is between 0-127, the 
    corresponding pixel is set to the first color. If the brightness of the 
    pixel is between 127-255, that corresponding pixel will be set to the 
    second color'''

    mydict = {
        "black": (0,0,0),
        "white": (255,255,255),
        "red": (255,0,0),
        "lime": (0,255,0),
        "blue": (0,0,255),
        "yellow": (255,255,0),
        "cyan": (0,255,255),
        "magenta": (255,0,255),
        "gray": (128,128,128)
        }


    pic = copy(picture) 

    
    for x, y, (r,g,b) in pic:
        
        brightness = (r+g+b)//3
     
       
        if brightness <= 127:
            
            try:
                newr,newg,newb = mydict[color1] 
            except KeyError:
                print("Not a valid first color!")
                raise 
                
        if brightness >= 128:
            
            try:
                newr,newg,newb = mydict[color2] 
            except KeyError:
                print("Not a valid second color!")
                raise 
        
        new_color = create_color(newr,newg,newb)
        set_color(pic,x,y,new_color)
        
    return pic





#Three-Tone
def three_tone(picture,color1:str,color2:str,color3:str):
    '''The function takes three colors, if the brightness of the pixel is 
    between 0-84, it is set to the first color. If the brightness of the pixel 
    is between 85-170, it is set to the second color. Lastly, if the brightness 
    of the pixel is between 171-255, it is set to the third color.'''

    mydict = {
        "black": (0,0,0),
        "white": (255,255,255),
        "red": (255,0,0),
        "lime": (0,255,0),
        "blue": (0,0,255),
        "yellow": (255,255,0),
        "cyan": (0,255,255),
        "magenta": (255,0,255),
        "gray": (128,128,128)
        }


    pic = load_image(picture) 


    for x, y, (r,g,b) in pic:
    
        brightness = (r+g+b)//3
     
       
        if brightness <= 84:
            
            try:
                newr,newg,newb = mydict[color1] 
            except KeyError:
                print("Not a valid first color!")
                raise 
                
        if brightness <= 170 and brightness >=85:
            
            try:
                newr,newg,newb = mydict[color2] 
            except KeyError:
                print("Not a valid second color!")
                raise 
            
        if brightness >= 171:
                
            try:
                newr,newg,newb = mydict[color3] 
            except KeyError:
                print("Not a valid third color!")
                raise         
                
                
        new_color = create_color(newr,newg,newb)
        set_color(pic,x,y,new_color)
        
        
    return pic




#Edge
def detect_edges(picture,threshold:int): 
    
    pic = copy(picture)
    
    max_y = get_height(pic_obj)
    
    for x, y, (r,g,b) in pic:

            
        if y<=(max_y-2):
            
            (rb,gb,bb) = get_color(pic,x,y+1)
            
            
            brightness_top = (r+g+b)//3
            brightness_bottom = (rb+gb+bb)//3
            
         
            if abs(brightness_top - brightness_bottom) > threshold:
                    
                (r,g,b) = (0,0,0)        
                
            else:
                
                (r,g,b) = (255,255,255)
    
        else:

            (r,g,b) =(255,255,255)   
            
        modified_color = create_color(r,g,b) 
        set_color(pic, x,y, modified_color)            
            
    return pic   



        

    
    

 
 #Improved Edge
def detect_edges_better(image,threshold:int):

    pic = copy(picture) 
    
    
    max_y = get_height(pic)
    max_x = get_width(pic)
    
    for x, y, (r,g,b) in pic:
            
            
        if y<=(max_y-2) and x<=(max_x-2):
            
            (rb,gb,bb) = get_color(pic,x,y+1)
            (rr,gr,br) = get_color(pic,x+1,y)
            
            brightness_top = (r+g+b)//3
            brightness_bottom = (rb+gb+bb)//3
            brightness_right = (rr+gr+br)//3
            
         
            if abs(brightness_top - brightness_bottom) > threshold or abs(brightness_top - brightness_right) > threshold:
                    
                (r,g,b) = (0,0,0)     
        
            else:
                
                (r,g,b) = (255,255,255)
    
        else:

            (r,g,b) =(255,255,255)   
            
        modified_color = create_color(r,g,b) 
        set_color(pic, x,y, modified_color)            
            
    return pic   


       
        
        
 #Vertical Flip
def flip_vertical(picture):
    """Reurns a vertically flipped copy of that image
    """
    pic= copy(picture)
    width = get_width(pic)
    height = get_height(pic)

    for y in range(height):
        for x in range(width//2):
            replace = get_color(pic,(width-1)-x,y)
            set_color(pic,(width-1)-x,y,get_color(pic,x,y))
            set_color(pic,x,y,replace)
    return pic
    
    


#Horizontal Flip
def flip_horizontal(picture):
    
    image_height = get_height(pic)
    
    for pixel in pic:
        x,y,(r, g, b) = pixel
        col= get_color(pic, x, image_height-y-1)
        set_color(pic, x, y, col)
        
    return pic




'''-------------------------Defining all Filters----------------------------'''


run = True
image = None
while run == True:
    task = input("L)oad image  S)ave-as\n2)-tone  3)-tone  X)treme contrast  T)int sepia  P)osterize\nE)dge detect  I)mproved edge detect  V)ertical flip  H)orizontal flip\nQ)uit\n: ")
    
    task = task.upper()
    
    if task == "L":
        image = load_image(choose_file())
    elif task == "S":
        save_as(image)
    elif task == "Q":
        run = False
    else:
        if image == None:
            print("No Image Loaded")
        else:
            if task == "2":
                
                two_tone_color1 = input("Color 1:\n")
                two_tone_color2= input("Color 2:\n")
                    
                show(two_tone(image,two_tone_color1,two_tone_color2))
                
            elif task == "3":
                
                three_tone_color1 = input("Color 1:\n")
                three_tone_color2= input("Color 2:\n")
                three_tone_color3= input("Color 3:\n")
                
                show(three_tone(image,three_tone_color1,three_tone_color2,three_tone_color3))    
                
                
            elif task == "X":
                
                show(extreme_contrast(image))
                
            elif task == "T":
                
                show(sepia(image))
                
            elif task == "P":
                
                show(posterize(image))
                
            elif task == "E":
                
                edge_chosen_threshold = input("Threshold:\n")
                
                show(detect_edges(image,edge_chosen_threshold))    
                
            elif task == "I":
                
                improved_chosen_threshold = input("Threshold:\n")
                show(detect_edges_better(image,improved_chosen_threshold))
                
            elif task == "V":
                
                show(flip_vertical(image))
                
            elif task == "H":
                
                show(flip_horizontal(image))    

