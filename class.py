class musaif:
    # instance bolte below name and salary ko
    name = "md musaif"
    salary = 25000


# class ka object hai ye below one like java me kaisa rhata waisa he
obj = musaif()
n = obj.name
if(obj.salary > 20000):
   print(f"My Name is {n.upper().replace(' ','_')}")
   print(obj.salary)
else:
   print("Salary is less then 25K")
