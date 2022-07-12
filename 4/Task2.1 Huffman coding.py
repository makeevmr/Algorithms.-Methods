def letter_counter(str_to_code):  # counting numbers of different letters and returning dictionary with values
    frequency_dict = {}
    for character in str_to_code:
        if character in frequency_dict:
            frequency_dict[character] += 1
        else:
            frequency_dict[character] = 1
    return frequency_dict


def code_builder(branch, current_code=''):
    if type(branch[0]) == str and type(branch[1]) == str:
        codes_dict[branch[0]] = current_code + '0'
        codes_dict[branch[1]] = current_code + '1'
    elif type(branch[0]) == str:
        codes_dict[branch[0]] = current_code + '0'
        return code_builder(branch[1], current_code + '1')
    elif type(branch[1]) == str:
        codes_dict[branch[1]] = current_code + '1'
        return code_builder(branch[0], current_code + '0')
    else:
        return code_builder(branch[0], current_code + '0'), code_builder(branch[1], current_code + '1')


codes_dict = {}
str_encode = input()
counted_dict = letter_counter(str_encode)
priority_queue = []
for letter in counted_dict:
    priority_queue.append((letter, counted_dict[letter]))
for _i in range(len(priority_queue) - 1):
    min_priority1 = min(priority_queue, key=lambda x: x[1])
    priority_queue.remove(min_priority1)
    min_priority2 = min(priority_queue, key=lambda x: x[1])
    priority_queue.remove(min_priority2)
    priority_queue.append(((min_priority1[0], min_priority2[0]), min_priority1[1] + min_priority2[1]))
priority_queue = priority_queue[0][0]
if type(priority_queue) == str:
    print(1, counted_dict[priority_queue])
    print(priority_queue + ': 0')
    print('0' * counted_dict[priority_queue])
else:
    code_builder(priority_queue)
    for letter in counted_dict:
        str_encode = str_encode.replace(letter, codes_dict[letter], counted_dict[letter])
    print(len(counted_dict), len(str_encode))
    for letter in codes_dict:
        print(letter + ': ' + codes_dict[letter])
    print(str_encode)
