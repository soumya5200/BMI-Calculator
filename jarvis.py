m1 = int(input("enter marks 1"))
m2 = int(input("enter marks 2"))
m3= int(input("enter marks 3"))
m4 = int(input("enter marks 4"))
total= (m1 + m2+ m3 + m4)
per = total/4
if (m1<40,m2<40,m3<40,m4<40):

    print("fail")
    print("with held")
else:
    print("pass")
    if (per>90):
        print("grade a")
    elif(per>80):
        print("grade b") 
    elif(per>70,m3<80):
        print("grade c")
    else:
        print("d")           



























