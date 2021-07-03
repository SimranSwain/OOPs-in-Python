def calculate(a,b):
    #return a//b,"\n", a+b,"\n", a/b,"\n", a % b
    return f"here the  answers are:\n {a//b} \n {a+b} \n {a/b}\n {a % b}"

def main():
    x,y=map(int,input().split())
    x=calculate(x,y)              # As calculate function takes argument
    print(x)

if __name__=="__main__":
    main()


