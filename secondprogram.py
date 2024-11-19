Name= input("Name :")
Age= int(input("Age :"))
Price= float(input("Price :"))

print("my name is ",Name, "and i am ", Age,"years old")


light= input("light:")
if(light=="red"):
    print("stop")
elif(light=="yellow"):
    print("look")
elif(light=="green"):
    print("go")
else:
    print("light is broken")

food=input("food:")
eat="yes" if food== "cake"else "no"
print(eat)

traffic=input("traffic:")
way="right"if traffic== "light"else "left"
print(way)

dessert=input("dessert:")
print("sweet") if dessert=="rasgula" or dessert=="jalebi" else print ("not sweet")


p=int(input("p:"))
r=int(input("r:"))
t=int(input("t:"))

SI=(p*r*t)/100
print (SI)

v=50
i=54
print(not v<i)
n= int(input("Enter year"))
if(n%4==0):
    print("YES")
else:
    print("NO")