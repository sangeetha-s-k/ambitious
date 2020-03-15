def kangaroo(kangaroo=[[],[]]):
    for i in range(0,2):
        location=int(input("enter the start location of kangaroo: "))
        jump=int(input("enter the jump distance of kangaroo: "))
        kangaroo[i].append(location)
        kangaroo[i].append(jump)
    if sum(kangaroo[0])==sum(kangaroo[1]):
        print("yes,both kangaroos reach the same position at the same time")
    else:
        print("No,both kangaroos don't reach the same position at the same time")
kangaroo()
