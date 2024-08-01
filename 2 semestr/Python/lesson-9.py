from collections import deque


def fact(n) -> int:
    if n == 1 or n == 0:
        return 1
    return fact(n - 1) * n

def list_fact(n) -> list:
    lst: list = list()
    for i in range(n):
        lst.append(fact(n - i))
    return lst

def create(pets: dict) -> dict:
    last = deque(pets, maxlen=1)[0] + 1
    pets[last] = dict()
    name: str = input("Введите имя животного: ")
    pets[last][name] = dict()
    pets[last][name]["Имя вид питомца"] = input("Вид питомца: ")
    pets[last][name]["Возраст питомца"] = int(input("Его возраст: "))
    pets[last][name]["Имя владельца"] = input("Имя владельца: ")
    return pets_list()

def read(pets: dict) -> str:
    id_pets: str = int(input("Для вывода информации, введите ID питомца: "))
    if get_pet(id_pets):
        for n in pets[id_pets].items():
            return f'Это {deque(n[1].values())[0]} по кличке "{n[0]}". Возраст питомца: {deque(n[1].values())[1]} {get_suffix(deque(n[1].values())[1])}. Имя владельца: {deque(n[1].values())[2]}'
    return 'Такого ID нет в базе'

def update(pets: dict) -> dict:
    pets_list()
    id_pets: str = int(input("Для изменения информации, введите ID питомца: "))
    if get_pet(id_pets):
        for i in pets[id_pets].items():
            print(i)
        request: str = int(input(
            "Что вы хотите изменить?\n1 - Имя питомца\n2 - Вид питомца\n3 - Его возраст\n4 - Имя владельца\n"
        ))
        if request == 1:
            pets[id_pets][input("Введите новое имя для питомца: ")] = pets[id_pets].get(
                deque(pets[id_pets].keys())[0]
            )
            del pets[id_pets][deque(pets[2])[0]]
            return pets
        elif request == 2:
            for i in pets[id_pets].values():
                i["Вид питомца"] = input("Введите новый вид: ")
                return pets
        elif request == 3:
            for i in pets[id_pets].values():
                i["Возраст питомца"] = int(input("Введите новый возраст: "))
                return pets
        elif request == 4:
            for i in pets[id_pets].values():
                i["Имя владельца"] = input("Введите новое имя владельца: ")
                return pets
        return "не верная команда"
    return 'Такого ID нет в базе'

def delte(pets: dict) -> dict: 
    pets_list()
    id_pets: str = int(input("Для удаления информации, введите ID питомца: "))
    if get_pet(id_pets):
        del pets[id_pets]
        return pets
    return 'Такого ID нет в базе'

def get_pet(ID) -> dict:
    return pets[ID] if ID in pets.keys() else False

def get_suffix(age) -> str:
    if age == 1 or age % 10 == 1 and age != 11:
        return "год"
    elif age in [2, 3, 4] or age % 10 in [2, 3, 4]:
        return "года"
    elif age in [5, 6, 7, 8, 9, 10, 11] or age % 10 in [5, 6, 7, 8, 9]:
        return "лет"

def pets_list() -> str:
    for k, v in pets.items():
        for k1, v2 in v.items():
            print(f'ID: {k} - Имя {k1}:')
            for value, key in v2.items():
                print(f'\t{value} - {key}')

def controller():
    command = str()
    while True:
        command = input("Введите команду:\n- create\n- read\n- update\n- delete\n- stop\n")
        if command == 'stop':
            break
        elif command == 'create':
            create(pets)
            continue
        elif command == 'read':
            print(read(pets))
            continue
        elif command == 'update':
            update(pets)
            continue
        elif command == 'delete':
            delte(pets)
            continue
        else:
            print('Нет такой команды ')
            continue

# print(list_fact(fact(3))) # задание 1

pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел",
        },
    },
    2: {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша",
        },
    },
    3: {
        "Кеша": {
            "Вид питомца": "попугай",
            "Возраст питомца": 9,
            "Имя владельца": "Маша",
        },
    },
}

controller() # задание 2
