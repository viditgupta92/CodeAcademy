def reverse(text):
    t = len(text)
    rev = ""
    for i in range(t-1,-1,-1):
        rev += text[i]
    print(rev)

reverse("tatoo")