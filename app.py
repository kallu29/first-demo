class caluculator():
    def __init__(self,a=1,b=1):
        self.a=a
        self.b=b
    def addition(self):
        return self.a+self.b
    def subtraction(self):
        return self.a-self.b
    def multiplication(self):
        return self.a*self.b
obj=caluculator(a=20,b=20)
print(f"addition of a and b are:{obj.addition()}")
