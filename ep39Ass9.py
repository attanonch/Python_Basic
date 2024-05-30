#หา min max sum

num = []
x = int(input("ป้อนค่า :"))

while True :
    x = int(input("ป้อนค่า :"))
    if x < 0 :
        break
    num.append(x)

print(num)

print("ค่าน้อยที่สุด",min(num))
print("ค่ามากที่สุด",max(num))
print("ผลรวม",sum(num))
