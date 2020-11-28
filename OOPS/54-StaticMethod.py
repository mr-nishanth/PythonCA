class Car():
    def normal():
        print("Normal Method")

    @staticmethod
    def printed():
        """Static-Method"""
        print("I am Static Method")
Car.printed()
A = Car()
A.printed()
Car.normal()