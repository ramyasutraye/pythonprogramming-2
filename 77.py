num=int(raw_input(""))
count=0
if num>0:
    for i in range(1,num+1):
        if num%i==0:
            print i,
