class musaif:
    name = "Mohammed Musaif"

    def __init__(self):
        print("hello! i'm Constructor")

    @staticmethod
    def fun1():
        print("Im  static function")

obj = musaif()
obj.fun1()

''' For constructor we no need to call its function just by creating obj its automatically run and constructor syntax __init__(self)
'''