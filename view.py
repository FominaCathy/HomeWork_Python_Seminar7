# достаем данные из файла 
# нужно ли их возвращать как список для дальнейшей с ними работы в модуль interface?
# дела храняться в файле. (??) имя файла поступает на вход (??)
import logg as log_case


def print_case():
    print("Тест: печатаем список дел") # строка для теста. вместо нее должно быть тело
    data = "list case real. test"
    log_case.add_logg_str("вывод списка дел на экран", "просмотр") #логгируем
    return data