def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) == 1:
        return first
    i = 0
    while i < (len(str_number) - 1):
        i += 1
        a = int(str_number[i])
        if a > 0:
            first = a
        else:
            break

    return first * get_multiplied_digits(int(str_number[1:]))


result = get_multiplied_digits(40203)
print(result)
