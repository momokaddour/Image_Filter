'''
ECOR 1051
Milestone 3
2020-04-02
Team Identifier: 60
Batch UI

Team Members:
Mohamed Kaddour(TL) - 101140829
Adam Burger - 101141832
Kiyara De Silva - 101165279
Taekwan Oh - 101148069
'''

from T60_image_filters import *

from Cimpl import choose_file, load_image, copy, create_color, set_color,\
                  show, Image, get_color, create_image, get_width, get_height,\
                  save_as


def inputanalysis (filterinput:str,image:Image) -> Image:
        '''
        Takes in a string as a command as well as the loaded image 
        and returns the image with the commanded filter applied.
        >>>inputanalysis('T',copy(load_image('image.jpg')))
        [returns the image with the filter applied]
        '''
        
        if filterinput == '2':
                image = two_tone(image,"yellow", "cyan")
                
        elif filterinput == '3':
                image = three_tone(image,"yellow","magenta","cyan")
                
        elif filterinput == 'X' or filterinput == "x":
                image = extreme_contrast(image)   
        
        elif filterinput == 'T' or filterinput == "t":
                image = sepia(image)
         
        elif filterinput == 'P' or filterinput == "p":
                image = posterize(image)     
                
        elif filterinput == 'E' or filterinput == "e":
                image = detect_edges(image, 10)        
                
        elif filterinput == 'I' or filterinput == "i":
                image = detect_edges_better(image, 10)             
        
        elif filterinput == 'V' or filterinput == "v":
                image = flip_vertical(image)
                
        elif filterinput == 'H' or filterinput == "h":
                image = flip_horizontal(image)   
                
        return image
    

file = open("batch_sample.txt", "r")
lines = file.readlines()
for line in lines: #Goes through each line element in the lines list in the file 
        commands = line.split(" ")#Splits each line into a list based on the space
        image = copy(load_image(commands[0]))#Define the name of the image(constant)
        filename = commands[1] #Define the filename (constant)
        del commands[0:2]
        for filterinput in commands: #Goes through each command in the commands list
                image = inputanalysis(filterinput,image)
        save_as(image,filename) #Saves the image after every command is looked at. 

file.close()
    