a=[[12,5,7,3],[2,8,4,2]]
b=a[::-1]
print(b)
for i in range(len(b)):
    c=b[i][::-1]
    print(c,end='')