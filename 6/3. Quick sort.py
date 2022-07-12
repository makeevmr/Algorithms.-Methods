import random


def quick_sort(lst, left, right):
    random_int = random.randint(left, right)
    p = lst[random_int]
    l = left
    r = right
    while l <= r:
        while lst[l] < p:
            l += 1
        while lst[r] > p:
            r -= 1
        if l <= r:
            lst[l], lst[r] = lst[r], lst[l]
            l += 1
            r -= 1
    if left < r:
        quick_sort(lst, left, r)
    if right > l:
        quick_sort(lst, l, right)


def binary_search(lst, value):
    left = 0
    right = len(lst) - 1
    while left < right:
        middle = (left + right) // 2
        if lst[middle] == value:
            return (left + right) // 2
        elif lst[(left + right) // 2] > value:
            right = (left + right) // 2 - 1
        else:
            left = (left + right) // 2 + 1
    return left


def left_border(lst, value):
    left = 0
    right = len(lst) - 1
    while left < right:
        middle = (left + right) // 2
        if lst[middle] == value:
            right = middle
        elif lst[middle] > value:
            right = (left + right) // 2 - 1
        else:
            left = (left + right) // 2 + 1
    return left


def right_border(lst, value):
    left = 0
    right = len(lst) - 1
    while left < right:
        if right - left > 1:
            middle = (left + right) // 2
        else:
            middle = (left + right) // 2 + 1
        if lst[middle] == value:
            left = middle
        elif lst[middle] > value:
            right = (left + right) // 2 - 1
        else:
            left = (left + right) // 2 + 1
    return left


n, m = map(int, input().split())
left_points_lst = []
right_points_lst = []
for _i in range(n):
    ai, bi = map(int, input().split())
    left_points_lst.append(ai)
    right_points_lst.append(bi)
points = list(map(int, input().split()))
quick_sort(left_points_lst, 0, len(left_points_lst) - 1)  # sorting left values of segment
quick_sort(right_points_lst, 0, len(right_points_lst) - 1)  # sorting right values of segment
for point in points:  # counting amount of points
    left_points_counter = 0
    right_points_counter = 0
    nearest_left_index = binary_search(left_points_lst, point)
    nearest_right_index = binary_search(right_points_lst, point)
    if left_points_lst[nearest_left_index] == point:
        right_value1 = right_border(left_points_lst, point)
        left_points_counter += right_value1 + 1
    elif left_points_lst[nearest_left_index] > point:
        left_points_counter += nearest_left_index
    else:
        left_points_counter += nearest_left_index + 1
    if right_points_lst[nearest_right_index] == point:
        left_value2 = left_border(right_points_lst, point)
        right_points_counter += left_value2
    elif right_points_lst[nearest_right_index] <= point:
        right_points_counter += nearest_right_index + 1
    else:
        right_points_counter += nearest_right_index
    print(left_points_counter - right_points_counter, end=' ')
