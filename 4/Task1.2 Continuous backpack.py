n, W = map(int, input().split())
total_value = 0.0
dict_kilo = {}
lst_price = []
for _i in range(n):
    c, w = map(int, input().split())
    if c / w not in dict_kilo:
        dict_kilo[c / w] = w
    else:
        dict_kilo[c / w] += w
    lst_price.append(c / w)
lst_price.sort(reverse=True)
while W > 0 and len(lst_price) > 0:
    if W > dict_kilo[lst_price[0]]:
        total_value += lst_price[0] * dict_kilo[lst_price[0]]
        W -= dict_kilo[lst_price[0]]
        del lst_price[0]
    else:
        total_value += lst_price[0] * W
        W = 0
print(f'{total_value:.3f}')
