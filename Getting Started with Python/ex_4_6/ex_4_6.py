hours = input("Number of hours")
rate = input("Pay rate")
h = float(hours)
r = float(rate)
def computepay(h,r):
    if h <= 40:
        return h * r
    if h > 40:
        return (40*r)+(h-40)*(1.5*r)
p = computepay(h,r)
print("Pay",p)
