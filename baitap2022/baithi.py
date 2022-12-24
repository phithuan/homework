n=[1, 5, 10, 4, 19, 26, 40, 20, 21, 21, 40, 2, 41, 44, 39]
lst = []
sochan=sole=0
for i in range(len(n)):
    n1 = n[i:i+1]
    print(n1)
    for j in n1:
        if j%2==0:
            sochan+=1
        else:
            sole+=1
        break
print('số lượng chẵn',sochan)
print('số lượng lẽ',sole)