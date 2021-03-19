from datetime import date
from datetime import datetime
from datetime import timedelta
import os

# inlocuieste aici cu path-ul la care sa se salveze fisierele
highlight_path = 'G:/Youtuber-mare/Streaming/Highlight-timestamp/'

# data de azi
today = datetime.today()
today_formated = datetime.strftime(today, '%d-%m-%Y')
# sablon pt ora:minut:secunda
FMT = '%H:%M:%S'

curr_hour = datetime.now().hour

# verific daca e trecut de ora 10 cand rulez scriptul, pentru ca altfel
# si daca il rulez la 1 noaptea, mi-ar fi creat un fisier nou, si nu asta vreau
if curr_hour > 10:
    # cand sciptul este apelat pt prima oara, el va creea un fisier cu numele = data la care facem stream-ul
    # in care adaugam ora la care am inceput streamul
    if not os.path.exists(highlight_path + today_formated + '.txt'):
        file = open(highlight_path + today_formated + '.txt', 'a+')
        now = datetime.now()
        file.write(str(now.hour) + ':' + str(now.minute) + ':' + str(now.second) + '\n')
        file.write('\nMomente:\n')
        file.close()

# daca fisierul deja exista (deci suntem live) vrem sa adaugam minutul si secunda din stream la care se afla
# highlight-ul
else:
    file = open(highlight_path + today_formated + '.txt', 'r')
    now = datetime.now()
    string_now = str(now.hour) + ':' + str(now.minute) + ':' + str(now.second)
    contents = file.readlines()
    contents[0] = contents[0].replace('\n', '')
    timestamp = datetime.strptime(string_now, FMT) - datetime.strptime(contents[0], FMT)

    # atunci cand facem stream peste 12 noaptea, ora actuala ar fi mai mica decat cea de inceput si ne-ar da
    # calculele peste cap
    if timestamp.days < 0:
        timestamp = timedelta(days=0, seconds=timestamp.seconds)

    file.close()
    file_a = open(highlight_path + today_formated + '.txt', 'a+')
    file_a.write(str(timestamp) + '\n')
    file_a.close()