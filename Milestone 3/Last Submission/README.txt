Image Editing Program 60 version 1.0 07/04/2020

PRICING
-------
starting $4.99 CAD

DESCRIPTION
------------
This photo editing program is an easy to use and efficient application which allows you to place many 
filters on an image of your choice. Filters that are available include 2-tone, 3-tone, extreme contrast,
tint sepia, posterize, edge detection, improved edge detection, vertical flip and horizontal flip. This program 
also allows you to stack image filters and save multiple copies of an image at any time. It also includes a 
batch feature if you would like to apply filters onto many images. 

INSTALLATION
-------------
when installing the program on windows or mac, it is recommended that
you open the file in any python IDE (wing, pycharm etc.). Windows XP
and OS X 10.6 or later are required to install and run the IDE. Python version
3.8.2 or later is recommended. That latest pip version (19.2.3) is also recommended 
in order to install pillow.
Installing pillow is done through cmd where you must simply type 'pip install pillow'.

USAGE(MAIN PROGRAM)
-------------------
- If using the wing IDE, press the run button in order to begin running the program.
- It is recommended that you load an image prior to selecting an image filter on the interface and
doing so will open up a prompt to select an image of your choice. 
>>> L 
[opens file for image selection]
- Using the nine different image filters, you can now apply them onto the image by selecting the letter to 
the left of the name of the filter. 
NOTES: 
*Image filters stack up
*Program accepts both capital and lowercase commands
>>> 2
[Applies 2 tone filter onto loaded image]
>>> V
[Flips the 2 tone image vertically]
- At anytime, you may press the "s" button to save the image. You will be prompted to enter the 
image name that it will be saved under. 
>>> s
Please enter a filename with the type of file (example: mypicture.jpg):
>>> mypicture.jpg
[saves picture under mypicture.jpg name]
- To quit the program at any time, press the q button. 
WARNING: Doing this will erase any image filters you have applied

FINAL NOTE: For the edge detection and improved edge detection filters, you will be prompted to enter a 
threshold as well. 
>>>E
Please enter a threshold
>>> 30
[displays an image with the 30 thershold applied]

USAGE(BATCH)
------------
- In order to use the batch UI feature, you must first open the file named "batch_sample.txt".
- Then you must enter several different commands in a particular order as seen below:
<Name of original image with extension><one space><name of new image with extension><one space>
<letter corresponding to the image filter><one space>
*There are already 2 premade examples in the file.

NOTE: You can apply as much filters as you want to a single image but there must be a space at the end 
of each line. 
- To add another image, simply press enter and repeat the process for as many lines as you want. 

Credits
--------
Mohamed Kaddour: 
Filters: two tone filter, three tone filter, improved edge detection,
Tests: extreme contrast, edge detection
Additional: planning, batch UI, interactive UI, re-factoring, README

Taekwan Oh:
Filters: extreme contrast, flip horizontal
Tests: two tone filter, three tone filter, flip vertical
Additional: planning, batch UI, interactive UI, re-factoring, README 

Kiyara De Silva: 
Filters: sepia filter, flip vertical
Tests: posterize filter, flip horizontal
Additional: planning, batch UI, interactive UI, re-factoring, README

Adam Burger: 
Filters: posterize, detect edges
Tests: sepia, detect edges better
Additional: planning, batch UI, interactive UI, re-factoring, README

Image Editing Program 60 can be reached at:
----------------------------------------

Mohamed Kaddour - 101140829
mohamedkaddour@cmail.carleton.ca

Copyright © 2020 Team 60-ECOR 1051. All right reserved. 
Image Editing Program 60 and its use are subject to a license agreement and are
also subject to copyright, trademark, patent and/or other laws. 
Refer to the user guide or www.Examplet.com/legal for additional
information about Example patents.
All other brand and product names are trademarks or registered