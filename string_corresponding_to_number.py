import collections
two_digit_dict = collections.OrderedDict

def two_digits(num,lst):
    if num <= 20:
        return dict[num]
    else:
        if num % 10 == 0:
            return dict[num]
        else:
            return two_digit_dict[lst[1]] +" " + dict[lst[0]]


def num_to_string(num):
    dict = collections.OrderedDict
    temp = num
    ctr = 0
    lst = []
    while temp != 0:
        lst.append(temp % 10)
        temp = int(temp/10)
        ctr += 1
    dict[1] = 'one'
    dict[2] = "two"
    dict[3] = "three"
    dict[4] = "four"
    dict[5] = "five"
    dict[6] = "six"
    dict[7] = "seven"
    dict[8] = "eight"
    dict[9] = "nine"
    dict[10] = "ten"
    dict[11] = "eleven"
    dict[12] = "twelve"
    dict[13] = "thirteen"
    dict[14] = "fourteen"
    dict[15] = "fiveteen"
    dict[16] = "sixteen"
    dict[17] = "seventeen"
    dict[18] = "eighteen"
    dict[19] = "nineteen"

    two_digit_dict[2] = "twenty"
    two_digit_dict[3] = "thirty"
    two_digit_dict[4] = "fourty"
    two_digit_dict[5] = "fifty"
    two_digit_dict[6] = "sixty"
    two_digit_dict[7] = "seventy"
    two_digit_dict[8] = "eighty"
    two_digit_dict[9] = "ninty"
    two_digit_dict[10] = "hundred"

    digits = len(lst)
    if digits ==1:
        res = dict[lst[0]]
    elif digits == 2:
        res = two_digits(num,lst)
    return res
    # elif digits == 3:
    #     three_digits(lst)
    # elif digits == 4:
    #     four_digits(lst)
    # elif digits == 5:
    #     five_digits(lst)

num_to_string(45)
#print(num_to_string(4))