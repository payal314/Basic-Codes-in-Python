#!/usr/bin/env python
# coding: utf-8

# # Assignment Submitted by: Payal Chaudhary

# # Part A

# # A1: Write a program that prints the next 20 leap year and sum of digits of leap year must be greater than 16 
# 

# In[1]:


# Function to check whether a year is leap year or not
# Function will return 1 for leap year and 0 for non leap year
def check_leap(ly):
    if ly%100==0 and ly%400==0:
        rly=1 # It is a leap year
    elif ly%100!=0 and ly%4==0:
        rly=1 # It is a leap year
    else:
        rly=0 # It is not a leap year
    return rly

# Function to check whether the sum of digits in a year is greater than 16 or not
# Function will return 1 if sum is greater than 16 else return 0 along with sum
def sum_check(scy, c=16): 
    sum = 0
    while scy>0: # Check if all digits are added
        sum+= (scy%10) #Adding Unit Digit to Sum
        scy = scy//10 # Deleting Unit Place
    if sum>c: # compare sum and c
        sc=1
    else:
        sc=0
    return sc, sum    

    
# Start of Main Function
m=1
while m==1:
    m=0
    print("Below Code will print the next 20 leap year and sum of digits of leap year must be greater than 16")
    print(" ")
    print("Enter your Choice: \n 1 for user defined base year, \n 0 for current year as base year. ")
    print("Choice: ", end="")

    ch=int(input()) # Take choice from user
    print("")
    if ch==1: 
        print("Enter base year: ",end="")
        y=int(input()) # Take base year from user
    elif ch==0:
        import datetime # Call datetime library
        now = datetime.datetime.now() # Get current date and time
        y= int(now.year)  # Take base year from now
    else:
        print("OOPS!!! Invalid Choice")

    print("-------------------------------------------------------------------------")
    print("")

    print("Base Year: ",y) # Show user base year
    n1 = 20
    c = 16
    n=0 # Counter to count number of leap year printed
    print("")
    print("Following is the list of ",n1," leap years whose sum of digits is greater than ",c)
    while n<n1: 
        y=y+1 # Increment year
        ry = check_leap(y) # Call a function to check whether the year is leap year or not
        if ry==1: # Check if ry = 1, it is a leap year
            sc, sum = sum_check(y) # Call a function to check sum of digits in a year
            if sc==1: # Check if sc = 1, sum >16
                print("Count = ",n+1,"\t : \t Leap Year = ",y) # Print count and year
                n=n+1 # Increment counter
    print("")
    print("")
    print("-------------------------------------------------------------------------")
    print("")
    print("Would you like to retry for other input? (Yes/No): ", end="")
    m1 = input()
    if m1=="YES" or m1=="YEs" or m1=="YeS" or m1=="Yes" or m1=="yES" or m1=="yEs" or m1=="yeS" or m1=="yes" or m1=="Y" or m1=="y" or m1=='1':
        m=1
    else:
        print("Thank You")
    print("")
    print("-------------------------------------------------------------------------")

# End of code


# # A2: Design a user interactive Calculator .( sum , subtraction , multiplication , division , Distance , speed , Intrest)

# In[2]:


def sum(a,b):
    c=a+b
    return c

def sub(a,b):
    c=a-b
    return c

def mul(a,b):
    c=a*b
    return c

def div(a,b):
    c=a/b
    return c

def dis(a,b):
    c=((a[0]-a[1])**2+(b[0]-b[1])**2)**0.5
    return c

def sp(a,b):
    c=a/b
    return c

def si(a,b,c):
    d=a*b*c/100
    return d

def ci(a,b,c):
    d=a*((1+b/100)**c-1)
    return d

