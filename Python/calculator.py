import math
import time
import random

condition = True
while (condition) :
    x=float (input("please enter first number: this will be number 1     :"))
    print ("thank-you")
    z=float (input ("please enter your second number: this will be number 2       :"))
    print ("thank-you")


    op=input("please select a operation +, >,-,*,/,gen,q     gen is a number genarator, q to quit")
    if (op!=">" and op!="<" and op!="-" and op !="+" and op !="*" and op !="/" and op !="x" and op !="gen" and op !="q") :
           print("not recognized")


    if (op=="+") :
            print("you have selected addition" + op)
            time.sleep(1)
            print(x+z)


    elif (op==">" or op=="<" ) :
            print("you have selected comparing" + op)
            time.sleep(1)
            if (x > z):
                    print("number 1 is greater than number 2")
            if (x < z) :
                    print("number 1 is smaller than number 2")
            if (x == z) :
                    print ("number 1 is equal to number 2")

    elif (op=="-"):
            time.sleep(1)
            print("you have selected subtraction" + op)
            time.sleep(1)
            print(x-z)
    elif (op=="*" or op=="x") :
            print("you have selected multiplication" + op)
            time.sleep(1)
            print(x*z)
    elif (op=="/") :
            print("you have selected division")
            print(x/z)
    elif (op=="gen") :
            print("random number genarator")
            time.sleep(2)
            z=int(input("enter the amount of numbers"))
            y=float(input("enter the minimum amount for genarated numbers"))
            a=float(input("enter the maximum amout for genarated numbers"))
            for x in range(z) :
             print(random.randint(y,a))
    elif (op=="q") :
          break
    if (op != "gen") :
            x=float (input("please enter first number: this will be number 1     :"))
            print ("thank-you")
            z=float (input ("please enter your second number: this will be number 2       :"))
            print ("thank-you")




