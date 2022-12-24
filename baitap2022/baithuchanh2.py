def tinhcvdientich():
    a= float(input("nhap canh goc vuong 1:"))
    b= float(input("nhap canh goc vuong 2:"))
    c= float(input("nhap canh huyen:"))
    if ((a**2+b**2-c**2)==0):
        print("chuvi",a+b+c)
        print("dientich",(a*b)/2)
    else:
        print("k phai tam giac vuong")
def giophutgiay():
    t=int(input('nhap giay'))
    hour=(t//3600)%24
    minute=(t%3600)//60
    second=(t%3600)%60
    if t >=86400 :
        print("vui lòng nhập lại số t bé hơn 24*3600")
    elif t>= 43200 and t<86400 :
        print(str(hour) + ":"+str(minute) + ":"+ str(second), "PM")
    else   :
        print(str(hour) + ":" +str(minute)+":"+str(second),"AM")
def tbchk():
    Co_So_Du_lieu_phantan = 4
    Cau_truc_dulieu = 3
    Chuyen_de_nnlt3 = 3
    NoSQL = 2
    May_Hoc = 3
    a= float(input("mon 1:"))
    b= float(input("mon 2;"))
    c= float(input("mon 3:"))
    d= float(input("mon 4:"))
    e= float(input("mon 5:"))
    Tinh_TB = (a*Co_So_Du_lieu_phantan+b*Cau_truc_dulieu+c*Chuyen_de_nnlt3+d*NoSQL+e*May_Hoc)/(Chuyen_de_nnlt3+Cau_truc_dulieu+Co_So_Du_lieu_phantan+May_Hoc+NoSQL)
    print(Tinh_TB)
def namnhuan():
    year = int(input("nhập năm để ktra"))
    if (year%4==0 and year%100 != 0)or year%400==0:
        print(year,"là năm nhuận ")
    else:
        print(year,"k phải là năm nhuận")
def ngaytrongthang():
    month=int(input("nhập số tháng:"))
    if month in (1,3,5,7,8,10,12):
        print("Tháng",month,"có 31 ngày")
    elif month in (4,6,9,11):
        print("Tháng",month,"có 30 ngày")
    elif month==2 :
        year = int(input("nhập số năm:"))
        if (year%4==0 and year%100 !=0) or year%400 ==0 :
            print("Tháng 2 có 29 ngày")
        else:
            print("Tháng 2 có 28 ngày")
def giaiptbac2():
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    d = b*b - 4*a*c
    if a==0 :
        print("moi nhap lai a")
    if d < 0 :
        print("phương trình vô nghiệm")
    elif d> 0:
        x1 = float(( -b + d**(1/2))/2*a)
        x2 = float(( -b - d**(1/2))/2*a)
        print("phương trình có hai nghiệm")
        print("x1=",x1)
        print("x2=",x2)
    else:
        x  = float(-b/2*a)
        print("x=",x)
def sorachu():
    num= int(input("nhap so:"))
    chuso={0:"không",1:"một",2:"hai",3:"ba",4:"bốn",5:"năm",6:"sáu",7:"bảy",8:"tám",9:"chín",10:"mười"}
    if num <= 10:
        print(chuso[num])
    elif num<=19:
        c=num%10
        print("mười",chuso[c])
    else:
        a= num//10
        b= num%10
        print(chuso[a],"mươi",chuso[b])
def ngayketiep():
    ngay= int(input("nhập ngày:"))
    thang= int(input("nhập tháng:"))
    nam= int(input("nhập năm:"))
    if ngay>=32 or thang>=13:
        print("ngay khong ton tai")
    if thang in (4,6,9,11) and ngay <=30:
        ngaymoi = ngay +1
        if ngaymoi >30:
            ngaymoi = 1
            thangmoi = thang +1
            print(ngaymoi,thangmoi,nam)
    elif thang in (1,3,5,7,8,12):
        ngaymoi= ngay + 1
        if ngaymoi >31:
            ngaymoi= 1
            thangmoi= thang + 1
            if thangmoi >12:
                thangmoi = 1
                nammoi = nam + 1
                print(ngaymoi,thangmoi,nammoi)
    else:
        ngaymoi= ngay + 1
        if ngaymoi>28 and nam%400==0 :
            print(ngaymoi,thang,nam)
        elif ngaymoi>28 and nam%400 != 0:
            ngaymoi= 1
            thangmoi= thang +1
            print(ngaymoi,thangmoi,nam)
def quitrongnam():
    a= int(input("nhập tháng:"))
    if a in (1,2,3):
        print("Quí I")
    elif a in (4,5,6):
        print("Quí II")
    elif a in (7,8,9):
        print("Quí III")
    elif a in (10,11,12):
        print("Quí IV")
