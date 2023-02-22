#!/usr/bin/env python3

"""Trying to change global variables"""

TN = ""


def some_funct():
    """testing if we can change variable in function"""
    #   TN here is local to the function, masks the global one.
    TN = ""
    print(TN)  # prints empty line egain, local TN masks global
    TN = "77"

    return TN


def other_funct():
    """testing if we can change variable in function"""
    global TN  # indicates that we will be using external variable
    TN = ""
    print(TN)  # prints empty line again, local TN masks global
    TN = "88"
    return TN


def main():
    TN = ""
    print(TN)  # prints empty line

    TN = "66"

    print(TN)  # prints value 66

    some_funct()
    print("jeden")

    print(some_funct())

    print("dwa")

    print(TN)  # depends on how some_funct is defined
    print("trzy")
    other_funct()
    print("cztery")
    print(other_funct())
    print("piec")

    print(TN)


main()
