import sys
b = int(sys.argv[1])
a = b+1
def rev_diamond():
    global a
    a +=1
    if a==b:
        print(" " * (a - 1), "*" * (b - a) + "*" + "*" * (b - a), " " * (a - 1))
        return
    else:
        print(" "*(a-1),"*"*(b-a)+"*"+"*"*(b-a)," "*(a-1))
        rev_diamond()
def diamond():
    global a
    a-=1
    if b ==1:
        print("*")
    else:
        if a == 0:
            a+=1
            rev_diamond()
        else:
            print(" "*(a-1),"*"*(b-a)+"*"+"*"*(b-a)," "*(a-1))
            diamond()
diamond()