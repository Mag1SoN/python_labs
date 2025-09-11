a = input("a: ")
b = input("b: ")
a = a.replace(',','.')
b = b.replace(',','.')
a = float(a)
b = float(b)
sum = a+b
avg = (a+b)/2
print(f"sum={sum:.2f}; avg={avg:.2f}")