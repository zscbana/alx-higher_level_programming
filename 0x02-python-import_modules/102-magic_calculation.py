def magic_calculation(a, b):
    add = None
    sub = None
    c = 0

    if a < b:
        from magic_calculation_102 import add, sub
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
    else:
        from magic_calculation_102 import sub
        c = sub(a, b)
    return c
