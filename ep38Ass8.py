#Ass รับค่าและเรียงลำดับข้อมูล
# .sort
# reverse

number = []

while True :
    x = int(input("ป้อนตัวเลขของคุณ :"))
    if x < 0 :
        break
    number.append(x)

print("ก่อนเรียง",number)
number.sort() 
print("น้อยไปมากเรียง",number)
number.reverse()
print("มากไปน้อยเรียง",number) 
print("จบโปรแแกรม")