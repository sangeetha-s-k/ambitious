def kangaroo(kangaroo=[[],[]]):
    for i in range(0,2):
        location=int(input("enter the start location of kangaroo: "))
        jump=int(input("enter the jump distance of kangaroo: "))
        kangaroo[i].append(location)
        kangaroo[i].append(jump)
    if ((kangaroo[0][0]>kangaroo[1][0])and (kangaroo[0][1]>kangaroo[1][1]))or((kangaroo[0][0]<kangaroo[1][0]) and
    kangaroo[0][1]<kangaroo[1][1]):
        print("No,both kangaroos don't reach the same position at the same time")
    else:
        for i in range(0,10000):
            kangaroo[0][0]=kangaroo[0][0]+kangaroo[0][1]
            kangaroo[1][0]=kangaroo[1][0]+kangaroo[1][1]
            if sum(kangaroo[0])==sum(kangaroo[1]):
                print("Yes,both kangaroos reach the same position at the same time")
                break
        else:
            print("No,both kangaroos don't reach the same position at the same time")
kangaroo()

