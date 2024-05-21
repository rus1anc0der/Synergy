def count_number() -> int:
    number: int = int(input())
    count: int = 0
    for _ in range(number):
        input_number: int = int(input())
        if input_number == 0:
            count += 1
    return count

def count_div() -> int:
    number: int = int(input())
    count: int = 0
    for i in range(1, number+1):
        if number % i == 0:
            count += 1
            print(i)        
    return count

def even_number() -> str:
    number1: int = int(input())
    number2: int = int(input())
    if number1 % 2 != 0:
        number1 += 1
    elif number1 == 0:
        number1 += 2
    for i in range(number1, number2+1, 2):
        print(i, end=' ')

        
# print(count_number())
# print(count_div())
even_number()