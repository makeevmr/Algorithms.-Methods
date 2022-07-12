n = int(input())
A = list(map(int, input().split()))
inversions_counter = 0


def merge_sort(lst, left, right):
    if left < right:
        middle = (left + right) // 2
        return merge(merge_sort(lst, left, middle), merge_sort(lst, middle + 1, right))
    else:
        return [lst[right]]


def merge(lst1, lst2):
    global inversions_counter
    sorted_lst = []
    while lst1 and lst2:
        if lst1[0] > lst2[0]:
            inversions_counter += len(lst1)
            sorted_lst.append(lst2[0])
            del lst2[0]
        else:
            sorted_lst.append(lst1[0])
            del lst1[0]
    if lst1:
        for number in lst1:
            sorted_lst.append(number)
    else:
        for number in lst2:
            sorted_lst.append(number)
    return sorted_lst


merge_sort(A, 0, len(A) - 1)
print(inversions_counter)
