def input_str(input_string):
    floor_at_end = 0
    for i in input_string:
        if i == '(':
            floor_at_end += 1
        elif i == ')':
            floor_at_end -= 1
    print('At the end, you will be at floor number:', floor_at_end)

input_str(input('Enter Brackets: '))