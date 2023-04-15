import subprocess
import os

path1 = 'E:\Python'
path2 = 'E:\\React-js\\clone\\reactFirebase'
#path2=os.chdir('E:\React-js\clone\reactFirebase\src')


word = input("react (r) or python(p) or newrepo(n) :\n")


if(word =="react" or word =="r"):
    pwd = path2

elif(word == "python" or word =="p"):
    pwd = path1
    #link=prodlink

elif(word == "newrepo" or word == "n"):
    addpath = input("Your path here :\n ")
    pwd = addpath
    #url=input("ur repo url :\n")
    #link=prodlink
    
word1 = input("pull(pl) or push(ph) or status(s) :\n")
if(word1 == "pull" or word1 == "pl"):
    subprocess.run(['git','checkout','master'], cwd=pwd)
    subprocess.run(['git','pull'], cwd=pwd)
    #subprocess.run(['git','checkout','musaifbranch'], cwd=pwd)
    subprocess.run(['git','merge','master'], cwd=pwd)
    subprocess.run(['git','status'], cwd=pwd)
    print("successfully merge")
    print("executed the code")
elif(word1 == "push"  or word1 == "ph"):
    #subprocess.run(['git','checkout','master', 'or', 'main'], cwd=pwd)
    subprocess.run(['git','add','-A'], cwd=pwd)
    subprocess.run(['git','commit','-m"initial changes added "'], cwd=pwd)
    subprocess.run(['git','push'], cwd=pwd)
    print("successfully push the code to repo")
    
elif(word1 == "status" or word1 == "s"):
    #subprocess.run(['git','init'], cwd=pwd)
    #subprocess.run(['git','commit','-m"initial changes added "'], cwd=pwd)
    #subprocess.run(['git','branch','-M','main'], cwd=pwd)
    #subprocess.run(['git','remote','add','origin',url], cwd=pwd)
    #subprocess.run(['git','push','-u','origin','master'], cwd=pwd)
    subprocess.run(['git','status'], cwd=pwd)
    print("status of given repo")
else:
    print("something happened pls try again ...")