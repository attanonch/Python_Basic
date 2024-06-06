import random

x = random.random() #
i = 0

items = [1,2,3,4,5,6,"a","B","v"]
while i in range(9):
    # x = random.random()
    # x = random.uniform(-5,10)
    # x = random.randint(-5,10)
    # x = random.randrange(1,10,2) #2 สุ่มที่ละ 2 ครั้งฝ
    # if x == 9 :
    #     print("ได้  = ",x)
    #     break
    # x = random.choice(items)
    random.shuffle(items)
    print(items)
    i+=1
