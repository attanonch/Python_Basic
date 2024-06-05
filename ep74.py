'''
mode 
r = read
w = เขียนไฟล์ ลบไฟล์เดิม
a = เขียนข้อมูลไปต่อ
การลบข้อมูล
'''
import os
# try :
#     fw = open("ep74.txt","r",encoding="utf-8")
#     # fw.write("Hello World\n")
#     # fw.writelines("สวัสดีชาวโลก")
#     line=fw.readlines()
#     for world in line :
#         print("=>",world)
#     # print(fw.readlin())
#     fw = open("ep74.txt","a",encoding="utf-8")
#     fw.writelines("\nสวัสดีวันจันทร์")
#     fw.close()
# except FileNotFoundError:
#     print("หาไฟล์ไม่เจอ")

# try :
#     fw = open("ep74.txt","+r",encoding="utf8")
#     print(fw.read())
#     fw = open("ep74.txt","+a",encoding="utf8")
#     for i in range(3) :
#         name = input("ระบุชื่อ : ")
#         fw.writelines(name+"\n") 
#     fw.close()
#     fw.close()

# except FileExistsError:
#     print("หาไฟล์ไม่เจอ")


try :
    if os.path.exists("test.py"):
        os.remove("test.py")
        print("ลบไฟล์แล้ว")
    else :
        print("ไม่พบไฟล์")
    
except Exception as e:
    print(e)