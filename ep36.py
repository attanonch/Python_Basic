#เกมทายลูกเต๋า
#1,2,3,4,5,6

import random 
#สุมเลขลูกเต๋า
myrandom = random.randrange(1,7) #1-9

print(myrandom)
 
k=1
while True :
    num = int(input("ป้อนคำตอบ : "))
    if num <0 or k == 3 :
        break
    correct = (num==myrandom)

    if correct :
        print("ถูกต้อง")
        break
    if not correct :
        if num > myrandom:
            print("ต้องระบุค่าน้อยกว่า")
            print("ผิด")
        else : 
            print("ผิด")
            print("ต้องระบุค่ามากกว่า")
    k+=1

if not correct :
    print("เสียใจด้วย")
print("เฉลย :", myrandom)
