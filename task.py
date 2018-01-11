# Шахов Кирилл
# 2 курс ИВТ 
# задание - 
""" считать данных из файла JSON, распарсить (разпознать их) и напечатать 
несколько значений полей в соответствующем формате"""

import pprint
import json
filename = 'data.json'
try:
    with open(filename, encoding='utf-8') as data_file:        
        data = json.loads(data_file.read())
except OSError: # ошибка, связанная с системой.
    print("error 404. Или вы неправильно ввели имя")
pprint.pprint(data)
