print(23)
print(35+23)
name="Vipul Yadav"
age=19
price=69.00

print(name)
print(age)
print(price)
print("my name is :", name)
print("my age is :", age)
print("the price of mac is:", price)


print(type(name))
print(type(age))
print(type(price))

old=False
a=None

print(type(old))
print(type(a))

a=3
b=4
sum=a+b
print(sum)
txt= "a"
print(2*txt*3)
print(a*txt*b)
text="@"

print(2*text*3)
a="50"
b=52

print((a+text)*b)
a=20
b,c=30,40
print(a+b*c)

d=3.0
e=a*d
print(e)

print(a/b)

f=a//c
print(f,a/c)

x=-5
y=2
print(x%y)
z=-2
h=5
print(h%z)

#print("hello")
print("world")

"""this is 
a multiline
comment"""



Name= input("Name :")
Age= int(input("Age :"))
Price= float(input("Price :"))

print("my name is ",Name, "and i am ", Age,"years old")
def even_count(n):
    
    if n<2:
        return 0
        
    else:
        return n//2
n=int(input())
result=even_count(n)
print(result)