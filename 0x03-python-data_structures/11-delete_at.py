def delete_at(my_list=[], idx=0):
    n = len(my_list)
    if idx >= 0 and idx < n:
        del my_list[idx]
    return (my_list)
