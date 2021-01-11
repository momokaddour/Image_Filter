'''
Red, Green, Blue and Combine Image Filters
Group 60
ECOR 1051 - Group Project - Milestone 1 - P3

Authors:
Mohamed Kaddour (TL)
Kiyara De Silva
Taekwan Oh
Adam Burger

Date:
2020-03-13

Description: Takes in an image and then puts on red, green and blue filters 
for each. It then returns a combined image of the all the filtered images, 
which should be the original image. 

'''



from Cimpl import choose_file, load_image, copy, create_color, set_color,\
                  show, Image, get_color


#Image Filter Functions


'''red_channel Function
Author: Adam Burger'''
def red_channel(image:Image) -> Image:
    
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



'''green_channel Function
Author: Kiyara Desilva'''
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

'''blue_channel Function
Author: Taekwan Oh'''
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

'''combine Function
Author: Mohamed Kaddour'''
def combine(red_image:Image, green_image:Image, blue_image:Image) -> Image:
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

#Testing Images Functions

'''test_red_channel Function
Author: Adam Burger'''
def test_red_channel (image:Image) -> None:
    '''Takes in an image and checks each pixel to ensure it is red. Prints
    out pixels being tested, RGB values and "pass" or "fail"
    >>>test_red_channel(red_image)
    Testing Pixels: 541 445 RGB: 104 0 0
    Passed
    .......
    ...
    '''
    print("Testing Red Image...")
    for pixel in image:
        x, y, (r, g, b) = pixel
        print ("Testing Pixels:",x,y,"RGB:", r,g,b)
        if (g==0 and b==0):
            print("Passed")
        else:
            print("Failed")
            

'''test_green_channel Function
Author: Kiyara Desilva'''
def test_green_channel (image:Image) -> None:
    '''Takes in an image and checks each pixel to ensure it is green. Prints
    out pixels being tested, RGB values and "pass" or "fail"
    >>test_green_channel(green_image)
    Testing Pixels: 310 402 RGB: 0 6 0
    Passed
    ........
    ...
    '''    
    print("Testing Green Image...")
    for pixel in image:
        x, y, (r, g, b) = pixel
        print ("Testing Pixels:",x,y,"RGB:", r,g,b)
        if (r==0 and b==0):
            print("Passed")
        else:
            print("Failed")


'''test_blue_channel Function
Author: Taekwan Oh'''
def test_blue_channel (image:Image) -> None:
    '''Takes in an image and checks each pixel to ensure it is blue. Prints
    out pixels being tested, RGB values and "pass" or "fail"
    Testing Pixels: 253 463 RGB: 0 0 88
    Passed
    ........
    ...
    '''  
    print("Testing Green Image...")
    for pixel in image:
        x, y, (r, g, b) = pixel
        print ("Testing Pixels:",x,y,"RGB:", r,g,b)
        if (r==0 and g==0):
            print("Passed")
        else:
            print("Failed")
            

'''combine_test Function
Author: Mohamed Kaddour'''
def combine_test(red_image,green_image,blue_image,combined_image):
    '''
    Takes in the three images being combined and checks if their combination 
    is equal to that of the combined image. Prints out the pixel being tested
    and the RGB values. 
    >>>combine_test(r_image, g_image, b_image, combined_image)
    Testing Combined Image...
    Testing Pixels: 225 473 RGB: (151, 144, 90) with RGB: (151, 144, 90)
    ...
    ...
    ...
    '''
   
    print("Testing Combined Image...")
    for pixel in combined_image:
        x, y, (r, g, b) = pixel
        comb_pix = r,g,b
        r1,g,b = get_color(red_image,x,y)
        r,g1,b = get_color(green_image,x,y)
        r,g,b1 = get_color(blue_image,x,y)
        acc_pix = (r1,g1,b1)
        print ("Testing Pixels:",x,y,"RGB:",comb_pix,"with RGB:", acc_pix) 
        if (acc_pix) != (comb_pix):
            print("FAILED")
        else:
            print("PASSED")
            
  
  
'''Program Body'''          
filename = "p2-original.jpg"
filename = copy(load_image(filename))

red_image = red_channel(filename)
green_image = green_channel(filename)
blue_image = blue_channel(filename)
combined_image = combine(red_image,green_image,blue_image)

#Displaying
print("Showing Red Image")
show(red_image)
print("Showing Green Image")
show(green_image)
print("Showing Blue Image")
show(blue_image)
print("Showing Combined Image")
show(combined_image)


#Testing: 

test_red_channel(red_image)
test_green_channel(green_image)
test_blue_channel(blue_image)
combine_test(red_image, green_image, blue_image, combined_image)
