a = [20,0,30,12,45,67,98,100]
p = []
for i in range(0,len(a)):
    if (i ==0):
        p.append(a[i])
    else:
        p.append(p[i-1] + a[i])

print(a)
print(p)

print("3rd to 5th elel",{p[4]-p[1]})