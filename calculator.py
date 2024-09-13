f = open('input.txt')
c = open('output.txt')
a = []
for i in f:
    for j in i:
        a.append(j)
if a[2] == "+":
    c.write(int(a[0]) + int(a[1]))
elif a[2] == "-":
    c.write(int(a[0]) - int(a[1]))
elif a[2] == "*":
    c.write(int(a[0]) * int(a[1]))
    
