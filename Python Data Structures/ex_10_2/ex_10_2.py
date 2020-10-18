file = open("mbox-short.txt")
count = dict()
for lines in file:
    words = lines.split()
    if len(words) < 1:
        continue
    if words[0] == "From":
        time = words[5]
        hour = time.split(":")
        hr = hour[0]
        count[hr] = count.get(hr,0) + 1
for k,v in sorted(count.items()):
    print(k, v)
