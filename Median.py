def median(lst):
    lst = sorted(lst)
    num = len(lst)
    mid = int(num / 2)
    if num % 2 == 0:
        mid1 = mid - 1
        median = (lst[mid] + lst[mid1]) / 2
    else:
        median = lst[mid]
    #return median
    print(median)
median([4,5,5,4])