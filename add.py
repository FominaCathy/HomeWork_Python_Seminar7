# добавляет в список дел новую строку
# 
import logg as log_case

def add_str(data):

    print(f"Тест: добавили задачу: {data}") # строка для теста. вместо нее должно быть тело

    log_case.add_logg_str(f"добавили задачу: {data}", "добавление") #логгируем
    return