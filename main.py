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


def main():
    """ This function gives the user to pick drinks from the list
    Can select as many drink they want. In the end , displays the total Sum of prices"""
    drink_list = Drink.products
    print("Drink-List: ", str(drink_list) + "\n")
    while True:
        Sum = 0
        while True:
            drink_name = get_string_input("Enter the drink you want from the list")
            # while
            if drink_name in drink_list:
                    drink_size = get_string_input("What size do you want? ")
                    # checks if the size entered by the user is in the list
                    if str(drink_size).upper() in {"LARGE", "MEDIUM", "SMALL"}:
                        drink_quantity = get_user_int("enter the quantity")
                        d = Drink(drink_name, drink_size)
                        price = d.calculate_price(drink_quantity)
                        Sum = Sum + price  # Sum for all the drink
                        more_drink = get_string_input("DO you want anything more ? (Y/N)")
                        if str(more_drink).upper() == 'Y':
                            continue
                        elif str(more_drink).upper() == 'N':
                            print("The total for all the drink is", round(Sum, 2))
                            break
                        else:
                            print("Invalid entry")
                            continue
                    else:
                        print(" Only Large/Medium/Small sizes are available !!! ")
                        continue
                    break
            else:
                print("No such drink exists !!! choose from the List")
                continue
        break


main()
