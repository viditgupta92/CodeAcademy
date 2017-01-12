def censor(text, word):
    data = text.split(" ")
    num = len(word)
    ast = ""
    res = ""
    for i in range(len(word)):
        ast += "*"
    for ind,val in enumerate(data):
        if val == word:
            res += ast
        else:
            res += val
        if ind != len(data) -1:
            res += " "
    #return res
    print(res)
censor("this hack is wack hack", "hack")