# def swap(x,y):
#     temp = x
#     x = y
#     y = temp
#     print(x, y)

# def main():
#     a,b=map(int, input().split())
#     swap(a,b) 


#     print(a,b)           # No Reflection


# if __name__=="__main__":
#     main()

# print("----------------------------------------------------------------------------------------------------------")


def swap(x,y,z):
    temp=x
    x=y
    y=z
    z=temp
    print(x,y,z)

def main():
    a,b,c=map(int,input().split())
    swap(a,b,c)


if __name__=="__main__":
    main()
