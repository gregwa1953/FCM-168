
def check_number(number):
    # print(f'Number to check: {number}')
    if 1 <= number <= 5:
        print("Between 1 and 5, inclusive")
    elif 6 <= number <= 8:
        print("Between 6 and 8, inclusive")
    elif number == 9 or number == 10:
        print("Equal to 9 or 10")
    else:
        print("Not between 1 and 10, inclusive")


for i in range(0, 12):   # get numbers between 0 and 11
    check_number(i)
