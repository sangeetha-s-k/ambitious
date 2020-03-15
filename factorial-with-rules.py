"""WAP for factorial where factorial has following rules
(1)If number is prime then factorial is all multilication of numbers divisible by 3
(2)if number is even then factorial is all multiplication of number divisible by all prime number less than the no
(3)if number is odd and not prime then factorial is number multiplied by all number which is less than the number
itself except first 5 prime numbers"""


def start():
    num=int(input("enter the number: "))
    res=isprime(num)
    if res==False:
        prime_rule(num,1)
    elif res==True:
        if (num%2)!=0:
            odd_rule(num,0)

    if num%2==0:
        print("sk")
        even_rule(num)


def prime_rule(num,output):
    for i in range(1,num+1):
        if i%3==0:
            output=output*i
        else:
            continue
    print("the entered input number {} is prime and it's factorial is {}".format(num,output))

def even_rule(num):
    output=1
    prime_list=[]
    for i in range(2,num):
        x=isprime(i)
        if x==False:
            prime_list.append(i)
        else:
            continue
    for i in range(1,num):
        for j in prime_list:
            if i%j==0:
                #print(i,j)
                output=output*i
                break
            else:
                continue
    print("the entered input number {} is even and it's factorial is {}".format(num,output))

def odd_rule(num,counter):
    result=1
    for i in range(2,num):
        x=isprime(i)
        if x==False:
            counter=counter+1
            if counter<=5:
                continue
            else:
                result=result*i
    print("the entered input number {} is odd and it's factorial is {}".format(num,result))


def isprime(num):
    for i in range(2,num):
        if num%i==0:
            return True
    else:
        return False



start()
