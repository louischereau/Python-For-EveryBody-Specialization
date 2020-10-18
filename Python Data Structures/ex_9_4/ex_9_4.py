file = open("mbox-short.txt")
count =  dict()
for lines in file:
    words = lines.split()
    if len(words) < 1 :
        continue
    if words[0] == "From":
        name = words[1]
        count[name] = count.get(name,0) + 1
biggestcount = None
biggestword = None
for name,count in count.items():
    if biggestcount is None or count > biggestcount:
        biggestword = name
        biggestcount = count
print(biggestword, biggestcount)