# Start of Main Function
m=1
while m==1:
    m=0
    print("Enter Your Choice: ")
    print("1.Addition \n2.Subtraction \n3.Multiplication \n4.Division \n5.Distance \n6.Speed\n7.Interest")

    print("------------------------------------------------------------------------------------------------")
    ch=int(input("Your choice is "))
    print("")
    if ch==1:
        a=int(input("Enter Value of a: "))
        b=int(input("Enter Value of b: "))
        print(" ")
        c=sum(a,b)
        print("The sum of", a,"and", b," is ",c)
        print("")
        print("------------------------------------------------------------------------------------------------")
        print("")
        
    elif ch==2:
        a=int(input("Enter Value of a: "))
        b=int(input("Enter Value of b: "))
        print(" ")
        c=sub(a,b)
        print("The Difference of", a,"and", b," is ",c)
        print("")
        print("------------------------------------------------------------------------------------------------")
        print(" ")
        
    elif ch==3:
        a=int(input("Enter Value of a: "))
        b=int(input("Enter Value of b: "))
        print(" ")
        c=mul(a,b)
        print("The Product of", a,"and", b," is ",c)
        print("")
        print("------------------------------------------------------------------------------------------------")
        print(" ")
        
    elif ch==4:
        a=int(input("Enter Value of a: "))
        b=int(input("Enter Value of b: "))
        print(" ")
        c=div(a,b)
        print("The Divison of", a,"and", b," is ",c)
        print("")
        print("------------------------------------------------------------------------------------------------")
        print(" ")
        
    elif ch==5:
        a,b=[0,0],[0,0]
        a[0]=int(input("Enter value of x co-ordinate :"))
        a[1]=int(input("Enter value of y co-ordinate :"))
        b[0]=int(input("Enter value of x co-ordinate :"))
        b[1]=int(input("Enter value of y co-ordinate :"))
        print(" ")
        c=dis(a,b)
        print("The Distance between",a,"and",b,"is",c)
        print("")
        print("------------------------------------------------------------------------------------------------")
        print("")
        
    elif ch==6:
        a=int(input("Enter Value of Distance:"))
        b=int(input("Enter Time:"))
        print(" ")
        c=sp(a,b)
        print("The Speed of",a,"and",b,"is",c)
        print("")
        print("------------------------------------------------------------------------------------------------")
        print("")
        
    elif ch==7:
        print("Enter Your Choice: ")
        print("a.Simple Interest\nb.Compound Interest\n")
        print("Your choice is ",end=" ")
        print(" ")
        choice=input()
        if choice=='a':
            print("For Finding Simple Interest:")
            a=int(input("Enter Principal Value:"))
            b=int(input("Enter Rate of Interest:"))
            c=int(input("Enter Number of years:"))
            d=si(a,b,c)
            print("The Simple Interest is ",d)
            print("")
            print("------------------------------------------------------------------------------------------------")
            print("")
        elif choice=='b':
            print("For Finding Compound Interest:")
            a=int(input("Enter Principal Value:"))
            b=int(input("Enter Rate of Interest:"))
            c=int(input("Enter Number of years:"))
            d=ci(a,b,c)
            print("The Compound Interest is ",d)
            print("")
            print("------------------------------------------------------------------------------------------------")
            print("")
        else:
            print("Invalid Choice!!!")
    else:
        print("Invalid Choice!!!")
    print("")
    print("------------------------------------------------------------------------------------------------")
    print("")
    print("Would you like to retry for other input? (Yes/No): ", end="")
    m1 = input()
    if m1=="YES" or m1=="YEs" or m1=="YeS" or m1=="Yes" or m1=="yES" or m1=="yEs" or m1=="yeS" or m1=="yes" or m1=="Y" or m1=="y" or m1=='1':
        m=1
    else:
        print("Thank You")
    print("")
    print("------------------------------------------------------------------------------------------------")
        
# End of Code


# # A3: The game is that the computer "thinks" about a number and we have to guess it. On every guess, the computer will tell us if our guess was smaller or bigger than the hidden number. The game ends when we find the number.Also Define no of attemps took to find this hidden number.(Hidden number lies between 0 - 100)

# In[3]:


from random import randint

m=1
while m==1:
    m=0
    print("-------------------------------------------------------------")
    print("")
    print("Let Begin the Game of Guessing the Number")
    a=0
    b=100
    x = randint(a, b)
