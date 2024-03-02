import pandas as pd
f= open("studen.txt","a",encoding="utf-8")
while True:
    MSV= input("mã số sinh viên: ")
    ten= input("tên sinh viên: ")
    lop= input("lớp: ")
    Que= input("Quê quán: ")
    f.write("\t". join([MSV, ten, lop, Que]) +"\n" )#\t bằng 4 dấu cách  và \n là xuống dòng

    close = input("BẠN MUỐN TIẾP TỤC NHẬP:(NẾU MUỐN NHẮN K ĐỂ THOÁT) ")
    if close=="k":
        break
f.close()

f="studen.txt"
sv= pd.read_csv(f, sep="\t", names=["mã SV","tên","lớp","quê"])
print(sv)