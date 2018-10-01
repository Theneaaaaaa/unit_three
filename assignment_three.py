# Thenea Sun
# Oct. 1st
# This project is about creating a code that can calculate the surface area of a rectangle prism.


def print_instruction():
    """
    This function gives the instruction of how to use this program
    :return:none
    """
    print("Here I am going to help you with calculating the surface area of a rectangle.")
    print("Please input the length, width and height of the solid.")


def get_length():
    """
    This function gets the input of the length from the user
    :return: length
    """
    length = input("Please enter length:")
    return float(length)


def get_width():
    """
    This function gets the input of the width from the user
    :return: width
    """
    width = input("Please enter width:")
    return float(width)


def get_height():
    """
    This function gets the input of the height from the user
    :return: height
    """
    height = input("Please enter height:")
    return float(height)
# Don't forget to make all of these strings float


def area_of_rectangle(length, width):
    """
    This function calculates one of the surfaces areas of the rectangle.
    :param length: length of the rectangle
    :param width: width of the rectangle
    :return: area
    """
    area = length * width
    return area


def total_surface_area(length, width, height):
    """
    This function calculates the total surface area of the rectangle.
    :param length: length of the rectangle
    :param width: width of the rectangle
    :param height: height of the rectangle
    :return:total surface area
    """
    front_back = area_of_rectangle(length, width) * 2
    sides = area_of_rectangle(width, height) * 2
    top_bottom = area_of_rectangle(length, height) * 2
    return front_back + sides + top_bottom
# Almost forget to put parameters in there.


def main():
    print("The total surface area is:", total_surface_area(get_length(), get_width(), get_height()))
# This function works for the calculation.


main()
