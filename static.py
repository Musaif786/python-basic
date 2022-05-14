class musaifStatic:
    name="musaif"
    
    @staticmethod        # ye dalne se self likne ke zarurat nahi rahti function me
    def fun1():
        print(f"Good Morning,Musaif")

obj = musaifStatic()
obj.fun1()