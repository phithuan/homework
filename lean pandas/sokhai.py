f= open("studen.txt","a",encoding="utf-8")
while True:
    MSV= input("mã số sinh viên: ")
    ten= input("tên sinh viên: ")
    lop= input("lớp: ")
    Que= input("Quê quán: ")
    f.write("\t". join([MSV, ten, lop, Que]) +"\n" )#\t bằng 4 dấu cách  và \n là xuống dòng

    cl = input("BẠN MUỐN TIẾP TỤC NHẬP:(NẾU MUỐN NHẮN K ĐỂ THOÁT) ")
    if cl=="k":
        break
f.close()

f=open("studen.txt","r",encoding="utf-8")
print("\t".join(["mã sinh viên", "tên", "lớp", "quê"]))
for sv in f.readlines():
    print(sv.replace("\n",""))
f.close()