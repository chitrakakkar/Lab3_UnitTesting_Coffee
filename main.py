""" This class displays the interface"""

from drink import Drink
from food import Food
from validator import *


def show_menu():
    """ displays the menu for the user
    checks if user has chosen the right choice from the list
    and calls methods to complete the action"""
    menu = ('\t1) choose a drink\n'
            '\t2) buy a snack\n'
            '\t3) Both'
            '\t4) Quit \n'
            '\nWhat do you want ??? : ')

    menu_choice = int(input(menu))
    while not is_whole_number(menu_choice, range(1, 5)):
        menu_choice = int(input("Invalid entry, please select from the list !!!"))
    if menu_choice == 1:
            call_drink()
    elif menu_choice == 2:
            call_snack()
    elif menu_choice == 3:
        drink_and_snack()
    elif menu_choice == 4:
       exit(4)


def call_drink():
    """ gets the drink-price and add it to the sum for all the drinks chosen
    """
    sum_of_drinks = 0
    while True:
        drink_price = calculate_drink_price()
        sum_of_drinks += drink_price
        more_drink = get_string1_input(input("DO you want anything more ? (Y/N)"))
        if str(more_drink).upper() == 'Y':
            continue
        elif str(more_drink).upper() == 'N':
            print('\033[1m' + "The total-price for the drink is $" + '\033[0m', round(sum_of_drinks, 2))
            #break
            show_menu()

        else:
            print("Invalid entry")


def call_snack():
    """ gets the snack-price and add it to the sum for all snacks chosen"""
    sum_of_snack = 0
    while True:
        snack_price = calculate_snack_price()
        sum_of_snack += snack_price
        more_snack = get_string1_input(input("DO you want anything more ? (Y/N)"))
        if str(more_snack).upper() == 'Y':
            continue
        elif str(more_snack).upper() == 'N':
            print('\033[1m' + "The total-price for the snacks is $" + '\033[0m', round(sum_of_snack, 2))
            #break
            show_menu()

        else:
            print("Invalid entry")


def drink_and_snack():
    """ calculate both drink and snacks list once"""
    while True:
        sum_of_items = 0
        drink_price = calculate_drink_price()
        sum_of_items += drink_price
        more_options = input("DO you want anything more ? (Y/N)")
        if get_string1_input(str(more_options).upper()) == 'Y':
            snack_price = calculate_snack_price()
            sum_of_items = sum_of_items + drink_price + snack_price
            print('\033[1m' + "The total-price for the snacks is $" + '\033[0m', round(sum_of_items, 2))
            #break
            show_menu()
        else:
            print('\033[1m' + "The total-price for the snacks is $" + '\033[0m', round(sum_of_items, 2))
            # break
            show_menu()


def get_drink():
        """ takes input from the user and return if in list
        else displays an error message"""
        drink_list = Drink.products
        while True:
            print('\033[1m' + '\033[4m' + "Drink-List: " + '\033[0m', str(drink_list))
            drink = get_string1_input(input('\033[1m' + "Enter the drink you want from the list"+ '\033[0m'))
            if drink in drink_list:
                return drink
            else:
                print('\033[91m'+ '\033[1m' + "I'm sorry, we do not serve that here"+ '\033[0m')


def get_size():
    """ takes input from the user and returns the size if in the expected list
    else error message"""
    drink_sizes = Drink.get_sizes()
    while True:
        drink_size = input("What size do you want?").upper()
        if drink_size in drink_sizes:
            return drink_size

        else:
            print("Only Large/Medium/Small sizes are available")


def get_snack():
    """ gets  user input for snack selection
    if not , error message"""
    snack_list = Food.products
    while True:
        print('\033[1m' + '\033[4m' + "Snacks-List: " + '\033[0m', str(snack_list))
        snack = input('\033[1m' + "Enter the snack you want from the list"+ '\033[0m')
        if get_string1_input(snack) in snack_list:
            return snack
        else:
            print('\033[91m' + '\033[1m' + "I'm sorry, we do not serve that here" + '\033[0m')


def calculate_drink_price():
    """" gets user input for drink object and calculate the price """
    drink_name = get_drink()
    drink_size = get_size()
    # checks that the quantity is an integer
    drink_quantity = get_user_int("enter the quantity")
    d = Drink(drink_name, drink_size)
    drink_price = d.calculate_price(drink_quantity)
    return drink_price


def calculate_snack_price():
    """ gets user input for snack object and calculate the price"""
    snack_name = get_snack()
    # checks that the quantity is an integer
    snack_quantity = get_user_int("enter the quantity")
    s = Food(snack_name)
    price = s.calculate_food_price(snack_quantity)
    return price


def main():

    """ This function gives the user to pick drinks from the list
    Can select as many drink they want. In the end , displays the total Sum of prices"""
    print('\033[1m' + '\033[94m' + "Welcome to the break-time " + '\033[0m')
    print("***************************")
    print("Menu : ")
    show_menu()


if __name__ == '__main__':
    main()

