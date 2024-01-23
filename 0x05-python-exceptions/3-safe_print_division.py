#!/usr/bin/python3
def safe_print_division(a, b):
    Result = 0
    try:
        Result = a / b
    except ZeroDivisionError:
        Result = None
    finally:
        print("Inside result: {}".format(Result))
        return Result