#    print(x)
    n = int(input("Number of Guesses you are going to try:"))

    for i in range(n):
        print("")
        print("-------------------------------------------------------------")
        print("")
        print("Number of Remaining Attempts left:",n-i)
        print("Hint: ",a,"< x <",b)
        y=int(input("Your Guess:"))
    
        if x==y:
            print("Hurrah!! You Guess the correct Number")
            print("")
            print("-------------------------------------------------------------")
            print("")
            break
        elif x>y:
            print("The Number is Bigger than Ur Guess")
            a=y
        elif x<y:
            print("The Number is Smallar than Ur Guess")
            b=y
        if i==n-1:
            print("-------------------------------------------------------------")
            print("")
            print("OOPS!! No More Chance Left")
            print("Correct Number:",x)
            print("Better Luck Next Time!!!")
            print("")
            print("-------------------------------------------------------------")
            print("")
    print("Would you like to Play again? (Yes/No): ", end="")
    m1 = input()
    if m1=="YES" or m1=="YEs" or m1=="YeS" or m1=="Yes" or m1=="yES" or m1=="yEs" or m1=="yeS" or m1=="yes" or m1=="Y" or m1=="y" or m1=='1':
        m=1
    else:
        print("Thank You")
    print("")
    print("-------------------------------------------------------------")
            
    
        


# # A4: Write a Python program to calculate sum and product of digits of a number.(Create Two different funtions one for sum and one product.)

# In[4]:


def sum_digits(d):
    Sum=0
    while d>0:
        Sum+=(d%10)
        d=d//10
    return Sum

def product_digits(d):
    Product=1
    while d>1:
        Product*=(d%10)
        d=d//10
    return Product

m=1
while m==1:
    m=0
    x=int(input("Enter a Number:"))
    s=sum_digits(x)
    print("Sum of Digits in the Number",x,"is",s)
    p=product_digits(x)
    print("Product of Digits in the Number",x,"is",p)
    print("")
    print("-------------------------------------------------------------")
    print("")
    print("Would you like to Try again? (Yes/No): ", end="")
    m1 = input()
    if m1=="YES" or m1=="YEs" or m1=="YeS" or m1=="Yes" or m1=="yES" or m1=="yEs" or m1=="yeS" or m1=="yes" or m1=="Y" or m1=="y" or m1=='1':
        m=1
    else:
        print("Thank You")
    print("")
    print("-------------------------------------------------------------")
    print("")
    


# # A5: Write a Python program to calculate area and perimeter of square,rectangle,Rhombus,parallelogram.(Create Two different funtions one for Area and one for Perimeter.)

# In[6]:


def area(ch,*args):
    if ch==1: # Compute Area of a Square
        area = args[0]**2 # Area of a Square = Side * Side
    elif ch==2: # Compute Area of a Rectangle
        area = args[0]*args[1] # Area of a Rectangle = length * Breadth
    elif ch==3: # Compute Area of a Rhombus
        area = 0.5*args[0]*args[1] # Area of a Rhombus = 0.5 * d1 * d2
    elif ch==4: # Compute Area of a Parallelogram
        area = args[0]*args[1] # Area of a Parallelogram = Base * Height
        
    return area # Return Area

def perimeter(ch,*args):
    if ch==1: # Compute Perimeter of a Square
        perimeter = 4*args[0] # Perimeter of a Square = 4 * Side
    elif ch==2: # Compute Perimeter of a Rectangle
        perimeter = 2*(args[0]+args[1]) # Perimeter of a Rectangle = 2*(Length + Breadth)
    elif ch==3: # Compute Perimeter of a Rhombus
        perimeter = 2*((args[0]**2+args[1]**2)**0.5) # Perimeter of a Rhombus = 2*(square root of (d1^2 + d2^2))
    elif ch==4: # Compute Perimeter of a Parallelogram
        perimeter = 2*(args[0] + args[1]) # Perimeter of a Rhombus = 2*(Side1 + Side2)
         
    return perimeter # Return Perimeter.
