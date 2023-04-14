#Python code for reversestring or palidrome

print("Welcome to Musaif coding world")

def palidromeFun():
    s = input("Enter value to know it is palidrome or not\n :")
    UserInput = s.lower() 

    if UserInput == UserInput[::-1]:
        print(UserInput, "Yes given name is palidrome: ")
    
    else:
        print(UserInput,"Not a palidrome")
    
    
    
def loopFun():
    print("Reversing the string: \n")
    name1 = input("enter the string which your trying to reverse:\n")
    name = name1[::-1]
    print("Reverse of your value is : ",name)
    
    
    
loopFun()
palidromeFun()