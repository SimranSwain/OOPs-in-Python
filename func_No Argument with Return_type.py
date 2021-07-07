# def addition():
#     a,b=map(int,input().split())
#     return a+b

# def main():
#     x=addition()        # we have to store the return value in a variable and can print that variable.
#     print(x)

#     print(type)
#     print(type(x))

# if __name__=="__main__":
#     main()

# print("--------------------------------------------------------------")


def addition():
    sum=0
    a=list(map(int,input().split()))
    for i in range (len(a)):
        sum=sum+a[i]
    return sum

def main():
    x=addition()
    print(x)
    print(type)
    print(type(x))

if __name__=="__main__":
    main()