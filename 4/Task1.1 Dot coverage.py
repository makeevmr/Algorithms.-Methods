n = int(input())
lst_coordinates = list()
dot_counter = 0
lst_dot_coordinates = []
for _i in range(n):
    l, r = map(int, input().split())
    lst_coordinates.append(list((l, r)))
    lst_coordinates.sort(key=lambda x: x[1])
while lst_coordinates:
    dot_counter += 1
    lst_dot_coordinates.append(lst_coordinates[0][1])
    del_lst = [lst_coordinates[0]]
    if len(lst_coordinates) > 1:
        for i in range(1, len(lst_coordinates)):
            if lst_coordinates[i][0] <= lst_coordinates[0][1]:
                del_lst.append(lst_coordinates[i])
    for segment in del_lst:
        lst_coordinates.remove(segment)
print(dot_counter)
for coordinate in lst_dot_coordinates:
    print(coordinate, end=' ')
