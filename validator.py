""" This class checks all the validation
for all input done """


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


def is_whole_number(number, valid_range=None):
    try:
        number_as_int = int(number)
        if number_as_int in valid_range:
            return True

        # if parsing as integer does not produce an error, check if it's in range if a range has been given
        if valid_range and number_as_int in valid_range:
            return True
        else:
            return False
    except ValueError:
        # also return False if an integer is not passed
        return False