m=1
while m==1:
    m=0
    print("Enter Your Choice: ")
    print("1.Square \n2.Rectangle \n3.Rhombus \n4.Parallelogram")

    print("------------------------------------------------------------------------------------------------")
    print("Your choice is",end=" ")
    ch=int(input())
    print("------------------------------------------------------------------------------------------------")
    print("")
    
    if ch==1: # Square
        print("You have selected Square.")
        a = float(input("Enter Side of a Square: "))
        x = area(ch,a)
        print("Area of a Square is",x ,"sq.unit")
        y = perimeter(ch,a)
        print("Perimeter of a Square is",y ,"unit")
        print("")
        print("------------------------------------------------------------------------------------------------")
        print("")
        
    elif ch==2: # Rectangle
        print("You have selected Rectangle.")
        a = float(input("Enter Length of a Rectangle: "))
        b = float(input("Enter Breadth of a Rectangle: "))
        x = area(ch,a,b)
        print("Area of a Rectangle is",x ,"sq.unit")
        y = perimeter(ch,a,b)
        print("Perimeter of a Rectangle is",y ,"unit")
        print("")
        print("------------------------------------------------------------------------------------------------")
        print("")

    elif ch==3: # Rhombus
        print("You have selected Rhombus.")
        a = float(input("Enter Length of a 1st Diagonal of Rhombus: "))
        b = float(input("Enter Length of a 2nd Diagonal of Rhombus: "))
        x = area(ch,a,b)
        print("Area of a Rhombus is",x ,"sq.unit")
        y = perimeter(ch,a,b)
        print("Perimeter of a Rhombus is",y ,"unit")
        print("")
        print("------------------------------------------------------------------------------------------------")
        print("")

    elif ch==4: # Parallelogram
        print("You have selected Parallelogram.")
        a = float(input("Enter Length of a Base/Side1 of Parallelogram: "))
        b = float(input("Enter Length of a Side2 of Parallelogram: "))
        c = float(input("Enter Length of a Height of Parallelogram: "))
        x = area(ch,a,c)
        print("Area of a Parallelogram is",x ,"sq.unit")
        y = perimeter(ch,a,b)
        print("Perimeter of a Parallelogram is",y ,"unit")
        print("")
        print("------------------------------------------------------------------------------------------------")
        print("")
    
    else:
        print("OOPS!! Invalid Choice")
        print("Try Again")

    print("")
    print("------------------------------------------------------------------------------------------------")
    print("")
        
    print("Would You like to try again? (Yes/No)",end="")
    m1 = input()
    if m1=="YES" or m1=="YEs" or m1=="YeS" or m1=="Yes" or m1=="yES" or m1=="yEs" or m1=="yeS" or m1=="yes" or m1=="Y" or m1=="y" or m1=='1':
        m=1
    else:
        print("Thank You!! ")
    print("")
    print("------------------------------------------------------------------------------------------------")
    print("")
    


# # A6: Write a function that takes a list of strings an prints them, one per line, in a rectangular frame. For example the list ["Hello", "World", "in", "a", "frame"] gets printed as:
# 
# *********
# * Hello     *
# * World   *
# * in           *
# * a             *
# * frame   *
# *********

# In[7]:


def sframe(n, x, xl, ml):
    for i in range(n):
        print(ch,x[i],end="")
        for j in range(ml-xl[i]-1):
            print(" ",end="")
        print(ch)
    
m=1
while m==1:
    m=0

    x=[] # Empty list for Strings
    xl=[] # Empty list for length of Strings
    n=int(input("Enter Number of String you want to Print:")) # Number of Strings
    ch =input("Enter a Character which is Used for a Boundary:")
    # Take n Strings from users
    for i in range(n): 
        s=input("Enter a string: ") # Take i th String from user
        x.append(s) # Append String in the List x
        xl.append(len(s)) # Append length of String in the List x
    print("List of String:",x) # 
    xm = xl.copy()
    xm.sort(reverse=True)
    ml = xm[0]+2
    #print(ml)
    print("")
    print("---------------------------------------------------------")
    print("")
    for i in range(ml+2):
        print(ch,end="")
    print("")
    sframe(n, x, xl, ml)
    for i in range(ml+2):
        print(ch,end="")
    print("")
    print("")
    print("---------------------------------------------------------")
    print("")
    print("")
    print("-------------------------------------------------------------")
    print("")
    print("Would you like to Try again? (Yes/No): ", end="")
    m1 = input()
    if m1=="YES" or m1=="YEs" or m1=="YeS" or m1=="Yes" or m1=="yES" or m1=="yEs" or m1=="yeS" or m1=="yes" or m1=="Y" or m1=="y" or m1=='1':
        m=1
    else:
        print("Thank You")
    print("")
    print("-------------------------------------------------------------")
    print("")
    


