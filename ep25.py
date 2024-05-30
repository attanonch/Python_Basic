#ทำซ้ำ ไม่รู้จำนวนที่แน่นอน

'''
 while expression :
    statement
'''
i = 1
result = 0
avg = 0

# while i<=3 :
#     print("รอบที่ ",i)
#     i +=1 
# print("จบโปรแกรม")

count = int(input("ระบุรอบ "))
while i<=count :
    result +=i
    ava = result/i
    print("รอบที่", i ,"ค่าผลลัพธ์ คือ",result,"ค่าเฉลี่ย คือ ",ava)
    i += 1
avg = result/count   
print("เฉลี่ย ", avg)   
print("ผลรวมคือ ", result)


#for รู้จำนวนที่แน่นอน

# for i in range(start,stop-1,step)
# for i in range(0,10,2): #range เริ่มที่ 0 จำนวนรอบ

# sum = 0
# ava = 0

# for i in range(10,0,-1): #range เริ่มที่ 0 จำนวนรอบ
#     sum = sum + i
#     print("รอบที่ ",i,"ผลรวม", sum)
  
  