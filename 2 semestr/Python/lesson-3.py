def info_of_number() -> str:
    number: int = int(input())
    if number > 0:
        if number % 2:
            return "Положительное нечетное число"
        else:
            return "Положительное четное число"
    elif number < 0:
        if number % 2:
            return "Отрицательное нечетное число"
        else:
            return "Отрицательное четное число"
    else:
        return "Нулевое число"

def count_the_vowel_letters() -> dict:
    word: str = input()
    #словарь из гласных и их количество в слове
    vowels: dict = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    #гласные
    count_vowels: int = 0
    #согласные
    count_consonant: int = 0
    for i in word:
        if i in vowels:
            count_vowels += 1
            vowels[i] += 1
        else:
            count_consonant +=1
    for key, value in vowels.items():
        if value == 0:
            vowels[key] = False
    return vowels, count_vowels, count_consonant            

def check_invest() -> list:
    # сумма вложения
    max_invest: int = 10
    # деньги Майкла
    cash_michael: int = int(input())
    # деньги Ивана
    cash_ivan: int = int(input())
    if cash_michael >= max_invest and cash_ivan >= max_invest:
        return 2
    else:
        if cash_michael >= max_invest:
            return "Michael"
        elif cash_ivan >= max_invest:
            return "Ivan"
        elif cash_ivan + cash_michael >= max_invest:
            return 1
        else:
            return 0
    
            
# print(info_of_number())
# print(count_the_vowel_letters())
print(check_invest())

      