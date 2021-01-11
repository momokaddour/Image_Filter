'''
ECOR 1051: combine-channel Filter
Author: Mohamed Kaddour
101140829
Winter 2020
'''

from Cimpl import choose_file, load_image, copy, create_color, set_color,\
                  show, Image, get_color


def combine(red_image:Image, green_image:Image, blue_image:Image) -> Image:
    '''Takes in three images, a red one, a green one and a blue one and returns
    one image which is the a combination of all three
    >>> combined_image = combine(red_image, green_image, blue_image)
    >>> show(combined_image)
    '''
    
    new_image = copy(red_image)
    
    for pixel in new_image:     
        x, y, (r,b,g) = pixel
        r1,g1,b = get_color(green_image,x,y)
        r1,g,b1 = get_color(blue_image,x,y)
        original = create_color(r,g1,b1)
        set_color(new_image, x, y, original)  
    return new_image

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

r_image = "red_image.png"
g_image = "green_image.png"
b_image = "blue_image.png"
r_image = load_image(r_image)
g_image = load_image(g_image)
b_image = load_image(b_image)

combined_image = combine(r_image, g_image, b_image)
show(combined_image)
combine_test(r_image, g_image, b_image, combined_image)