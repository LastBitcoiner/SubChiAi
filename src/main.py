from utils.grab_subtitle import grab_sub as gs
from utils.export import export
import os

vid_link = input('enter video link: ')

gs(vid_link)

path = r'C:\Users\omido\Documents\GitHub\SubChiAI\SubChiAi\src\assets\subs'

files = os.listdir(path)

try:
    for i in files:
        export(i)

    print('all your files is ready in exported folder!')
except:
    print('an error occured')
