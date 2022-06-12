# достаем данные из файла 
# нужно ли их возвращать как список для дальнейшей с ними работы в модуль interface?
# дела храняться в файле. (??) имя файла поступает на вход (??)
import logg as log_case


def print_case(data):
   
    with open(data, "r", encoding = 'utf8') as file:
        i = 1
        for line in file:
            print(f"{i} - {line}")
            i += 1
    
    
    log_case.add_logg_str("вывод списка дел на экран", "просмотр") #логгируем
    