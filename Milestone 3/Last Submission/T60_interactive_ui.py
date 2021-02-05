'''
ECOR 1051
Milestone 3
2020-04-02
Team Identifier: 60
Interactive UI

Team Members:
Mohamed Kaddour(TL) - 101140829
Adam Burger - 101141832
Kiyara De Silva - 101165279
Taekwan Oh - 101148069

PUSHED
'''

from T60_image_filters import *

from Cimpl import choose_file, load_image, copy, create_color, set_color,\
                  show, Image, get_color, create_image, get_width, get_height,\
                  save_as

run = True
image = None

while run == True:
    filterinput = input("L)oad image  S)ave-as\n2)-tone  3)-tone  X)treme contrast"
                       + " T)int sepia  P)osterize\nE)edge detect  I)mproved edge detect"
                       + " V)ertical flip  H)orizontal flip\nQ)uit\n\n: ") 
   
    if filterinput == "L" or filterinput == "l":
        image = copy(load_image(choose_file()))
        show(image)
        
    elif filterinput == "S" or filterinput == "s":
        if image is None:
            print("Please load an image")
        else:
            filename = input("Please enter a filename with the type of file"+
                             "(example: mypicture.jpg)\n: ")
            save_as(image,filename)
            
    elif filterinput == '2':
        if image is None:
            print("Please load an image")
        else:
            image = two_tone(image,"yellow", "cyan")
            show(image)
            
    elif filterinput == '3':
        if image is None:
            print("Please load an image")
        else:
            image = three_tone(image,"yellow","magenta","cyan")
            show(image) 
            
    elif filterinput == 'X' or filterinput == "x":
        if image is None:
            print("Please load an image")
        else:
            image = extreme_contrast(image)
            show(image)    
    
    elif filterinput == 'T' or filterinput == "t":
        if image is None:
            print("Please load an image")
        else:
            image = sepia(image)
            show(image)    
            
    elif filterinput == 'P' or filterinput == "p":
        if image is None:
            print("Please load an image")
        else:
            image = posterize(image)
            show(image)      
            
    elif filterinput == 'E' or filterinput == "e":
        if image is None:
            print("Please load an image")
        else:
            threshold = float(input(("Please enter a threshold")))
            image = detect_edges(image, threshold)
            show(image)        
            
    elif filterinput == 'I' or filterinput == "i":
        if image is None:
            print("Please load an image")
        else:
            threshold = float(input(("Please enter a threshold")))
            image = detect_edges_better(image, threshold)
            show(image)              
    
    elif filterinput == 'V' or filterinput == "v":
        if image is None:
            print("Please load an image")
        else:
            image = flip_vertical(image)
            show(image)  
            
    elif filterinput == 'H' or filterinput == "h":
        if image is None:
            print("Please load an image")
        else:
            image = flip_horizontal(image)
            show(image)      
    
    elif filterinput == "Q" or filterinput == "q":
        run = False
    
    else:
        print("Please enter a valid command")
     
    
