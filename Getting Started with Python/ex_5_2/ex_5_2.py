largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        i = int(num)
        y = int(num)
    except:
        print("Invalid Input")
    if largest is None:
        largest = i
    elif i > largest:
        largest = i
    if smallest is None:
        smallest = y
    elif smallest > y:
        smallest = y
print("Maximum is", largest)
print("Minimum is", smallest)
