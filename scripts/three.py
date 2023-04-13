class khan():
    def __init__(self,name,address):
        self.name = name
        self.address = address
        
    def displayName(self):
        print(f"My name is {self.name } and My Address is {self.address}")
        
    def setName(self,name,address):
        self.name = name
        self.address = address
        