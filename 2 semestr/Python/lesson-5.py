def palindrom() -> str:
    string: str = input()
    if string == string[::-1]:
        return "yes"
    else:
        return "no"
    
def change_str() -> str:
    string: str = input()
    count: int = 0
    result: str = ''
    for i in string:
        if i == ' ':
            count += 1    
            if count > 1:
                continue
            result += i    
        else:
            result += i
            count = 0
    return result
    
# print(palindrom())
print(change_str())