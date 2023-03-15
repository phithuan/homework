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
	return uocso

#bai4
def tong(a=7):
		b = int(input())
		c = int(input())
		return a+ b +c

#bai5
def ngto():
n = int(input("nhâp số:"))

if n<2:
    print("không phải là số nguyên tố")
else:
    for i in range(2,n//2):
        if n%i==0:
            print(n," không phải là số nguyên tố")
            break
    else:
        print("là số nguyên tố",n)

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
n = 3
thaphanoi(n, "A", "B","C")



