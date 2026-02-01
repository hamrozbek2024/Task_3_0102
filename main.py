class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

class Cow(Animal):
    def speak(self):
        print("Cow moos")

class Bird(Animal):
    def speak(self):
        print("Bird sings")


animal = Animal()
dog = Dog()
cat = Cat()
cow = Cow()
bird = Bird()

animal.speak()
dog.speak()
cat.speak()
cow.speak()
bird.speak()