# # Part B

# # B1: Develop a Python Program which prints  cube sum of first n natural numbers (N is user defined)

# In[9]:


m=1
while m==1:
    m=0
    n=int(input("Enter a Natural Number:"))
    if n>0:
        sum=0
        for i in range(n):
            sum+=((i+1)**3)
        print("Using For Loop: Sum of Cube of First ",n," Natural Numbers = ",sum)
        print("Using Formula: Sum of Cube of First ",n," Natural Numbers = ",(n*(n+1)/2)**2)
        
    else:
        print("Input is not a Natural Number") 
    print("")
    print("-------------------------------------------------------------")
    print("")
    print("Would you like to Try again? (Yes/No): ", end="")
    m1 = input()
    if m1=="YES" or m1=="YEs" or m1=="YeS" or m1=="Yes" or m1=="yES" or m1=="yEs" or m1=="yeS" or m1=="yes" or m1=="Y" or m1=="y" or m1=='1':
        m=1
    else:
        print("Thank You")
    print("")
    print("-------------------------------------------------------------")
    print("")
    
    


# # B2: Develop a Python program to print all Prime numbers in a given Interval (Interval values should be user defined)

# In[10]:


m=1
while m==1:
    m=0
    x=int(input("Enter the Lower value: "))
    y=int(input("Enter the Upper value: "))
    if x>y:
        print("Invalid Range!!!")
    else:
        print("")
        print("Following is the list of Prime Numbers in the interval ", x, "and", y,": ")
        if x<2:
            x=2
        c=0
        for i in range(x,y+1):
            for j in range(2,(i//2)+1):
                if i%j==0:
#            print(i,"is not a Prime Number.")
                    break
            else:
                print(i,"is a Prime Number.")
                c=1
        if c==0:
            print("There are no prime numbers in this range.")
    print("")
    print("-------------------------------------------------------------")
    print("")
    print("Would you like to Try again? (Yes/No): ", end="")
    m1 = input()
    if m1=="YES" or m1=="YEs" or m1=="YeS" or m1=="Yes" or m1=="yES" or m1=="yEs" or m1=="yeS" or m1=="yes" or m1=="Y" or m1=="y" or m1=='1':
        m=1
    else:
        print("Thank You")
    print("")
    print("-------------------------------------------------------------")
    print("")
        
        


# # B3: Develop a Python Program which prints factorial of a given number (Number should be User defined)

# In[11]:


def fac(x):
    if x==1:
        return x
    else:
        return (x*fac(x-1))

m=1
while m==1:
    m=0
    print("Let us find the Factorial of a number:")
    x=int(input("Enter the Number: "))
    if x<0:
        print("Factorial is not for negative numbers")
    elif x==0:
        print("Factorial of 0 is 1")
    else:
        print("The factorial of",x,"is a",fac(x))
    print("")
    print("-------------------------------------------------------------")
    print("")
    print("Would you like to Try again? (Yes/No): ", end="")
    m1 = input()
    if m1=="YES" or m1=="YEs" or m1=="YeS" or m1=="Yes" or m1=="yES" or m1=="yEs" or m1=="yeS" or m1=="yes" or m1=="Y" or m1=="y" or m1=='1':
        m=1
    else:
        print("Thank You")
    print("")
    print("-------------------------------------------------------------")
    print("")
    


# # B4: Develop a Python Program to check if a given string is palindrome or not ? (Example for an Palindrome is abcba looks same from both ends)

# In[2]:


m=1
while m==1:
    m=0
    x=input("Enter a string:")
    c=input("Would You like to neglect blank space? (1: Yes / 0: No)")
    if c=="YES" or c=="YEs" or c=="YeS" or c=="Yes" or c=="yES" or c=="yEs" or c=="yeS" or c=="yes" or c=="Y" or c=="y" or c=='1':
        x2 = x.replace(" ","")
        print("You have selected to neglect blank space.")
    else:
        x2=x
        print("You have selected NOT to neglect blank space.")
    x1=x2[::-1]
#    print(x1)
    if x1==x2:
        print("Your String \'", x, "\' is a Palindrome")
    else:
        print("Your String \'", x, "\' is not a Palindrome")
    
    print("")
    print("-------------------------------------------------------------")
    print("")
    print("Would you like to Try again? (Yes/No): ", end="")
    m1 = input()
    if m1=="YES" or m1=="YEs" or m1=="YeS" or m1=="Yes" or m1=="yES" or m1=="yEs" or m1=="yeS" or m1=="yes" or m1=="Y" or m1=="y" or m1=='1':
        m=1
    else:
        print("Thank You")
    print("")
    print("-------------------------------------------------------------")
    print("")
        


# # B5: Develop a python program which print sum of all the Integers in a list (Note  : All the elements must be user defined and list must contain strings also) 

# In[3]:


m=1
while m==1:
    m=0
    x=[]    # Create Empty list
    sum=0   # Initialize sum to Zero
    n=int(input("Enter number of elements you want in a list: ")) 
    for i in range(n):
        z=input("Enter a Number or String: ")
        if z.isdigit(): # if input is an integer then convert input string to integer
            z=int(z)
            sum+=z
        else:
            try: # try an error
                z=float(z) # if input is an float then convert input string to float
            except ValueError: # Catch an error
                z=z #if input is a String.
        x.append(z) # Appending input in the list
    
    print("User defined List: ",x)
    print("The sum of Integers in list is =", sum)
    print("")
    print("-------------------------------------------------------------")
    print("")
    print("Would you like to Try again? (Yes/No): ", end="")
    m1 = input()
    if m1=="YES" or m1=="YEs" or m1=="YeS" or m1=="Yes" or m1=="yES" or m1=="yEs" or m1=="yeS" or m1=="yes" or m1=="Y" or m1=="y" or m1=='1':
        m=1
    else:
        print("Thank You")
    print("")
    print("-------------------------------------------------------------")
    print("")
    


# # B6: Develop a python program which print count of all the type of data in a list (Note  : All the elements must be user defined and list must contain Integers and Strings also)
# 

# In[4]:


m=1
while m==1:
    m=0
    x=[] # Create an Empty List
    y=int(input("Enter number of elements you want in a list: "))
    sc=0 # Counter for String=0
    nc=0 # Counter for Integers=0
    fc=0 # Counter for Float =0
    for i in range(y):
        z=input("Enter a Number or String: ")
        if z.isdigit(): # if input is an integer then convert input string to integer
            z=int(z)
            nc+=1
        else:
            try: # try an error
                z=float(z) # if input is an float then convert input string to float
                fc+=1
            except ValueError: # Catch an error
                z=z
                sc+=1
        x.append(z) # Appending input in the list
    
    print("User defined List: ",x)
    print("Number of Integers in the List = ",nc)
    print("Number of Floating Numbers in the List = ",fc)
    print("Number of String in the List = ",sc)
    print("")
    print("-------------------------------------------------------------")
    print("")
    print("Would you like to Try again? (Yes/No): ", end="")
    m1 = input()
    if m1=="YES" or m1=="YEs" or m1=="YeS" or m1=="Yes" or m1=="yES" or m1=="yEs" or m1=="yeS" or m1=="yes" or m1=="Y" or m1=="y" or m1=='1':
        m=1
    else:
        print("Thank You")
    print("")
    print("-------------------------------------------------------------")
    print("")
    


# # End of Assignment

# In[ ]:




