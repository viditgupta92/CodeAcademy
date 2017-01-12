def remove_duplicates(lst):
    values = list(lst)
    for each in lst:
        count = 0
        for ind,val in enumerate(values):
            if each == val:
                count += 1
                if count > 1:
                    values.pop(ind)
    return values
remove_duplicates([6,6,6,6,6])