from data import *
from welcome import *
from linkedlist import LinkedList

print_welcome()


# Write code to insert food types into a data structure (LinkedList) here. The data is in data.py
def insert_food_types():
    food_type_list = LinkedList()
    for food_type in types:
        food_type_list.insert_beginning(food_type)
    return food_type_list






