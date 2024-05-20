def rectangle_properties():
    length = float(input())
    height = float(input())
    return f"S = {length*height}\nP = {(length+height)*2}"

def  operations_on_a_number():
    number = int(input())
    unit = number % 10
    tens = number % 100 // 10
    hundreds = number % 1000 // 100
    thousands = number % 10000 // 1000
    tens_of_thousands = number // 10000
    return tens**unit * hundreds / (tens_of_thousands - thousands)


# print(rectangle_properties())

print(operations_on_a_number())
