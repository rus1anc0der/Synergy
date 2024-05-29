def unique_numbers() -> int:
    len_list: int = int(input())
    set_number: set = set()
    if 1 <= len_list <= 100000:
        for _ in range(len_list):
            number: int = int(input())
            if number <= 2*pow(10,9):
                set_number.add(number)
            else:
                return "the number must not be greater than 2*10^9"
        return len(set_number)
    else:
        return "the quantity must not be less than 1 and not more than 100000"
    
def unique_list() -> int:
    lst1: list = []
    lst2: list = []  
    len_list: int = int(input())
    if len_list < 100000:
        for _ in range(len_list):
            lst1.append(int(input())) # вводим числа по очереди в каждый список
            lst2.append(int(input()))
        return len(set(lst1) & set(lst2))  # так же можно использовать метод intersection()
    else:
        return 'the number must not be greater than 100000'
    
def checking_strings() -> str:
    lst: list = list(map(int, input().split()))
    result: set = set()
    for i in lst:
        if i in result:
            print(i, 'YES')
        else:
            print(i, 'NO')
        result.add(i)
        
    
# print(unique_numbers())
# print(unique_list())
checking_strings()

