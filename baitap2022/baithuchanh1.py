def helloword():
    print("hello word")
def ten():
    ten=input()
    print("tôi tên là",ten)
def tinh2songuyen():
    a = int(input("nhap so a:"))
    b = int(input("nhap so b:"))
    print("tong:",a+b)
    print("hieu:",a-b)
    print("nhan:",a*b)
    print("thuong:",a/b)
def tinhtuoi():
    namSinh = int(input("nhap nam sinh cua ban:"))
    namhientai = 2022
    tuoi = namhientai-namSinh
    if tuoi ==0 :
        print("tuoi cua ban la:", tuoi + 1)
    elif tuoi < 0 :
        print("tuoi khong ton tai")
        print("nhap lai nam sinh")
    else:
        print("tuoi cua ban la:", tuoi)
def tongchu1songuyen():
    x= int(input("nhap so can tinh:"))
    a=0
    s=0
    if x/10 >=1 :
        s= x%10
        a= int(x/10)
        print("tong la", a+s)
    else:
        print("tong la",x)
def ptbacnhat():
    a= float(input("nhap so a:"))
    b= float(input("nhap so b:"))
    if a==0 and b == 0 :
        print("phuong trinh vo so nghiem")
    elif a==0 and b != 0 :
        print("phuong trinh vo nghiem")
    else:
        c = -b/a
        print("phuong trinh co nghiem la:", c)
def tinhhcn():
    a= float(input("nhap chieu dai:"))
    b= float(input("nhap chieu rong:"))
    c= float(input("nhap chieu cao:"))
    print("chu vi",(a+b)*2)
    print("dien tich", a*b)
    print("the tich",a*b*c)
def hinhtron():
    pi= 3.14
    R= float(input("bk:"))
    if R<0 :
        print("bk k hop le,bk phai lon hon 0")
    else :
        CV = 2*R*pi
        DT = R*R*pi
        print("Cv la",CV)
        print("DT la",DT)
def chanleN():
    N = int(input("nhap so nguyen N:"))
    if N%2==0 :
        print("N la so chan")
    else :
        print("N la so le")