import add as add_case
import delete as del_case
import logg as logg_case
import view as view_case


def print_list_case(data): # печать списка дел
    print("Cписок текущих дел:") # строка для теста. вместо нее должно быть тело
    view_case.print_case(data)

def delete_unit_case(data):
    print_list_case(data)
    task_del = int(input("какое дело будем удалаять? укажите его номер: "))
    del_case.delete_str(data, task_del) 
    print("теперь список дел такой:")
    print_list_case(data)

def add_unit_case(): 
    data = input("введите задачу: ")
    add_case.add_str(data, "task_log.txt")

def begin_work():

    list_operation = ['печать списка дел', 'добавление дела в список', 'удаление дела']

    for i, list_operation in enumerate(list_operation, 1):
        print(i, list_operation)

    task = int(input("Укажите номер операции: "))

    if task == 1:
        print_list_case("task_log.txt")
    elif task == 2:
        add_unit_case()
    elif task == 3:
        delete_unit_case("task_log.txt")
    