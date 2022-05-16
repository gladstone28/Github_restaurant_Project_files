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


# Write code to insert restaurant data into a data structure (LinkedList of LinkedLists) here. The data is in data.py
def insert_restaurant_data():
    restaurant_data_list = LinkedList()
    for food_type in types:
        restaurant_sublist = LinkedList()
        for restaurant in restaurant_data:
            if restaurant[0] == food_type:
                restaurant_sublist.insert_beginning(restaurant)
        restaurant_data_list.insert_beginning(restaurant_sublist)
    return restaurant_data_list


my_food_list = insert_food_types()
my_restaurant_list = insert_restaurant_data()


selected_food_type = ""







