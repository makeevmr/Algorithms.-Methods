def calculate_up(x):
    for i in range(2, x + 1):
        numbers_lst.append(i)
        division_by_2 = calculated_numbers_lst[i // 2 - 1]
        division_by_3 = calculated_numbers_lst[i // 3 - 1]
        minus_1 = calculated_numbers_lst[i - 2]
        if i % 2 == 0 and i % 3 == 0:
            calculated_numbers_lst.append(min(minus_1, division_by_2, division_by_3) + 1)
            if minus_1 < division_by_3 and minus_1 < division_by_2:
                previous_number_lst.append(i - 2)
            elif division_by_2 <= minus_1 and division_by_2 <= division_by_3:
                previous_number_lst.append(i // 2 - 1)
            else:
                previous_number_lst.append(i // 3 - 1)
        elif i % 2 == 0:
            calculated_numbers_lst.append(min(minus_1, division_by_2) + 1)
            if minus_1 < division_by_2:
                previous_number_lst.append(i - 2)
            else:
                previous_number_lst.append(i // 2 - 1)
        elif i % 3 == 0:
            if minus_1 < division_by_3:
                previous_number_lst.append(i - 2)
            else:
                previous_number_lst.append(i // 3 - 1)
            calculated_numbers_lst.append(min(minus_1, division_by_3) + 1)
        else:
            calculated_numbers_lst.append(minus_1 + 1)
            previous_number_lst.append(i - 2)
    return calculated_numbers_lst[x - 1]


n = int(input())
calculated_numbers_lst = [0]
numbers_lst = [1]
previous_number_lst = ['-']
print(calculate_up(n))
number_sequence_lst = [n]
n = n - 1
while previous_number_lst[n] != '-':
    number_sequence_lst.append(numbers_lst[previous_number_lst[n]])
    n = previous_number_lst[n]
for number in number_sequence_lst[::-1]:
    print(number, end = ' ')
