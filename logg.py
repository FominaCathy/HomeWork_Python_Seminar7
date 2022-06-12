# добавляет в файл logg.txt строку с данныим об операции
# строка которую нужно добавить поступает на вход
from datetime import datetime as data_time


def add_logg_str(data, operation):
    time = data_time.now()
    with open("logg.txt", "a", encoding = 'utf8') as file:
        file.write(f"{data}; {operation}; {time} \n")
    return