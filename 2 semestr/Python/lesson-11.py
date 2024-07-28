def print_list(lst: list, n: int) -> str:
    if n == len(my_list):
        return 'Конец списка'
    print(lst[n])
    return print_list(lst, n + 1)


my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

print(print_list(my_list, 0))
