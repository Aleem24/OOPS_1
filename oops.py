# Class or blueprint or template of something
class Bird:

#Instance attribute of a class
    def __init__(self,name,age):
        self.name = name
        self.age = age

maccow = Bird("Hiramon",11) # Instance or object of the class Bird
print(f"I have a {maccow.name} and it is {maccow.age} years old.")
        