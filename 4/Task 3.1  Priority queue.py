import copy


def insert(lst, x):
    lst.append(int(x))
    index = len(lst) - 1
    while lst[index] > lst[(index - 1) // 2] and index > 0:
        lst[index], lst[(index - 1) // 2] = lst[(index - 1) // 2], lst[index]
        index = (index - 1) // 2
    return lst


def extract_max(lst):
    if lst:
        print(lst[0])
        lst[0] = copy.copy(lst[-1])
        del lst[-1]
        i = 0
        while 2 * i + 1 <= len(lst) - 1:
            if 2 * i + 2 <= len(lst) - 1:
                if lst[2 * i + 1] > lst[2 * i + 2]:
                    if lst[i] < lst[2 * i + 1]:
                        lst[i], lst[2 * i + 1] = lst[2 * i + 1], lst[i]
                        i = 2 * i + 1
                    else:
                        break
                else:
                    if lst[i] < lst[2 * i + 2]:
                        lst[i], lst[2 * i + 2] = lst[2 * i + 2], lst[i]
                        i = 2 * i + 2
                    else:
                        break
            else:
                if lst[i] < lst[2 * i + 1]:
                    lst[i], lst[2 * i + 1] = lst[2 * i + 1], lst[i]
                break
    return lst


operations_number = int(input())
priority_queue = []
for _i in range(operations_number):
    command = input()
    if ' ' in command:
        priority_queue = insert(priority_queue, command.split()[1])
    else:
        priority_queue = extract_max(priority_queue)
