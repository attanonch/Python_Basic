# **kwargs ข้อมูลเป็นแบบ dictionary
# * agrs ข้อมูลแบบ tuple
def add(*num):
    sum = 0
    for item in num :
        sum += item
    print(sum)

def display(**data):
    print(data)

add(50,10)
display(fname="attanon",lname="chupool",status=True)