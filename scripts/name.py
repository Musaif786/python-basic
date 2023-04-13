#hello
#import gitbash
import os

name = input("Enter folder name : \n ")
localPath = "E:\React-js\clone\react-firebase-chat"
if(name == "react"):
    print(localPath)
    
    code= input("want to pull or push :\n")
    if(code =="pull"):
        #print("git checkout main")
        print("git status")
        #print("git pull")
        #print("successfull")
    elif(code == "push"):
        #print("git add -A")
        print("git status")
    else:
        print("error")
    
elif(name == "python"):
    print("Hello "+ name)
else: 
    print("Please use proper folder")