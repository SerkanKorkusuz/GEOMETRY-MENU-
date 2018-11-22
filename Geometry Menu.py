author = "serkan korkusuz"

from math import sqrt, fabs, pi

print("""*********************
*                   *
*GEOMETRY MENU      *
*1.Triangle         *
*2.Ouadrilateral    *
*3.Ellipse          *
*4.Exit             *
*********************
**
Enter choice: """)

def myfunction():
 user_choice=int(input())
 tf=True
 if user_choice not in [1,2,3,4]:
    print("Your choice is inappopriate. Please enter your choice again.")
    myfunction()
    
 elif user_choice==1:
   while tf:
    print("Enter x1, y1, x2, y2, x3, y3 of Triangle : ")
    triangle=[float(x) for x in input().split()]
    x1=triangle[0]
    y1=triangle[1]
    x2=triangle[2]
    y2=triangle[3]
    x3=triangle[4]
    y3=triangle[5]
    a=sqrt(((x1-x2)**2)+((y1-y2)**2))
    b=sqrt(((x2-x3)**2)+((y2-y3)**2))
    c=sqrt(((x1-x3)**2)+((y1-y3)**2))
    print("Edge Lengths: a="+str(a)+"  b="+str(b)+"  c="+str(c))
    if fabs(a-b)>=c or (a+b)<=c or fabs(a-c)>=b or (a+c)<=b or fabs(c-b)>=a or (c+b)<=a:
        print("TRIANGLE TYPE: Invalid")
        break
    elif (a==b and a!=c) or (a==c and a!=b) or (c==b and b!=a):
        print("TRIANGLE TYPE: Isoscales")
    elif a!=b and a!=c and b!=c:
        print("TRIANGLE TYPE: Scalene")
    elif (a**a+b**b==c**c) or (a**a+c**c==b**b) or (c**c+b**b==a**a):
        print("TRIANGLE TYPE: Right")
    elif a==b and b==c:
        print("TRIANGLE TYPE: Regular")
    print("Center coordinates (Cx, Cy): "+str((x1+x2+x3)/3)+", "+str((y1+y2+y3)/3))
    s=(a+b+c)/2
    print("Area: "+str(sqrt(s*fabs((s-a))*fabs((s-b))*fabs((s-c)))))
    print("Circumference: "+str(a+b+c))
    break
   myfunction()
   
 elif user_choice==2:
    print("Enter a, b, h of Quadrilateral : ")
    quadrilateral=[float(x) for x in input().split()]
    a=quadrilateral[0]
    b=quadrilateral[1]
    h=quadrilateral[2]
    print("Area: "+str((a+b)*h/2))
    print("Circumference: "+str(a+b+2*sqrt(h**2+(b-a)**2)))
    myfunction()
   
 elif user_choice==3:
    print("Enter r1, r2 of Ellipse : ")
    ellipse=[float(x) for x in input().split()]
    r1=ellipse[0]
    r2=ellipse[1]
    print("Area: "+str(pi*r1*r2))
    print("Circumference: "+str(pi*(1.5*(r1+r2)-sqrt(r1*r2))))
    myfunction()

 elif user_choice==4:
    print("Program finished.. ")
    tf=False
 
myfunction()
