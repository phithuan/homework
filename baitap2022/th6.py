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
nnis()






