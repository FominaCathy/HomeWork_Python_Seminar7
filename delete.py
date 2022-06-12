# удаляет строку из списка дел
#
#выводит на экран все дела и предлагает выбрать строку для удаления

#
import view as view_case
import logg as log_case
import add as add_case

def delete_str(data, task_del):

    with open(data, "r", encoding = 'utf8') as file:
        temp_list = []
        i = 1
        for line in file:
            if i != task_del: 
                temp_list.append(line)
                
            else:
                log_case.add_logg_str(line[:len(line)-2], "удаление") #логгируем
            i += 1


        
        with open(data, "w", encoding = 'utf8') as file:
            for tsk in temp_list:
                file.write(tsk)


    view_case.print_case(data)
    
    
    
    