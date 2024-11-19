#1st question

first= int(input("first number:"))
second= int(input("second number"))

sum= first+second
print(sum)

#2nd question

side = int(input("side:"))
print("area=", side * side )

#3rd question
firstfloat=float(input("enter firstfloat"))
secondfloat=float(input("enter secondfloat"))

print("average", firstfloat+secondfloat)

#4th question
a= int(input("enter a:"))
b= int(input("enter b:"))
result ="True" if a>=b else "False"
print(result)
def even_count(n):
    
    if n<2:
        return 0
        
    else:
        return n//2
n=int(input())
result=even_count(n)
print(result)
def swap_without_third_var(a,b):

    a = a + b
    b = a - b
    a = a - b
    return a,b
result=swap_without_third_var(5,10)
print(result)
def swap_without_third_var(a,b):

    a = a + b
    b = a - b
    a = a - b
    return a,b
a,b=map(int,input().split(','))
result=swap_without_third_var(a,b)
print(result)