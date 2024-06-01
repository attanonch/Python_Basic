
def sumation(number) :
    sum,avg = 0,0
    for item in number :
        sum += item
        avg = sum/len(number)
    return sum,avg



x = [1,2,3,4,5,6,7,8,9,10]
print(sumation(x))