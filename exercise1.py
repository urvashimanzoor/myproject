class Pets():
    animals = [] #class object attribute
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True #class object attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Simba(Cat):
    def sing(self, sounds):
        return f'{sounds}'

#2 Create a list of all of the pets (create 3 cat instances from the above)
# Cat1 = Simon("Simon",24)
# Cat2 = Sally("Sally",23)
# Cat3 = Simba("Simba",21)
# my_cats = [Cat1.walk(), Cat2.walk(), Cat3.walk()]
#Instead of above 4 lines, we can use single statement but above in walk fn of Pets class we have to
#add .walk in for loop (print(animal.walk())
my_cats = [Simon('Simon', 4), Sally('Sally', 21), Simba('Simba', 1)]


#3 Instantiate the Pet class with all your cats use variable my_pets
my_pets = Pets(my_cats)

#4 Output all of the cats walking using the my_pets instance
my_pets.walk()