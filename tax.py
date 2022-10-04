#!/usr/bin/env python3

# Created By: Tamer Zreg
# Date: Oct. 3, 2022
# This program adds the Albertan sales tax to orders.

# Imports Alberta's 5% GST
import constants


def main():
    # Gets the user's subtotal
    subtotal = float(input("Enter the subtotal of your item(s): $"))
    print("")
    # Calculates the tax and total of the order
    tax = subtotal * constants.GST
    total = subtotal + tax
    # Prints the tax cost and the sales tax.
    print(
        "${0:.2f} was added to the total due to the {1:.2f}% Albertan sales tax.".format(
            tax, constants.GST * 100
        )
    )
    # Prints the total cost of the order
    print("The total cost of your order is ${0:.2f}".format(total))


if "__main__" == __name__:
    main()
