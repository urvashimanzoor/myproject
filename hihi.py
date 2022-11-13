class Cat:
    species = 'mammal'  # Classobject attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age


Cat1 = Cat('Lussy', 12)
Cat2 = Cat('Simba', 13)
Cat3 = Cat('Limo', 15)


def CheckAge(*args):
    return max(args)


print(f"The oldest cat is {CheckAge(Cat1.age, Cat2.age, Cat3.age)} years old.")
