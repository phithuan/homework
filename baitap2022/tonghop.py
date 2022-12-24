#thực hành 1
#Bai1
def hello ():
  print ("hello word")
#bai2
def name():
  name = input()
  print ("xin chao toi ten la", name)
#bai3
def songuyen ():
  a= int(input())
  b= int(input())
  print("tong la",a+b)
  print("hieu la",a-b)
  print("tich la",a*b)
  print("thuong la",a/b)
#bai4
def age ():
  namsinh = int(input())
  namhientai= int(input())
  tuoi = namhientai - namsinh
  if tuoi == 0 :
    print("tuoi cua ban",tuoi + 1 )
  elif tuoi <0 :
    print ("tuoi k ton tai")
  else :
    print ("tuoi cua ban la ",tuoi)
#bai5
def tinhphantu ():
   a=int(input("nhap so can tinh :"))
   print ("tong cac", a//10 + a%10 )
#bai6
def ptbac1():
  a= float(input())
  b= float(input())
  if a== 0 and b == 0:
    print ("pt vo so nghiem")
  elif a==0 and b!= 0:
    print ("pt vo nghiem")
  else :
    print("pt có nghiệm duy nhất ", -b/a)
#bai7
def cn():
  d=float(input())
  r=float(input())
  print("dt=",d*r)
  print("cv=",(d+r)*2)
# bai8
def cv():
  pi=3.14
  r= float(input())
  print("cv=",2*r*pi)
  print("dt=",r*r*pi)
#bai9
def ktra():
  n=int(input())
  if n % 2 == 0 :
    print ("N la so chan")
  else :
    print ("N la so le ")
#--------------------------------------------------
#thực hành 2
#bai1
def cvdt():
  a =float(input())
  b =float(input())
  c =float(input())
  print("cv=",a+b+c)
  print("dt=",(a*b)/2)
#bai2
def chuyengio():
  t =int(input("nhap so giay"))
  hour = int(t/3600%24)
  minute= int(t%3600/60)
  second= int(t%3600%60)
  if hour <12 :
    print (hour,":",minute,":",second,"AM")
  else :
    hour = int(t/3600%12)
    print(hour,":",minute,":",second,"PM")
#bai3
def dtb():
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
#bai 4
def yearcheck():
  year = int(input("nhap nam"))
  if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print ("nam",year,"la nam nhuan")
  else :
    print ("nam",year,"la nam ko nhuan")
#bai5
def demsongay():
  month= int(input())
  if month in [1,3,5,7,8,10,12]:
    print ("thang do co 30 ngay")
  elif month in [4,6,9,11]:
    print ("thang do co 31 ngay")
  else :
    year = int(input("yeu cau nhap nam:"))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
      print ("thang do co 29 ngay")
    else :
      print ("thang do co 28 ngay")
#bai6
import math
def ptbac2():
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
#bai7
def docsothanhchu():
  n= int(input("nhập số nguyên n= "))
  if n < 10 :
    def so_co_1_chu_so(sobehon10):
      disc1 = {
        1: "một",
        2: "hai",
        3: "ba" ,
        4: "bốn",
        5: "năm",
        6: "sáu",
        7: "bảy",
        8: "tám",
        9: "chín"
      };
    return disc1.get(sobehon10)
    print(so_co_1_chu_so(n))
  elif n > 10 and n < 99 :
    if n//10 : # doc so hang chuc
      def sohangchuc (sochuc):
        disc2= {
          1 :"mười",
          2 :"hai mươi",
          3 :"ba mươi",
          4 :"bốn mươi",
          5:"năm mươi",
          6 :"sáu mươi",
          7 :"bảy mươi",
          8 :"tám mươi",
          9 :"chin mươi",
        }
        return disc2.get(sochuc);
      def sohangdonvi (sodonvi): # in số hạng đơn vị
        n% 10
        disc3= {
              1: "mốt",
              2: "hai",
              3: "ba" ,
              4: "bốn",
              5: "lăm",
              6: "sáu",
              7: "bảy",
              8: "tám",
              9: "chín"
        }
        return disc3.get(sodonvi);
    print(sohangchuc(n//10),sohangdonvi(n%10)) ;
  else :
    print ("giá trị không tồn tại ")


#bai8
def ngaytt():
  day = int(input("nhap ngay :"))
  month = int(input("nhap thang :"))
  year = int(input("nhap nam :"))
  if day>=32 or month>=13 or day < 0:
       print("Gia tri k ton tai ,Yeu cau nhap lai ")
  if month in [4, 6, 9, 11] :
    if day <30 :
      day+=1
      print(day,":",month,":",year )
    elif day == 30 :
      month +=1
      day=1
      print (day,":",month ,":",year )
  elif month in [1, 3, 5, 7, 8, 10] :
    if day <31 :
      day+=1
      print(day,":",month,":",year )
    elif day == 31 :
      month +=1
      day= 1
      print(day,":",month,":",year )
  elif month in [12]:
    if day <31 :
      day+=1
      print(day,":",month,":",year )
    elif day == 31 :
      month =1
      day= 1
      year += 1
      print(day,":",month,":",year )
  else  :
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
     if day <29 :
      day+=1
      print(day,":",month,":",year )
    elif day == 29 :
      month +=1
      day=1
      print(day,":",month,":",year )
    else :
      if day <28 :
        day +=1
        print(day,":",month,":",year )
      elif day == 28 :
        month +=1
        day=1
        print(day,":",month,":",year )
#bai9
def pheptoan():
  a=int(input("nhap gia tri a :"))
  b=int(input("nhap gia tri b "))
  pheptinh = input("yeu cau nhap phep tinh :")
  if pheptinh == "+":
    print("giá trị phép tính =",a+b)
  elif pheptinh == "-":
    print("giá trị phép tính =",a-b)
  elif pheptinh == "*":
    print("giá trị phép tính =",a*b)
  elif pheptinh == "/":
    print("giá trị phép tính =",a/b)
  else :
    print ("khong ton tai")

#bai 10
def xuatngaythang():
  a= int(input("nhập tháng:"))
  if a in (1,2,3):
      print("Quí I")
  elif a in (4,5,6):
      print("Quí II")
  elif a in (7,8,9):
      print("Quí III")
  elif a in (10,11,12):
      print("Quí IV")

#----------------------------------------------------------------
#thực hành 3
#bai 1
def csn():
  x=int(input(" x:"))
  n=int(input(" n:"))
  S = 0
  for i in range (1,n+1):
    S= S + x**i/math.factorial(i)
    i +=1
  print(S)
#bai2
def ktrasonguyen():
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
                    a=0
            if a==1:
                print(n,"k là số nguyên tố")
            else:
                print(n,"là số ngto")
        print("có muốn tiếp tục nữa không,1 để tiếp tục 0 để keets thuc")
        flag=int(input())
#bai3
def bangcuuchuong():
    for i in range(1, 11):
        for j in range(2, 10):
            print(j,"x", i, "=", j*i, end="\t")
        print()
#bài 4
def hinh1(n):
  for i in range (n):
    for j in range(n):
      if i == 0 or i == 3 or (i ==1  and j in[0,3])or (i ==2  and j in[0,3]):
        print ("*",end = ' ')
      else :
        print (" ",end= ' ')
    print()
def hinh2(n):
  for i in range (n):
      for j in range(n):
        if i == 3 or (i==0 and j in [3])or (i==1 and j in [2,3])or (i==2 and j in [1,2,3]) :
          print ("*",end = ' ')
        else :
          print (" ",end= ' ')
      print()
def hinh3(n):
  for i in range (n):
      for j in range(n):
        if (i== 0 and j in[0]) or (i== 1 and j in[0,1])or (i== 2 and j in[0,2]) or (i== 3) or (i== 4 and j in[4,6]) or (i== 5 and j in[5,6]) or (i== 6 and j in[6]):
          print ("*",end = ' ')
        else :
          print (" ",end= ' ')
      print( )


#bai5
def csn1():
  x=int(input(" x:"))
  n=int(input(" n:"))
  S = 0
  for i in range (1,n+1,2):
    S= S + x**i/math.factorial(i)
    print(S)
#bai6
import random
def gamedoanso():
  flag=1
  while flag :
    songaunhien = random.randint(1,100)
    for i in range (0,7):
      sodoan= int(input())
      if sodoan >songaunhien:
        print("số đoán lớn hơn số ngẫu nhiên")
      elif sodoan < songaunhien:
        print("số đoán bé hơn số ngẫu nhiên")
      else :
        print("Bạn đã chiến thắng")
        break
      print("Bn muốn tiếp tục không?,nhập 1 để tiếp tục 0 để kết thúc trò chơi")
      flag=int(input())
#bai7
def dttamgiac():
    print("lưu ý tổng 2 cạnh phải lớn hai cạnh còn lại")
    a= float(input("nhập cạnh a:"))
    b= float(input("nhập cạnh b:"))
    c= float(input("nhập cạnh c:"))
    tong = a+b
    cv= a+b+c
    p= cv/2
    dt = math.sqrt(p*(p-a)*(p-b)*(p-c))
    if tong >c:
        print("diện tích tam giác theo ct herong:",dt)
    else:
        pass
#bai8
def tinhtb():
  Môn1= float(input("Nhập điểm học phần toán rời rạc "))
  Môn2= float(input("Nhập điểm học phần Vậy lý 1 "))
  Môn3= float(input("Nhập điểm học phần à Tư tưởng Hồ Chí Minh "))
  print("điểm trung bình :",format((Môn1+Môn2+Môn3)/3,'.2f'))

#bai9
import math
def tinhcan():
    n =int(input("nhập N:"))
    tich = math.sqrt(2)
    for i in range(1,n):
        tich= math.sqrt(2+tich)
    print(tich)
#bai10
def hinh101(n):
  for i in range (n):
      for j in range(n):
        if (i== 0 and j in[3]) or (i== 1 and j in[3,4])or (i== 2 and j in[3,4,5]) or (i== 3) or (i== 4 and j in[0,1,2]) or (i== 5 and j in[0,1]) or (i== 6 and j in[0]):
          print ("*",end = ' ')
        else :
          print (" ",end= ' ')
      print( )
def hinh102(n):
  for i in range (n):
      for j in range(n):
        if (i== 0 and j in[3]) or (i== 1 and j in[3,4])or (i== 2 and j in[3,5]) or (i== 3) or (i== 4 and j in[0,2]) or (i== 5 and j in[0,1]) or (i== 6 and j in[0]):
          print ("*",end = ' ')
        else :
          print (" ",end= ' ')
      print( )
def hinh103():
  for i in range (n):
      for j in range(n):
        if (i== 0 and j in[3,4,5,6]) or (i== 1 and j in[3,4,5])or (i== 2 and j in[3,4]) or (i== 3 and j ==3 ) or (i== 4 and j in[2,3]) or (i== 5 and j in[1,2,3]) or (i== 6 and j in[0,1,2,3]):
          print ("*",end = ' ')
        else :
          print (" ",end= ' ')
      print( )
def hinh104(n):
  for i in range (n):
      for j in range(n):
        if (i== 0 and j in[3,4,5,6]) or (i== 1 and j in[3,5])or (i== 2 and j in[3,4]) or (i== 3 and j ==3 ) or (i== 4 and j in[2,3]) or (i== 5 and j in[1,3]) or (i== 6 and j in[0,1,2,3]):
          print ("*",end = ' ')
        else :
          print (" ",end= ' ')
      print( )
####################################
#thực  hanh 4
import math
# bai1
def tinhdodaiAB():
    print("Nhập tọa dộ của A:")
    x_A = int(input("Nhập tọa đọ xA:"))
    y_A = int(input("Nhập tọa đọ yA:"))
    print("Nhập tọa dộ của B:")
    x_B = int(input("Nhập tọa đọ xB:"))
    y_B = int(input("Nhập tọa đọ yB:"))
    dodai = math.fabs(math.sqrt((x_B - x_A)**2 + (y_B - y_A)**2))
    print("Độ dài 2 điểm là: ", dodai)

#bai2
def log():
    a= float(input("nhập a:"))#a khác 1
    x= float(input("nhập x:")) #x là cơ số
    c=math.log(x,a)
    print(c)

#bai3
def uocso():
	a = int(input("a:"))
	b = int(input("b:"))
	uocso = max(a,b)
	for i in range(a,1,-1):
		if a % uocso == 0 and b % uocso ==0:
			return uocso
		else:
		 	uocso = i

 # cach 2
def uocso1():
	a = int(input("a:"))
	b = int(input("b:"))
	print(math.gcd(a,b))
#bai4
def tong(a=7):
		b = int(input())
		c = int(input())
		return a+ b +c

#bai5
def songuyento(n):
    #Có sử dụng cấu trúc lambda
    if n <= 1:
        print(n,"Không là số nguyên tố")
        return
    elif n == 2:
        print(n,"là số nguyên tố")
        return
    lst = list(range(2,n))
    (lambda x: print(n,"là số nguyên tố") if 0 not in [n % i for i in lst] else print(n,"Không là số nguyên tố"))(n)

#bai6
def giaithua():
    Milestones =1
    while Milestones :
      n= int(input("Nhập số cần tính giai thừa: "))
      if n < 0 :
        print ("Vui lòng nhập số tự nhiên !!")
      else :
        mutiples = 1
        for i in range(1,n+1):
          mutiples *= i
      print ("kết quả giai thừa được tính :",mutiples)
      print("Ban muon tiep tuc khong? Nhap 1 de tiep tuc, 0 de ket thuc")
      Milestones = int(input())
#bai7
def bmi ():
  print("Chương trình tính BMI :Weight (KG) and Height(m)")
  weight=float(input(" Nhập vào weight :"))
  height=float(input("Nhập vào height :"))
  BMI= weight/(height*height)
  if BMI <18.5 :
    print ("Chỉ số BMI:",BMI ,"Phân loại :gầy","Nguy cơ : bệnh thấp ")
  elif 18.5 <BMI<24.9 :
    print ("Chỉ số BMI:",BMI ,"Phân loại :bình thường","Nguy cơ bệnh trung bình ")
  elif 25.0 <BMI<29.9 :
    print ("Chỉ số BMI:",BMI ,"Phân loại :hơi béo","Nguy cơ: bệnh cao ")
  elif 30.0 <BMI<34.9 :
    print ("Chỉ số BMI:",BMI ,"Phân loại :béo phì 1","Nguy cơ bệnh cao ")
  elif 35.0 <BMI<39.9 :
    print ("Chỉ số BMI:",BMI ,"Phân loại :béo phì cấp độ 2","Nguy cơ bệnh rất cao ")
  else :
    print ("Chỉ số BMI:",BMI ,"Phân loại :béo phì cấp độ 2","Nguy cơ bệnh nguy hiểm ")

#bai8
def tinh_tong(n):
	if n:
		return n + tinh_tong(n-1)
	return 0
#bai9
def thaphanoi(n, cot1,cot2,cot3):
	if n == 1:
		print("chuyển từ" ,cot1, "sang", cot3)
	else:
		thaphanoi(n-1, cot1,cot3,cot2)
		thaphanoi(1,cot1,cot2,cot3)
		thaphanoi(n-1,cot2,cot1,cot3)

##################################
#bai thực hành 5
#bai1
def tinhhetcaroi():
    dt= float(input("DOANH THU:"))
    cp= float(input("CHI PHI:"))
    roi = (dt - cp)/cp
    print("chỉ số ROI của bạn",roi)
    if roi >= 0.75:
        print("Đầu tư đi thg lz")
    else:
        print("Đầu tư là cháy tài khoản đó thg ngu này")

#bai2
def fibonacci(n):
    if n ==1 or n==0:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
#print("những số đầu tiên của dãy số fibonacci:")
fib = ""
for i in range(1,12):
    fib += str(fibonacci(i)) + ","
#print(fib,"...")

#bai4
def osc():
    for n in range(-3,5):
        print(n,end=" ")
        print(n*-1,end=" ")
    print()

#bai5
def hoanthien():
  def ktsohoanthien(n):
      tong = 0
      for i in range(1,n):
          if (n % i) == 0:
              tong += i
      if tong == n: #nếu số thịnh vượng thì thay đổi tong != n
          return True
      else:
          return False
  n= int(input("nhập số nguyên n:"))
  if ktsohoanthien(n):
      print(n,"là số hoàn thiện")
  else:
      print(n,"là số ko hoàn thiện")
#########################
#bài thực hành 6
#Bai 1
'''Dùng vòng lặp while vô tận, cho phép Nhập vào một Chuỗi. Xuất Chuỗi này có phải đối
xứng hay không?
Hỏi người sử dụng có tiếp tục phần mềm. Nếu tiếp tục thì nhập Chuỗi mới, còn không thì
thoát và thông báo cảm ơn'''
def xaudoixung():
    xdx= 1
    while xdx :
        S=input("Nhap xau S :")
        x =''
        for i in S :
            x= i+x
        if x==S :
            print("Là sâu đối xứng")
        else :
            print("Là xâu không đối xứng")
        print("Ban muon tiep tuc khong? Nhap 1 de tiep tuc, 0 de ket thuc")
        xdx = int(input())
# cach2
def xaudoixung():
    xdx= 1
    while xdx :
        str=input("nhap xau")
        if str[::-1] ==str :
            print("xau doi xung")
        else :
            print("xau ko dôi xứng ")
        print("Ban muon tiep tuc khong? Nhap 1 de tiep tuc, 0 de ket thuc")
        xdx = int(input())
#bai2
'''Một Chuỗi được gọi là tối ưu khi:
1. Không chứa các khoảng trắng dư thừa,
2. Các từ cách nhau bởi một khoảng trắng.
3. Ký tự đầu tiên của các từ Viết Hoa.'''
def toiuu_chuoi ():
    def toiuuchuoi(s):
        tachchuoi = s.split()
        chuoi = ""
        for i in tachchuoi:
            chuoi += " "+i
        return chuoi
    str= input("Nhập chuỗi chưa tối ưu :")
    print("Chuỗi tối ưu là:",toiuuchuoi(str).title().strip())
#bai3
'''1. Xuất các chữ số trên các dòng riêng biệt
2. Xuất có bao nhiêu chữ số chẵn
3. Xuất có bao nhiêu số âm
4. Xuất có bao nhiêu chữ số nguyên tố
5. Tính giá trị trung bình'''

import math
import statistics
def xulychuoi():
  list = [5,7,8,-2,8,11,13,9,10]
  count_number=[]
  count_negative = []
  print ("các chữ số riêng biệt :")
  for i in list :
    print(i)
    if i% 2 == 0 :
      count_number.append(i)
    if i <0 :
      count_negative.append(i)
  bodem=0
  def ktsonguyento(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
  for n in list :
    if ktsonguyento(n)== True:
        bodem = bodem +1
    else :
        pass
  print ("có tất cả số chẵn là :",len(count_number))
  print ("có tất cả số âm là :",len(count_negative))
  print("có tất cá số nguyên tố là : ",bodem)
  print("Gía trị trung bình là : ",statistics.median(list ))

#bai4
'''1. Bao nhiêu chữ IN HOA
2. Bao nhiêu chữ in thường
3. Bao nhiêu chữ là chữ số
4. Bao nhiêu chữ là ký tự đặc biệt
5. Bao nhiêu chữ là khoảng trắng
6. Bao nhiêu chữ là Nguyên Âm
7. Bao nhiêu chữ là Phụ âm'''
def kt():
    str= " khi Nao Trai Tim 123$!#!@#!1"
    print ("số lượng kí tự trong chuỗi ",len(str),"kí tự")
    NA= ('a','e','i','o','u','A','E','I','O','U')
    pa=('b','c','d','đ','g','h', 'k', 'l', 'm', 'n', 'p', 'q', 'r','s','t', 'v', 'x')
    PA=('B','C','D','G','H', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S','T', 'V', 'X')
    count_number= 0
    count_pa= 0
    count_na= 0
    count_alpha=0
    count_upper = 0
    count_lower = 0
    kt = 0
    sub= ' '
    NA= ('a','e','i','o','u','A','E','I','O','U')
    for i in str:
        if i.isupper():
            count_upper +=1
        elif i.islower():
            count_lower +=1
        elif i.count(sub):
            kt +=1
        elif i.isdigit():
            count_number += 1
        else :
            count_alpha +=1
        if i in NA :
            count_na +=1
        if i in pa and PA :
            count_pa +=1
    print("Số lượng kí tự in hoa:",count_upper,"kí tự")
    print("số lượng kí tự in thường:",count_lower,"kí tự")
    print("số lượng chữ số :",count_number,"kí tự")
    print("số lượng kí tự đặc biệt: ",count_alpha,"kí tự")
    print("số lượng khoảng trắng:",kt,"kí tự")
    print("số lượng nguyên âm:",count_na,"kí tự")
    print("số lượng phụ âm:",count_pa,"kí tự")
#bai5
import re
def nnis():
    str = input("Nhap chuoi ki tu")
    re_str = [int(d) for d in re.findall(r'-?\d+', str)]
    for i in range(0, len(re_str)):
        re_str[i] = int(re_str[i])
        if re_str[i] < 0:
            print(re_str[i])
        else:
            pass
##################################
#bài thực hành 7
#bai1
# Hàm 'sochan' có đầu vào là chuỗi số S, thực hiện tìm các số có 1 chữ số liên tiếp
# sao cho số tìm được là số chẵn. Kết quả trả về là danh sách các số chẵn liên tiếp tìm được
import re
def tachso():
    s = "1341512312412414214453498787332"
    tachso = re.findall('\d{1}' ,s)
    lst = []
    for i in range (0,len(s)):
        tachso[i]=int(tachso[i])
        if tachso[i] % 2 == 0:
            lst.append(tachso[i])
    print(lst ,end=' ')

#câu 2
# Hàm 'sapxep' có tham số đầu vào là chuỗi S, thực hiện sắp xếp các số có trong chuỗi số sao cho
# thứ tự các số trong chuỗi được xếp theo thứ tự từ nhỏ đến lơn. Kết quả trả về là một chuỗi số
# có thứ tự đã được sắp xếp
def num_sort():
    s = "1341512312412414214453498787332"
    a = list (s)
    a1= sorted(a)
    for i in a1 :
        print (i,end =' ')
        
# câu 3
# Hàm 'tachso' có tham số đầu vào là chuỗi S, thực hiện tách chuỗi S thành các số có 5 chữ số liên tiếp
# trong các số vừa tách được, có bao nhiêu số chia hết cho 5. Kết quả trả về của hàm là danh sách các số
# có 5 chữ số tìm được, danh sách các số chia hết cho 5
def bt3():
    s = "1341512312412414214453498787332"
    re_s = re.findall('\d{5}',s)
    print ("danh sách số đã tách :",re_s)
    for i in range(0,len(re_s)):
        re_s[i]=int(re_s[i])
        if re_s[i] % 5 == 0:
            print("danh sách các số chia hết cho 5 ","[",re_s[i],"]")
        else :
            print ("danh sách các số không chia hết cho 5 ","[",re_s[i],"]")

# BÀI 4 # Hàm 'sogiongnhau' có tham số đầu vào là chuỗi S, thực hiện tạo tất cả các số có 3 chữ số có
# mà bạn có thể tạo được từ chuỗi S, có bao nhiêu số có ít nhất 2 số giống nhau trong các số bạn
# vừa tạo. Kết quả trả về của hàm là danh sách các số có 3 chữ số được tạo, danh sách các số có
# ít nhất 2 số giống nhau trong dãy số vừa tạo S = "1341512312412414214453498787332"

 # Thực thi hàm 'tachso' so, capso = sogiongnhau(S) print("Danh sách các số có 3 chữ số tách được từ chuỗi: ", so) print("Danh sách các số giống nhau: ", capso) # Kết quả thu được khi thực thi hàm 'tachso' là: # Danh sách các số có 3 chữ số tách được từ chuỗi: [134, 341, 415, 151, # 512, 123, 231, 312, 124, 241, 412, 124, 241, 414, 142, 421, 214, 144, # 445, 453, 534, 349, 498, 987, 878, 787, 873, 733] # Danh sách các số giống nhau: [124, 241]
import collections
def bai4():
    s = "1341512312412414214453498787332"
    i=0
    lst = []
    for i in range (0,len(s)-3):
        s1 = s[i:i+3]
        lst.append(s1)
        i += 1
    print ("danh sách mảng đã cắt:",lst)
    print("danh sách các số trùng nhau trong mảng :",[k for k, v in collections.Counter(lst).items() if v > 1])

#################################
#bài thực hành 8
#bai1
N = [1, 4, 14, 15, 32, 15, 90, 54, 78, 32, 23, 56, 19]
def sapxep():
  lstsc= []
  lstsl=[]
  for i in range (len(N)):
    if N[i] % 2 == 0 :
      lstsc.append(N[i])
    else :
      lstsl.append(N[i])
  print(sorted(lstsl)+sorted(lstsc))
sapxep()



#bai2
def chenso():
    lst_chen = []
    for i in range (len(N)):
      if N.count(N[i]) == 1 :
        lst_chen.append(N[i])
        lst_chen.append(N[i])
      else :
        lst_chen.append(N[i])
    print(lst_chen)
#bai3
def uocsosx():
  for i in range (0,len(N)-1,2): #star end step
    a = N[i]
    b= N[i+1]
    def USCLN(a,b):
      r = a % b
      while r != 0:
          a = b
          b = r
          r = a % b
      return b
    print("uoc so chung lon nhat cua",a,"va",b,":",USCLN(a,b))
#CACH2
def uocsosx2():
  for i in range (0,len(N)-1,2):
    print("uoc so chung lon nhat cua",N[i],"va",N[i+1],":",math.gcd(N[i],N[i+1]))

##########################
#bài thực hành trên lớp
#vong lap
import math
def s():
  a=int(input("Nhập giá trị A="))
  b=int(input("Nhập giá trị B="))
  c=int(input("Nhập giá trị C="))
  r=int(input("Nhập giá trị r="))
  s = math.pi*r*r
  while True :
    r= r*a
    r=r//b
    s += s
    if r < 1 :
      break
    else :
      s += s
  print(s)
#bai 2

def taosoao():
  N=input("Nhap gia tri n :")
  def taoso (N):
    chuoi =['0','1','2','3','4','5','6','7','8','9']
    lst= []
    N_ = str(N)
    for i in range (len(N)+1):
      for j in chuoi:
        if i == 0 :
          new_str = j+N_
          lst.append(int(new_str))
        elif i == len(N_):
          new_str =N + j
          lst.append(int(new_str))
        else :
          new_str= N_[:i]+ j + N_[i:]
          lst.append(int(new_str))
    return lst
  def timboso(lst):
    lst_bs=[]
    for i in lst:
      if i % 9 == 0:
        lst_bs.append(i)
    return lst_bs
  def timmin(lst):
    return min(lst)
  print(timmin(timboso(taoso(N))))

#random tim 4
import random
def random():
  n =int(input(" nhập số < 1000 :"))
  print(n)
  while True:
    a= random.randint(1,n)
    b= n-a
    if "4" not in str(a) and "4" not in str(b):
      print(a,b)
      break
#tìm số kẹo
#bai toan tinh so keo
def sokeo():
  n=int(input("nhập số túi kẹo"))
  m=int(input("nhập số người nhận"))
  lst = [ ]
  tongsokeo = 0
  for i in range (n):
    i = int(input("nhập số kẹo mỗi túi "))
    lst.append(i)
    tongsokeo = tongsokeo + i
  print("số kẹo trong mỗi túi:",lst)
  print ("số kẹo mỗi người nhận được ", tongsokeo // m )
  print ("số kẹo còn dư lại ",tongsokeo % m )















