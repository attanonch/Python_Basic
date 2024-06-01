#factorail
def factorail(number) :
    if number == 1 :
        return number
    else : 
        return  number*factorail(number-1)


print(factorail(5))