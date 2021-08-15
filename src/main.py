from utils.grab_subtitle import grab_sub as gs
from pathlib import Path


seleniumPATH = "C:/Users/omido/Documents/GitHub/SubChiAI/SubChiAi/bin/chromedriver.exe"
seleniumDownloadDir = "C:/Users/omido/Documents/SubChiAI/assets/subs"
vid_link = "https://www.youtube.com/watch?v=KItleddMYFU"

gs(vid_link, seleniumPATH, seleniumDownloadDir)
