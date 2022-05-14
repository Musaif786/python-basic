class musaif:
    name = "Mohammed Musaif"

    def __init__(self):
        print("hello! i'm Constructor")

    def __init__(self, name, salary ):
        print(f"My name is {name} and salary is  {salary}")

obj = musaif("musaif", 30000)


'''if we have more then 1 constr.. then it will take last one'''