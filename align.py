#Isaac, you request this... Also, I didn't paste all of your code in here, and I also renamed some variables for my own sake
#So just copy and paste this code, and then re-adjust your code... haha... - James

#Also, Isaac, I'm planning on debugging this with you together. If it works on the first try... Wow, because I did no debugging, all of this was done in my head, and also my head is hurting 👍

## Also, Isaac, thanks for the code you put in the testing.py, helped me alot 😉 ##



from PIL import Image, ImageDraw, ImageFont
import os
import random

files = [] #list of files, I'm going to give you them
#btw, I'm making another folder in assets called backgrounds, ok?
files = os.listdir('assets/backgrounds') #gives me a list of all files and directories
#this is why I needed to create a separate folder @Isaac

file = random.choice(files)

img = Image.open('assets/backgrounds/' + str(file)) #renamed this from im to img, sorry
paint = ImageDraw.Draw(img) #renamed this from d to paint, sorry
fnt = ImageFont.truetype('assets/arial.ttf', 82)

width, height = img.size 

clock = "20:01" #renamed this from ftime, not sorry, what sorta name is ftime? If I get a dog, I'll name it atime.py
digit_w = []
digit_h = []

clock_dict = {}

str_spacing = 18 #idk... You're probably going to have to adjust this


#@Isaac, I may have underestimated the calculations - James
#You were right, my head is starting to hurt 🙏 sorry
bounds = ((150, 345), (150, 685), (490, 345), (490, 685)) #top left, bottom left, top right, bottom right
center_of_txt = [0, 0]

center_of_txt[0] = (bounds[2][0] - bounds[0][0]) / 2 #calculating the x position of the center, relative to top left corner
center_of_txt[1] = (bounds[1][1] - bounds[0][1]) / 2 #calculating the y position of the center, relative to top left corner

center_txt = bounds[0] + center_of_txt #the actual center of the text, using the above calculations

center_of_bounds = [0, 0] #to be determined
starting_pos = [0, 0] #tbd, the starting position of the text, relative to the bounds

for digit in clock:
    clock_dict[digit] = []

for digit in clock:
    w, h = fnt.getsize(digit)
    digit_w.append(w)
    digit_h.append(h)

def center_w(char):
    width = fnt.getsize(char)
    width = width / 2
    return width

def align_everything():
    for digit in clock:
        clock_dict[digit] = center_w(digit) #gives me the exact center width of each character in the string
    
    full_width = 0
    for w in digit_w:
        full_width += w #adding the widths of each character
    
    full_width += str_spacing * len(clock) - 1 #adding the string spacing to the full width
    
    ltr_center_height = digit_h[0] / 2 #since it's all numbers, their heights are the same... I think...

    center_height = bounds[3][1] - bounds[0][1] #center height of the bounds, relative to the bounds

    w = bounds[2][0] - bounds[0][0] #width of the outer circle/bounds

    #I will now explain how I will align the text
    #So, in google slides, how does it appear to align images with the center of the slide?
    #Well, the center of the image just needs to be aligned with the center of the slide, no?
    #So all I really have to do, is to get the center, and then 
    #subtract the x position from the center by half of the object you are planning to align
    #And then you have the top-left position of the object, no?
    #MWAHAHAHAHHAHAHA, I HAVE DISCERNED THE *COUGH, COUGH* TEACHINGS OF THE UNIVERSE *MORE VIOLENT COUGHING* - James

    center_of_bounds[0] = w / 2
    center_of_bounds[1] = center_height

    starting_pos[0] = center_of_bounds[0] - full_width / 2
    starting_pos[1] = center_height

    for digit in clock:
        paint.text((starting_pos[0]+clock_dict[digit], starting_pos[1]-ltr_center_height), digit, fill=(255, 255, 255), font=fnt, stroke_width=2, stroke_fill="white")
        starting_pos[0] += clock_dict[digit] * 2 #this brings the x position to the end of the character
        #the above is useful, because now we can add the char_separation
        starting_pos[0] += str_spacing #this brings the x position to the start of the next character/end of the character separation
    
    img.save('assets/temp/temporary.png')
    #await message.channel.send(file=discord.File('assets/temp/temporary.png'))
    import os
    os.remove('assets/temp/temporary.png')