# ตารางหมากฮอต

num = int(input("ป้อนขนาด  : "))

for row in range(num) :

    for col in range(num) :
        if (row+col) % 2 == 0 :
            print("o",end=" ")
        else :
            print("x",end=" ")
    print(" ")
