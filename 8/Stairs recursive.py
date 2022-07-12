n = int(input())
steps_lst = list(map(int, input().split()))
max_sum_step_lst = [float('-inf') for _i in range(len(steps_lst) + 1)]
max_sum_step_lst[0] = 0


def max_sum_steirs_td(step_number):
    if max_sum_step_lst[step_number] == float('-inf'):
        if step_number == 1:
            max_sum_step_lst[step_number] = steps_lst[step_number - 1]
        else:
            max_sum_step_lst[step_number] = steps_lst[step_number - 1] + max(max_sum_steirs_td(step_number - 1),
                                                                             max_sum_steirs_td(step_number - 2))
    return max_sum_step_lst[step_number]


max_sum_steirs_td(n)
print(max_sum_steirs_td(len(steps_lst)))
