# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
u = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    x = line.find('.')
    y = line.find(' ',x)
    z = line[x-1:y]
    u = u + float(z)
average = u/count
print("Average spam confidence:",average)
