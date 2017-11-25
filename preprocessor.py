import glob

file_list = glob.glob("img/notes/*.*")
print(len(file_list))
import os
import PIL

size = 128, 128
from PIL import Image

count = 0
for infile in file_list:
    try:
        count += 1
        basewidth = 240
        img = Image.open(infile)
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((basewidth, hsize), Image.ANTIALIAS)
        s = "img/new_notes/" + str(count) + ".jpg"
        print(count)
        img.save(s)
    except:
        print("___-----_____-----_______------_____-----__________------___----___---______-------____--_______---_______")
        continue
