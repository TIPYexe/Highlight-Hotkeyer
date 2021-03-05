from datetime import date
from datetime import datetime
import os

highlight_path = 'G:/Youtuber mare/Streaming/Highlight-timestamp/'
today = date.today()

if not os.path.exists(highlight_path + str(today) + '.txt'):
    file = open(highlight_path + str(today) + '.txt', 'a+')
    now = datetime.now()
    file.write(str(today) + '\n')
    file.write(str(now.hour) + ':' + str(now.minute) + ':' + str(now.hour) + '\n')
    file.close()