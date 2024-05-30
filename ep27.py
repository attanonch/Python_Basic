#สูตรคุณ

# num = int(input("ระบุแม่เลข : "))

# for i in range(1,13) :
#     result = num*i
#     print("สูตรคุณแม่",num,"ผลลัพธ์",num,"*",i,"=",result)

start = int(input("แม่สูตรคูณเริ่มต้น :"))
stop = int(input("แม่สูตรคูณสุดท้าย :"))


for x in range(start,stop+1) :
    print("สูตรคูณแม่ ",x)
    for i in range(1,13) :
        result = x*i
        print("สูตรคุณแม่ ",x ,"ผลลัพธ์",x ,"*",i,"=",result,)

result = 0
# for x in range(2,4) :
#     print("แม่",x)
#     for i in range(1,13):
#         result = x*i
#         print("สูตรคุณแม่",x,"ผลลัพธ์",x,"*",i,"=",result)