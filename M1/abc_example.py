from abc import ABC, abstractmethod
class Human(ABC):
    def __init__(self, name):
        self.name = name

    def say(self):
        return f"Hell my name is {self.name}"
    @abstractmethod
    def help_person(self):
        return "Good"

class MixinDriver():
    def drive_car(self):
        return "Driving"

class Ruslan(Human, MixinDriver):
    def teaching_python(self):
        return "Well"
    
    def help_person(self):
        return "I am here to help"

m_d = MixinDriver()
# a = Human()
r = Ruslan("Ruslan")
print(r.drive_car())
print(r.help_person())
