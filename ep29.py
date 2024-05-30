start,stop = 1,5 

result = 0
avg =  0
while (start <= stop) :
    num=int(input("ตัวเลข : "))


    result += num 
    avg = result/stop
    start += 1

print("result : ",result)
print("avg : ",avg)
