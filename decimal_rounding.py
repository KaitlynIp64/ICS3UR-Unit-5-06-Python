#!/usr/bin/env python3

# Created by: Kaitlyn Ip
# Created on: Jan 2023
# This program rounds decimals


def rounding(decimal, decimal_place):
    # This function rounds the decimals

    # Process
    rounded = decimal * (10**decimal_place) + 0.5
    rounded = int(rounded)
    rounded = rounded / (10**decimal_place)

    return rounded


def main():
    # This function gets user's input and shows rounded input
    rounding_num = []

    # Process
    user_decimal = input("Enter a decimal: ")
    try:
        user_decimal = float(user_decimal)
        user_decimal_place = input("Enter desired decimal places to round to: ")
        try:
            user_decimal_place = int(user_decimal_place)
            rounding_num.append(user_decimal)
            rounded_num = rounding(user_decimal, user_decimal_place)
            print("")
            print("Rounded number: ", rounded_num)
        except ValueError:
            print("That is not a valid input.")
    except ValueError:
        print("That is not a valid input.")

    print("\nDone.")


if __name__ == "__main__":
    main()
