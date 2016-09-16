""" This class displays the interface"""

from drink import Drink


def get_user_int(message):
    """Return an integer from the user
    """
    while True:
        user_input = input('{}: '.format(message))
        try:
            number = int(user_input)
        except ValueError:
            print('You must enter a whole number.')
            continue
        return number


def get_string_input(message):
    while True:
        user_input = input(('{}'.format(message)))

        if user_input:
            return user_input

        else:
            print("You must enter something")


def main():
    drink_list = Drink.products
    print("Drink-List: ", str(drink_list) + "\n")
    while True:
        drink_name = get_string_input("Enter the drink you want from the list")
        if drink_name in drink_list:
            while True:
                    drink_size = get_string_input("What size do you want? ")
                    if str(drink_size).upper() in {"LARGE", "MEDIUM", "SMALL"}:
                        drink_quantity = get_user_int("enter the quantity")
                        d = Drink(drink_name, drink_size)
                        price = d.calculate_price(drink_quantity)
                        print(" The total price for the drink ->", drink_name + " is " + str(price))
                        break
                    else:
                        print(" Only Large/Medium/Small sizes are available !!! ")
                        continue
            break
        else:
            print("No such drink exists !!! choose from the List")
            continue

main()
