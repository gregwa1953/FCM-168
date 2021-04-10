

def check_number(number):
    match number:
        case 1 | 2 | 3 | 4 | 5:
            print(f"{number} is between 1 and 5, inclusive")
        case 6 | 7 | 8:
            print(f"{number} is between 6 and 8, inclusive")
        case 9 | 10:
            print(f"{number} is equal to 9 or 10")
        case _:
            print(f"{number} Not between 1 and 10, inclusive")


for i in range(0, 12):   # get numbers between 0 and 11
    check_number(i)
