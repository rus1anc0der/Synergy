def reverse_list() -> list:
    n: int = int(input())
    result: list = []
    for _ in range(n):
        input_n: int = int(input())
        if 1 <= input_n <= 10000:
            result.append(input_n)
        else:
            return "out of range"
    result.reverse()
    return result

def modified_list(lst: list) -> list:
    result: list = lst.copy()
    for i in range(len(lst)):
        result[i] = lst[i-1]
    return result

def counting_boats() -> int:
    result: int = 0
    max_weight_boat: int = int(input('Максимальная масса которую может выдержать одна лодка: '))
    if 1 <= max_weight_boat <= 100000:
        fishermen: int = int(input("Количество рыбаков: "))
        if 1 <= fishermen <= 100:
            weight_men: list = sorted([int(input("Вес рыбака: ")) for _ in range(fishermen)])
            for i in weight_men:
                if 1 > i > max_weight_boat:
                    return f"the weight of the traveler cannot exceed the weight of the boat"
            if len(weight_men) != fishermen:
                return f'There are only {fishermen} fishermen'
            if len(weight_men)%2:
                for i in range(0, len(weight_men)//2+1):
                    if weight_men[i] + weight_men[-1-i] <= max_weight_boat or weight_men[i] <= max_weight_boat:  
                        result += 1
            else:
                for i in range(0, len(weight_men)//2):
                    if weight_men[i] + weight_men[-1-i] <= max_weight_boat or weight_men[i] <= max_weight_boat:  
                        result += 1
            return result
        else:
            return f'there should be more than 1 fishermen but less than 100'
    else:
        return f"The mass must be greater than 1 but less than 100,000"

                
# task1
# print(reverse_list())

# task2
# input_num1: int = int(input())
# if 1 <= input_num1 <= 100000:
#     result: list = list(map(int, input().split()))
#     if input_num1 == len(result):
#         print(modified_list(result))
#     else:
#         print("out of range")
# else:
#     print("out of range")
    
# task3
print(counting_boats())



            