def median(lst):
    sorted_lst = sorted(lst)
    if len(sorted_lst) % 2 == 0:
        mid_index1 = len(sorted_lst) / 2 - 1
        mid_index2 = len(sorted_lst) / 2
        mean = (sorted_lst[mid_index1] + sorted_lst[mid_index2]) / 2
        return mean
    else:
        mid_index = int((len(sorted_lst) + 1) / 2)
        mean = sorted_lst[mid_index - 1]
        return mean

print(median([1,2,3,4,5]))

