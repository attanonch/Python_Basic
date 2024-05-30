#ตัวเลขขั้นบันได

'''
4

1
12
123
1234

'''
num = int(input("กรุณากรอกเลข : "))

for row in range(1,num+1) :
    for col in range(1,row+1) :
        print(col,end='')
    print(" ")

