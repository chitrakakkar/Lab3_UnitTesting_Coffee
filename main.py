""" This class displays the interface"""

from drink import Drink


def get_user_int(message):
    """Return an integer from the user
    """
    while True:
        user_input = input('{}: '.format(message))
        try:
            number = int(user_input)
            if number <= 0:
                print("Enter a positive or greater than 0")
                continue
        except ValueError:
            print('You must enter a whole number.')
            continue
        return number


def get_string_input(message):
    """ Returns a string input !!! error msg if None"""
    while True:
        user_input = input(('{}'.format(message)))

        if user_input:
            return user_input

        else:
            print("You must enter something")


def get_drink():
        drink_list = Drink.products
        while True:
            print("Drink-List: ", str(drink_list) + "\n")
            drink = get_string_input("Enter the drink you want from the list").lower()
            if drink in drink_list:
                return drink
            else:
                print("I'm sorry, we do not serve that here")


def get_size():
    drink_sizes = Drink.get_sizes()
    while True:
        drink_size = input("What size do you want?").upper()
        if drink_size in drink_sizes:
            return drink_size

        else:
            print("Only Large/Medium/Small sizes are available")


def main():
    """ This function gives the user to pick drinks from the list
    Can select as many drink they want. In the end , displays the total Sum of prices"""
    sum_of_drinks = 0

    while True:
        drink_name = get_drink()
        drink_size = get_size()
        # checks that the quantity is an integer
        drink_quantity = get_user_int("enter the quantity")
        d = Drink(drink_name, drink_size)
        price = d.calculate_price(drink_quantity)
        # calculates sum of all drinks
        sum_of_drinks += price
        more_drink = get_string_input("DO you want anything more ? (Y/N)")
        if str(more_drink).upper() == 'Y':
            continue

        elif str(more_drink).upper() == 'N':
            print("The total for all of the drinks is $", round(sum_of_drinks, 2))
            break

        else:
            print("Invalid entry")


if __name__ == '__main__':
    main()
