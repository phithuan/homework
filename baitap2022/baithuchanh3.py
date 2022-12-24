def tinhdayso():
    n=int(input('nhập n: '))
    gt=1
    x = float(input("nhập X:"))
    S = 0
    for i in range(1,n+1):
        gt*=i
        S= S + x**i/gt 
    print(S)
def ktrasonguyento():
    flag=1
    while flag:
        n= int(input("nhập số nguyên:"))
        if n<0 :
            print("Vui lòng nhập số nguyên dương")
        elif n< 2:
            print("N không phải là số nguyên tố")
        elif n==2:
            print("N là số nguyên tố")
        else:
            for i in range(2,n-1,1):
                if n%i==0:
                    a=1
                    break
                else:
                    b=0
            if a==1:
                print(n,"k là số nguyên tố")
            else:
                print(n,"là số ngto")
        print("có muốn tiếp tục nữa không,1 để tiếp tục 0 để keets thuc")
        flag=int(input())
def bcc():
    for i in range(1,10):
        for j in range(2,10):
            print(i,"x",j,"=",i*j,end="\t\t")
            print(end='\n')
def doanso():
    import random
    flag=1
    while flag: 
        songaunhien=random.randint(1,100)
        for i in range(0,7):
            sodoan=int(input())
            if sodoan>songaunhien:
                print("số bn đoán lớn hơn")
            elif sodoan<songaunhien:
                print("sô bn đoán lơn hơn")
            else:
                print("Chúc mừng bn đã đoán đúng")
                break
        print("Bn muốn tiếp tục không?,nhập 1 để tiếp tục 0 để kết thúc trò chơi")
        flag=int(input())
