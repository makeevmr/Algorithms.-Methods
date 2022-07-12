n = int(input())
steps_lst = list(map(int, input().split()))
max_sum_step_lst = [0, steps_lst[0]]


def max_sum_steirs_bu(step_number):
    for i in range(2, step_number + 1):
        max_sum_step_lst.append(steps_lst[i - 1] +
                                max(max_sum_step_lst[0], max_sum_step_lst[1]))
        del max_sum_step_lst[0]
    return max_sum_step_lst[1]


print(max_sum_steirs_bu(n))
