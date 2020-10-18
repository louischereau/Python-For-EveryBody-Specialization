text = "X-DSPAM-Confidence:    0.8475";
a = text.find('0')
b = text.find('5')
c = text[a:b+1]
print(float(c))
