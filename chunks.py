one = "malayalam"
two = "mmaaaally"

def checkString(one,two):
    if len(one) != len(two):
        return "string is not have same len"
    letters_count = {}
    for i in one:
        if i in letters_count:
            letters_count[i] += 1
        else:
            letters_count[i] = 1
    for j in two:
        if j not in letters_count or two.count(j) != letters_count[j]:
            return f"{j} is not in string{one} or \noccurence |{two.count(j)}| is not matching \n{letters_count}"
       
    print(letters_count)

    return "successfull"

result = checkString(one,two)
print(result)