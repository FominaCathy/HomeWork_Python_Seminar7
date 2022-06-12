import add as add_case
import delete as del_case
import logg as logg_case
import view as view_case


def print_list_case(): # печать списка дел
    print(view_case.print_case())

def delete_unit_case():
    del_case.delete_str() 

def add_unit_case(data):
    add_case.add_str(data)