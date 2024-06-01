#lambda function ฟังชันที่ไม่มีชื่อ



'''
lambda argument : expression

'''
# x = lambda name : name
# add = lambda x,y : x+y

# print(x(name="attanon"))
# print(add(5,7))


def pow(number) :
    return lambda a:number**a

x = pow(5)
Result = x(2)
print(Result)

