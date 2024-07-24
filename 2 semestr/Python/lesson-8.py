def add_pests():
    pets: dict = dict()
    for _ in range(int(input("Введите количество животных которых нужно добавить: "))):
        name: str = input('Введите имя питомца: ')
        pets[name] = dict()
        pets[name]['Вид питомца'] = input('Вид питомца: ')
        pets[name]['Возраст питомца'] = int(input('Возраст: '))
        pets[name]['Имя владельца'] = input('Имя владельца: ')
    return pets
        
def print_pets():
    pets = add_pests()
    resulst = ''
    for k in pets.keys():
        resulst += f'Это {pets[k]['Вид питомца'].lower()} по кличке "{k.capitalize()}".'
        if pets[k]['Возраст питомца']%10 == 1 and pets[k]['Возраст питомца'] != 11:
            resulst += f' Возраст {pets[k]['Возраст питомца']} год.'
        elif pets[k]['Возраст питомца']%10 in list(range(2, 5)):
            resulst += f' Возраст {pets[k]['Возраст питомца']} годa.'
        elif pets[k]['Возраст питомца']%10 in list(range(5, 10)) or pets[k]['Возраст питомца'] in [0, 10, 11]:
            resulst += f' Возраст питомца: {pets[k]['Возраст питомца']} лет.'
        resulst += f' Имя владельца: {pets[k]['Имя владельца'].capitalize()}\n'
    return resulst

def dict_numbers():
    my_dict: dict = dict()
    for i in range(10, -6, -1):
        my_dict[i] = i**i
    return my_dict

print(print_pets()) # 1 задание
# print(dict_numbers()) # 2 задание


