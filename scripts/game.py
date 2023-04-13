#Small game
print("Hello guys Welcome to Musaif Gaming\n\n")
name=input("Want to play a game yes or no :\n ")
if name.lower() != "yes" :
    quit()
    
print("Okey! lets play")

answer = input("CPU stand for ?\n")
if answer == "central processing unit":
    print("correct")
else:
    print("ops! sorry it's wrong")