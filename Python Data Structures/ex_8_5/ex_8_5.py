text = open('mbox-short.txt')
count = 0
for line in text:
    words = line.split()
    if len(words) < 1:
        continue
    if words[0] == "From":
        count = count + 1
        print(words[1])
print("There were", count, "lines in the file with From as the first word")
