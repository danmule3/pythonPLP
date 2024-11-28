#Define a class
class Gadget:
   def __init__(self, color, model):
        self.color = color    # Instance variable
        self.model = model    # Instance variable

    # Creating objects with unique attributes
smartphone = Gadget("blue", "Samsung")
laptop = Gadget("Green", "HP-probook")
tv = Gadget("Black", "TCL")
dispenser = Gadget("Grey", "nunix")
    
print(smartphone.color)  # Output: 
print(tv.model)  # Output: SUV
    
class Radio(Gadget):
    pass
    
radio = Gadget("Orange", "Pioneer")

print(radio.color)

class SecretStash:
    def __init__(self):
        self.__chicken = -1  # Private attribute

    def take_chicken(self):
        if self.__chicken < 0:
            self.__chicken += 1
            print("One chicken added!")
        else:
            print("No chicken left 😢")

stash = SecretStash()
stash.take_chicken()

    
    
#Activity 2
class Jet:
    def fly(self):
        return "Flies Fastest!"

class Helicopter:
    def fly(self):
        return "Flies Fast!"

class Plane:
    def fly(self):
        return "Flies Faster!"

# Polymorphism in action
for airplane in [Jet(), Helicopter(), Plane()]:
    print(airplane.fly())