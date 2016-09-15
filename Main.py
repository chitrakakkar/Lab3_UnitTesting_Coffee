from Drinks import drink


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
    drink_list = {'Coffee', 'Mocha', 'Tea', 'Cappuccino', 'Espresso'}
    print("Drink-List: ", str(drink_list) + "\n")
    drink_name = get_string_input("Enter the drink you want from the list")
    drink_size = get_string_input("What size do you want? ")
    drink_quantity = get_user_int("enter the quantity")
    price = drink.calculate_price(" ", drink_name, drink_size, drink_quantity)
    print(" The total price for the drink ->", drink_name + " is " + str(price))


main()
