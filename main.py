from fastapi import FastAPI
import uvicorn

app = FastAPI()

class Animal:
    # Encapsulation
    def __init__(self, name):
        self.__name = name

    # Encapsulation
    def get_name(self):
        return self.__name

    def make_sound(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Inheritance
class Dog(Animal):
    #Polymorphism
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    #Polymorphism
    def make_sound(self):
        return "Meow!"

@app.get("/")
async def root():
    dog = Dog("Bob")
    dog1 = Dog("Toro")
    cat1 = Cat("Whis")
    cat = Cat("Tom")
    return {"dog1_name": dog.get_name(), "dog1_sound": dog.make_sound(),
            "cat1_name": cat.get_name(), "cat1_sound": cat.make_sound(),
            "dog2_name": dog1.get_name(), "dog2_sound": dog1.make_sound(),
            "cat2_name": cat1.get_name(), "cat2_sound": cat1.make_sound()}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

# http://localhost:8000/
#In the provided code, the concepts of Inheritance, Encapsulation, and Polymorphism are demonstrated as follows:
#Inheritance: class Dog(Animal):: This line indicates that the Dog class inherits from the Animal class. Inheritance is a fundamental principle of object-oriented programming where a new class (subclass) can inherit attributes and methods from an existing class (superclass). In this case, Dog and Cat inherit the __init__, get_name, and make_sound methods from the Animal class.
#Encapsulation: self.__name = name: The use of __name with double underscores indicates that __name is a private attribute of the Animal class. Encapsulation is the concept of bundling the data (attributes) and methods (functions) that operate on the data into a single unit (class) and controlling access to that unit. By making __name private, access to it is restricted to methods within the Animal class, enforcing encapsulation.
#Polymorphism:def make_sound(self):: The make_sound method is defined in the Animal class but raises a NotImplementedError, making it an abstract method. Polymorphism is the ability of different classes to be treated as instances of the same class (superclass) and to have their own unique implementations of methods. In this case, both Dog and Cat have their own implementations of the make_sound method, demonstrating polymorphism.
#Overall, this code demonstrates the use of object-oriented principles in a FastAPI application, showcasing how classes can inherit from each other, encapsulate data, and exhibit polymorphic behavior.
