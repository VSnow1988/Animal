class Animal():
    def __init__(self,name,health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def displayhealth(self):
        print self.health
        return self

#Test
Animal("Giraffe", 77).walk().walk().walk().run().run().displayhealth()

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__()
        self.health = 50
    def pet(self):
        self.health += 5
        return self


#Test
Dog().walk().walk().walk().run().run().displayhealth()

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__()
        self.health = 150
    def fly(self):
        self.health -= 10
        return self
    def displayhealth(self):
        super().displayhealth()
        print "I am a Dragon!"
        return self

#Test
Dragon().fly().walk().displayhealth()
