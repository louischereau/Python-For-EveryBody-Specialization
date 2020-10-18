text = open('romeo.txt')
lst = list()
for lines in text:
    words = lines.split()
    for i in range(len(words)):
        if words[i] not in lst:
            lst.append(words[i])
        i = i + 1
lst.sort()
print(lst)
