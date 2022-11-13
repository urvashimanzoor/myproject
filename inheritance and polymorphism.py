class Issue:
    def speak(self):
        print("Don't change me")
    def attack(self):
        print("Main User")
class Derived(Issue):
    def __init__(self,name,power):
        self.name=name
        self.power=power
    def attack(self):
        #Issue.attack(self)
        #if we want to use the same self as that of the Issue class within this class and don't want to overwrite it
        # with the function given within the class
        print(f"Done with inheritence {self.name} with {self.power}W")
class Derived2(Issue):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def attack(self):
        print(f"Done with polymorphism {self.name} in {self.age}")

p1 = Derived("Urva","500")
p2 = Derived2("Urvi",24)
p = Issue()
p.attack()
#here attack method is called using p object which belongs to Issue class(parent) so behaving like that
p1.speak() #inherited fn
p1.attack()
#here attack method is called using p1 object which belongs to Derived class so behaving like that
# even it's not considering the inhertied fn attack as it has its own defined
p2.speak() #inherited fn
p2.attack()
#here attack method is called using p2 object which belongs to Derived2 class so behaving like that
#even it's not considering the inhertied fn attack as it has its own defined
print("*"*200)
print(isinstance(p1, Issue))
print(isinstance(p1, Derived))
print(isinstance(p1, object))