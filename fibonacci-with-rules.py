"""fibonacci number is the number defined by the following rules
(1)its the sum of largest three consecutive even numbers if the target limit is odd
(2)its the sum of largest three consecutive odd numbers if the target limit is even
(3)if the target number is odd prime number then fibonacci number is the sum of all prime numbers which is
less than the reminder of target limit divided by 3"""

def start(sum,c):
    num=int(input("enter the number: "))
    if is_even(num):
        for i in range(num,1,-1):
            if is_odd(i):
                sum+=i
                c+=1
                if c==3:
                    break
        print("the entered number {} is an even number and its fibonacci is {}".format(num,sum))

    elif is_odd(num) and not isprime(num):
        for i in range(num,1,-1):
            if is_even(i):
                sum+=i
                c+=1
                if c==3:
                    break
        print("the entered number {} is an odd number and its fibonacci is {}".format(num,sum))

    elif isprime(num) and num!=2:
        remainder=num%3
        if remainder>2:
            for i in range(2,remainder):
                if isprime(i):
                    print(i)
                    sum+=i
            print("the entered number {} is an odd prime number and its fibonacci is {}".format(num,sum))
        else:
            print("sum is 0 since no prime number exists below 2")

def isprime(num):
    for i in range(2,num):
        if num%i==0:
            break
    else:
        return num

def is_even(num):
    if num%2==0:
        return num

def is_odd(num):
    if (num%2)!=0:
        return num

start(0,0)
