import math

#I developed it using methods, because it is little complicated....
# Variables s, st ------ there are strings for any moments or param to functions
# Variables x and for example y,z,n,i  etc. - there are numeric
# important variables - P,A,r,t - for investment and P,i,n,R - for bond


def InputCalcType():
#On this method we input calc type
#while loop returns only two values - from calc set

    calc = ("bond","investment")
    print("investment - to calculate the amount of interest you'll earn on your investment")
    print("bond - to calculate the amount you'll have to pay on a home loan")
    set_calc = ""
    while True:
        set_calc = input("Enter either 'investment' or 'bond' from the menu above to proceed:").lower()
        if set_calc in calc:
            return (set_calc)
        else:
            print("Improperly value")

def InputNumberInt(s):
#Input  and check int - param - information string - for example :" How many years......".
#In this way we can use this functiom im many situations
    while True:
        try:
            x = int(input(s))
            return (x)

        except ValueError:
            print("Improperly value - only int..")

def InputNumberFl(s):
#Function returns float only when value is properly -
# param - information string - for example : "Write your deposit...."
#In this way we can use this functiom im many situations
    while True:
        try:
            x = float(input(s))
            return (x)

        except ValueError:
            print("Improperly value - only float..")

def InputStrToBool(s):
    # Function returns bool from "yes"/"no" - checks values..
    #parans - info-string

    while (True):

        st = input(s).lower()

        if st==("yes"):
            return True
        if st==("no"):
            return False
        print("Improperly value - only yes/no")

def InvestCalculating():
    # Invest  calculating - string variables aren't important - I use that only for moment...
    # important variables - P, r, t, simple
    # I got and check input variables on other methods... -

    A=0
    x=0
   # //------------------------------------------------
    s="The amount of money that they are depositin - float"
    P = InputNumberFl(s)
    s = "Value P is:" + str(P)
    print(s)

    #//----------------------------------------------
    s = "The interest rate (as a percentage). Only the number of the interest - float"
    x = InputNumberFl(s)
    r=x/100
    s = "Value r is:" + str(r)
    print(s)
   # //------------------------------------------------------------------------
    s = "The number of years they plan on investing - int."
    t = InputNumberInt(s)
    s = "Value t is:" + str(t)
    print(s)

    #-------------------------------------------------------------------------

    s = "Do you want more simple calculating? "
    simple=InputStrToBool(s)

    try:
        if simple == True:
            A = P * (1 + r * t)

        if simple == False:
            A = P * math.pow((1 + r), t)
        s = "Result of investment calculating is: " + str(A)
        print(s)

    except :
        print("Improperly values - please - run nex time with other values... .")



def BondCalculating():
    #Bond calculating - string variables aren't important - I use that only for moment...
    # important variables - P, i, n, R
    # I got and check input variables on other methods... -

    R=0
   # //------------------------------------------------
    s="The present value of the house. - int"
    P = InputNumberInt(s)
    s = "Value P is:" + str(P)
    print(s)

    #//----------------------------------------------
    s = "The interest rate (as a percentage). Only the number of the interest - float"
    i = InputNumberFl(s)
    i=i/100
    #print(r)
    i=i/12
    s = "Value i is:" + str(i)
    print(s)

   # //------------------------------------------------------------------------
    s = "The number of months they plan to take to repay the bond - int."
    n = InputNumberInt(s)
    s = "Value n is:" + str(n)
    print(s)

    #-------------------------------------------------------------------------

    try:
        R = (i * P)/(1 - (1 + i)**(-n))
        s = "Result of bond calculating is: " + str(R)
        print(s)

    except :
        print("Improperly values - please - run nex time with other values... .")




#------------------------------------------------------------------------------------------
############################################################################################
##############################################################################################
#Main part of code
#We set check calc type and go to function - depending on the bond or investment
#Inside this functions we go to smaller functions....
calc = InputCalcType()
s = "You selected option: " + calc
print(s)
if calc=="investment":
    InvestCalculating()
if calc=="bond":
    BondCalculating()






