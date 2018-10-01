# Thenea Sun
# Oct. 1st
# This project is about creating a code that can calculate the surface area of a rectangle prism.


def print_instruction():
    print("Here I am going to help you with calculating the surface area of a rectangle.")
    print("Please input the length, width and height of the solid.")


def area_of_rectangle(length, width):
    area = length * width
    return area


def main():
    print(area_of_rectangle(2, 5))
# This function works for the calculation.


main()