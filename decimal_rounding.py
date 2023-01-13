#!/usr/bin/env python3

# Created by: Kaitlyn Ip
# Created on: Jan 2023
# This program rounds decimals


import math


def decimal_converter(decimal, decimal_places):
    # rounds a number
    decimal[0] = decimal[0] * pow(10, decimal_places) + 0.5
    decimal[0] = int(decimal[0])
    decimal[0] = decimal[0] / pow(10, decimal_places)


def main():
    # takes user input, passes it to functions and calls them
    decimal = []

    str_temp_decimal = input("Enter a decimal: ")
    str_decimal_places = input("Enter desired decimal places you want to round to: ")

    try:
        temp_decimal = float(str_temp_decimal)
        decimal.append(temp_decimal)
        decimal_places = int(str_decimal_places)

        decimal_converter(decimal, decimal_places)

        print("Rounded number: {0}".format(decimal[0]))
    except ValueError:
        print("That is not a valid input.")

    print("\nDone.")


if __name__ == "__main__":
    main()
