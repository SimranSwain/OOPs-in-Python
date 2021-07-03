def swap(p,q):             # We have swap the total list.
    temp = p
    p = q
    q = temp         
    print(p,q)
    print(p[0],q[0])

def main():
    a,b=map(int,input().split())
    x=[0] * 1
    y=[0] * 1
    x[0]=a
    y[0]=b
    swap(x, y)
    print(x, y)


if __name__=="__main__":
    main()

# #-----------------------------------------------------------------------------------------------------------


# x=[5]*2+[6]*1+[9]*3
#  print(x)
#  x.insert(4,8)          #(index position,value)
# print(x)


# # print("-----------------------------------------------------------------------------------------------------------------")


# def swap(p, q):                      # Elements of the list is swaped
#     temp = p[0]
#     p[0] = q[0]
#     q[0] = temp
#     print(p, q)
#     print(p[0], q[0])


# def main():
#     a, b = map(int, input().split())
#     x = [0] * 1
#     y = [0] * 1
#     x[0] = a
#     y[0] = b
#     swap(x, y)
#     print(x ,y)
#   #  print(x[0], y[0])

# if __name__ == "__main__":
#         main()

