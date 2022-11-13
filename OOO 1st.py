class DecoratorExample:
    """ Example Class """

    def __init__(self):
        """ Example Setup """
        print('Hello, World!')
        self.name = 'Decorator'
        self.age = 21

    # def example_function(self):
    #     """ This method is an instance method! """
    #     print('I\'m an instance method!')
    #     print('My name is ' + self.name)
        print(f'My name is {self.name} and age is {self.age}')


de = DecoratorExample()
#de.example_function()
