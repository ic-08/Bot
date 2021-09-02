elif message.content.startswith('$ttt'): 
        import os
        from PIL import Image, ImageDraw, ImageFont
        import pytz
        #Open the background
        pics = os.listdir('assets/backgrounds')
        picture = random.choice(pics)
        im = Image.open(f'assets/backgrounds/{picture}')


        ######## Day of the week ########
        time_list = str(datetime.now(pytz.timezone('US/Eastern')))
        print(time_list)
        time_list = list(time_list)
        ftime = ''
        print(time_list)
        x = datetime.now(pytz.timezone('US/Eastern')).weekday()
        day_of_the_week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        print(day_of_the_week[x])

        # Edit the picture for day of week
        d = ImageDraw.Draw(im) 
        fnt1 = ImageFont.truetype(f'assets/arial.ttf', 40)
        width = fnt1.getsize(day_of_the_week[x])[0]
        d.text((315 - round(width/2),400), day_of_the_week[x], fill=(255, 255, 255), font=fnt1) 

        #Line
        second_image = Image.open("assets/backgrounds/line.png") 
        newsize = (width, 5)
        second_image = second_image.resize(newsize)
        im.paste(second_image, (315 - round(width/2),450))



        ######## MONTH AND DATE ########
        # Order = August 26th, 2021

        #Find the month
        fnt2 = ImageFont.truetype(f'assets/arial.ttf', 30)
        months = ['January ', 'Feburary ', 'March ', 'April ', 'May ', 'June ', 'July ', 'August ', 'September ', 'October ', 'November ', 'December ']
        dt = datetime.now(pytz.timezone('US/Eastern'))
        full_date = str(months[dt.month -1]) + str(dt.day) + ','
        width = fnt2.getsize(full_date)[0]
        print(width)

        #Edit the picture for the corresponding month
        fnt2 = ImageFont.truetype(f'assets/arial.ttf', 35)
        d.text((315 - round(width/2),580), full_date, fill=(255, 255, 255), font=fnt2) 
        d.text((285,625), str(dt.year), fill=(255, 255, 255), font=fnt2, stroke_width=1, stroke_fill="white") 
        
        
        ######## TIME ########
        for i in range(5):
            ftime += str(time_list[i+11])
        ftime = list(ftime)
        fnt = ImageFont.truetype(f'assets/arial.ttf', 82)

        # Positioning of Time Text
        width, height = im.size 
        wtime = []
        for i in range(5):
            width = fnt.getsize(ftime[i])[0]
            wtime.append(width)
        print(wtime)
        x = 305
        y = 475

        #Distance between characters is exactly 26 pixels
        d.text((round(x-(wtime[1]/2 + wtime[2]/2+26)) - round(wtime[0]/2 + wtime[1]/2 + 26),y), ftime[0], fill=(255, 255, 255), font=fnt, stroke_width=2,
          stroke_fill="white") 
        d.text((round(x-(wtime[1]/2 + wtime[2]/2+26)),y), ftime[1], fill=(255, 255, 255), font=fnt, stroke_width=2,
          stroke_fill="white") 
        d.text((x,y), ftime[2], fill=(255, 255, 255), font=fnt, stroke_width=2,
          stroke_fill="white") 
        d.text((round(x+(wtime[3]/2 + wtime[2]/2+5)),y), ftime[3], fill=(255, 255, 255), font=fnt, stroke_width=2,
          stroke_fill="white") 
        d.text((round(x+(wtime[3]/2 + wtime[2]/2+5)) + round(wtime[3]/2 + wtime[4]/2 + 26),y), ftime[4], fill=(255, 255, 255), font=fnt, stroke_width=2,
          stroke_fill="white") 


        #Save the edited image
        im.save(f'assets/backgrounds/temp.png')
        await message.channel.send(file=discord.File(f'assets/backgrounds/temp.png'))
        import os
        os.remove(f'assets/backgrounds/temp.png')
