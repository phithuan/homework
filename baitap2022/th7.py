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
bt3()

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
    print ("danh sách mảng đã cắt:",lst)
    print("danh sách các số trùng nhau trong mảng :",[k for k, v in collections.Counter(lst).items() if v > 1])


