a = "Helloooooooooo"
# assign variables to a expression
if (n := len(a)) > 10:
    print(f"Too Long {n} elements")
while (n := len(a)) > 1:
    print(n)
    a = a[:-1]
print(a)