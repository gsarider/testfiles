#!/usr/bin/env python3

"""Trying to change global variables"""

TN = 1


def some_funct():
    """testing if we can change variable in function"""
    #   TN here is local to the function, masks the global one.
    TN = ""
    print(TN)  # prints empty line egain, local TN masks global
    TN = 77

    return TN


def other_funct():
    """testing if we can change variable in function"""
    global TN  # indicates that we will be using external variable
    print(
        "inside other funct, TN is empty", TN
    )  # prints empty line again, local TN masks global
    TN = 88
    return TN


# def main():
#    TN = ""
#    print('this shoudl be empty', TN)  # prints empty line
#    TN =66
#    print('this should be 66', TN)  # prints value 66
#    some_funct()
#    print("jeden")
#    print('this shoudl be 77, return from some_f', some_funct())
#    print("dwa")
#    print('this should be back to 66', TN)
#    print("trzy")
#    other_funct()
#    print('TN should be already assigned by other funct', TN)
#    print("cztery")
#    print('this is return value from other_f', other_funct())
#    print("piec")
#    print(TN)
#    TN = other_funct()
#    print(TN)


# main()
print(TN)
some_funct()
print(some_funct())
print(TN)
other_funct()
print("Value of TN is", TN)
