#ค้นหามากสุด น้อยสุด
max,min =0,999
while True :
    num = int(input("กรอกเลข :"))
    if  num < 0 :
        break
    if num > max :
        max = num
    if num < min :
        min = num 
    print("ค่าที่มากที่สุด : ",max)
    print("ค่าที่น้อยที่สุด : ",min)