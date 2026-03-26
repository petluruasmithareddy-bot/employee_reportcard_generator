def add(a,b):
    return a+b 
def sub (a,b):
    return a-b
def mul(a,b):
    return a*b
def div (a,b):
    if b==0:
        return 'zero division error'
    else:
        return a/b
print("calculator")
choice=input("enter your choice:1/2/3/4 : ")
x=int(input("enter your first number:"))
y=int(input("enter your second number:"))

if choice=="1":
    print(x,"+",y,"=",add(x,y))
elif choice =="2":
    print(x,"-",y,"=",sub(x,y))
elif choice=="3":
    print(x,"*",y,"=",mul(x,y))
elif choice=="4":
    print(x,"//",y,"=",div(x,y))
else:
    print("wrong choice")