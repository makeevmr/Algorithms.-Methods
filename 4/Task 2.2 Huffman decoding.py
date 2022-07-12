k, l = map(int, input().split())
decode_dict = {}
for _i in range(k):
    code = input()
    lst_split = code.split(': ')
    decode_dict[lst_split[1]] = lst_split[0]
str_to_decode = input()
current_symbol = ''
str_decoded = ''
for digit in str_to_decode:
    current_symbol += digit
    if current_symbol in decode_dict:
        str_decoded += decode_dict[current_symbol]
        current_symbol = ''
print(str_decoded)
