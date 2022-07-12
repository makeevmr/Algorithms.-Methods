n = int(input())
current_number = 1
numbers_counter = 0
numb_lst = []
while n - current_number >= current_number + 1:
    n -= current_number
    numbers_counter += 1
    numb_lst.append(current_number)
    current_number += 1
numbers_counter += 1
numb_lst.append(n)
print(numbers_counter)
for number in numb_lst:
    print(number, end=' ')
