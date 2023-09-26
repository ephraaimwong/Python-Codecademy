def remove_duplicates(lst):
    clean_list = []
    for i in lst:
        if i not in clean_list:
            clean_list.append(i)
    return clean_list