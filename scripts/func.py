#python function practice

def demo_fun():
    print("hello musaif i am function")
	
demo_fun()

def my_function(firstname="md"):
  print(f"My name is {firstname } Musaif")

#my_function()

def args_func(*names):
    print(f"my name is {names[3]}")
    
#args_func("Musaif","amir","khan","manohar")

def my_function(*kids):
  print("The youngest child is " + kids[2])

#my_function("Emil", "Tobias", "Linus")


#this below fun is loop

def loop_fun(names):
    for x in names:
        print("List of names " + x)
        
#names=["Mohammed","Musaif","Noman","Manohar"]
names={"apple", "banana", "cherry"}
loop_fun(names)

# fun ke under fun

def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

# about list, tiple,set and string

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("musaif")
print(type(thistuple))

thistuple = {"me"}
print(type(thistuple))

thistuple = ["me"]
print(type(thistuple))

""" Output

class 'tuple'>
<class 'str'>
<class 'set'>
<class 'list'>

"""