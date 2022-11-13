# INSTANCE MENTHOD
class Urva:
    def __init__(self, num1, num2):
        self.subjects = ["Maths", "English", "Science"]
        self.skills = ["C++", "Python", "Javascript"]
        self.num1 = num1
        self.num2 = num2
        self.num = num1 + num2
        # We have to initalise all the attributes/parameters in this init fn only they cant be initialised in any other fn

    def learn(self):
        print(f"I love {self.subjects} and {self.skills}")

    def life(self):
        print(f'My age is {self.num} and I like {self.subjects}')

    # we are using the parameter declared in init fn
    @classmethod
    def instantiating_now(cls):
        return cls(9, 90)
#now we want to instantiate the object without disturbing init fn and for that we will use return keyword
#and use cls for that -(like self) and provide arguments for the parameters defined in init fn

hey = Urva.instantiating_now()
print("hello" + " " + str(hey.num))
#we are creating an object and placing the value where fn's arguments might be saved
#then we print the string and use the num attribute defined in init.
happy = Urva(2, 3)
# we have to give arguments while we are initiating the object if we haven't given values in init fn
happy.learn()
happy.life()









print("=" * 150)









# DECORATOR ("@static method")
class Urvi:
    def __init__(self):
        self.subject = ["Maths", "Biology", "Network"]
        self.skill = ["CCNA", "Routing", "Switching"]

    def learns(self):
        print(f"I love {self.subject} and {self.skill}")

    @staticmethod
    # No concern with rest of the class now , can't access its data - in isolation
    def lifes(num1, num2):
        num = num1 + num2
        print(f'My age is {num}')
    @classmethod
    def new_one(cls):
        return cls()
so=Urvi.new_one()
print(so)
#here we have just created an object with no arguments or values, just an empty object created using cls

lives = Urvi.lifes(4, 3)
# lives=Urvi()
# lives.lifes(4,5)
# calling the fn - its obj = class  .  [static fn name lifes](arguments for parameters if any)
happy = Urvi()
happy.learns()




print("=" * 150)







# OR
class uu:
    @staticmethod
    def lets():  # without parameeters
        a = "hi"  # giving value
        b = "Why"  # giving val
        print(f'My concern is {a} {b}')

    # loo = uu.lets() # calling
    # we ideally call the static method like the above line.
    # other than this, we can call the static method using class method too

    # DECORATOR ("@class method")
    @classmethod
    def eg(cls):
        print("Class Method:done")
        cls.lets()  # calling the static method lets by using cls
        # it cant be done by simple function just the class method


# ipo=uu()
# ipo.eg()
ipo = uu.eg()
# calling the fn - its obj = class (uu) .  [static fn name eg](arguments for parameters if any)
# Note that both class and static method can be done eitherway
# calling the class method with the object but will also process the static method
# since that is defined within the class method

# class new():
#     @classmethod
#     def instantiating_now(cls, p, q):
#         return p+q
#
# hey=new.instantiating_now(4,9)
# print(f"hello {hey}")
print("=" * 80 + "DONE" + "=" * 90)
