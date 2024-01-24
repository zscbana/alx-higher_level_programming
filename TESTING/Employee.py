class Employee:
    def __init__(self, name, age, id, rate):
        self.name = name
        self.age = age
        self.id = id
        self.rate = rate # if rate <3 it's greate 

    def Rating(self):
        if self.rate > 3 :
            return "Excellent!"
        else:
            return "BAD"