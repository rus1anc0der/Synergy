def info_for_clinic():
    type_of_animal = input("input name: ")
    age_animal = input('age: ')
    name_animal = input('name: ')
    return f"Это {type_of_animal} по кличке {name_animal}. Возраст: {age_animal} года"
    
def test_for_biology():
       human_development = [input(i) for i in range(1, 10)]
       return human_development
   
   
# print(info_for_clinic())
answer = test_for_biology()
# сделал так что бы показать как работает команда sep
print(answer[0], answer[1],answer[2], answer[3],answer[4], answer[5],answer[6], answer[7], sep='=>')



