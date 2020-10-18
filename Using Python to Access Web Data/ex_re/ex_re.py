import re
sumtotal = 0
file = open("regex_sum_719146.txt")
for lines in file:
    numberList = re.findall('[0-9]+',lines)
    if len(numberList) < 1:
        continue
    for number in numberList:
        sumtotal = sumtotal + int(number)
print(sumtotal)
