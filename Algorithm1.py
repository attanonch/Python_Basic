def wordcut():
    inputword = input("กรอกข้อมูล : ")
    num = int(inputword[-1]) #คำที่จะตัด
    word = inputword[:-2]  #คำล้วน
    # print(word)
    # print(num)
    i = 0
    while i < len(word) :
        print(word[i:i+num])
        i+= num

wordcut()