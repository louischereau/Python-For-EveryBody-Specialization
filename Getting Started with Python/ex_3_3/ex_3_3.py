# Ask for score
x = input("What is your score")
i = float(x)
if i < 0:
    print("Error")
elif i > 1:
    print("Error")
elif i >= 0.9:
    print("A")
elif i >= 0.8:
    print("B")
elif i >= 0.7:
    print("C")
elif i >= 0.6:
    print("D")
elif i < 0.6:
    print("F")
