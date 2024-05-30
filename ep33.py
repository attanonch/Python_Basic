#สร้างภาพสี่เหลี่ยมจัตตุรัส

'''
xxx
xxx
xxx

xxxxx
xxxxx
xxxxx
xxxxx
xxxxx

'''


num = int(input("ป้อนขนาด  : "))

for row in range(1,num+1) :
    for col in range(1,num+1) :
        print("x",end=" ")
    print(" ")
