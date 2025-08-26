class Rektangel:
    def __init__(self, längd, bredd):
        self.längd = längd
        self.bredd = bredd
        
    def area(self):
        return self.längd * self.bredd
        
    def omkrets(self):
        return 2 * (self.längd + self.bredd)
        
fyrkant = Rektangel(4, 7)


print(fyrkant.area())
print(fyrkant.omkrets())