a = input("")
i = 0
Check = ["A", "B", "C"]
Change = ["_a", "_b", "_c"]
for Check in a:
    b = str(a).replace(Check[0+i], Change[0+i])
    break
else:
    i+1

print(b)
