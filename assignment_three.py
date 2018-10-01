# Thenea Sun
# Oct. 1st
# This project is about creating a code that can calculate the surface area of a rectangle prism.


def print_instruction():
    print("Here I am going to help you with calculating the surface area of a rectangle.")
    print("Please input the length, width and height of the solid.")


def get_length():
    length = input("Please enter length:")
    return float(length)


def get_width():
    width = input("Please enter width:")
    return float(width)


def get_height():
    height = input("Please enter height:")
    return float(height)
# Don't forget to make all of these strings float


def area_of_rectangle(length, width):
    area = length * width
    return area


def total_surface_area(length, width, height):
    front_back = area_of_rectangle(length, width) * 2
    sides = area_of_rectangle(width, height) * 2
    top_bottom = area_of_rectangle(length, height) * 2
    return front_back + sides + top_bottom
# Almost forget to put parameters in there.


def main():
    print(total_surface_area(get_length(), get_width(), get_height()))
# This function works for the calculation.


main()
