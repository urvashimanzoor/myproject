class Classs:
    def __init__(self, item):
        self.item = item
    def __getitem__(self, index):
        return self.item[index]
#we are asking getitem fn to return the value for self.item using storage of index
Objectt = Classs("hello")
#now instantiating object with parameter for index as hello
#further print the value at mentioned indexes - note that [] used for __getitem__
#so it's calling getitem fn to yield results
print(Objectt[0])
print(Objectt[1])
print(Objectt[2])
print(Objectt[3])
print(Objectt[4])
#OR
Objecttt = Classs([1, 2, 3])
print(f"First item: {Objecttt[0]}")
print(f"Second item: {Objecttt[1]}")
print(f"Third item: {Objecttt[2]}")
# Output:
# First item: 1
# Second item: 2
# Third item: 3


class Toy():
  def __init__(self, color, age):
    self.color = color
    self.age = age
    self.my_dict = {
         'name':'Yoyo',
         'has_pets': "ook",
     }

  def __str__(self):
    return f"{self.color}"

  def __len__(self):
    return 5

  def __del__(self):
    return "deleted"

  def __call__(self):
      return('yes??')

  def __getitem__(self,i):
      return self.my_dict[i]
      #here I am defining that we are going to create a space for one variable using i
 #here I my_dict is assigned to my variable that is now that data of my_dict  is stored in my variable
  #we are using [] these instead of () here as () means calling nd my_dict is an object
  # and we can't call it, we just want to assign value so we are using [] for that.


action_figure = Toy('red', 0)
print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
print(action_figure())
print(action_figure["name"])
#here we are getting an option to call anyone of the keys of my_dict as that is it will give
# the value present in my_dict for the respective key
#the benefit of __getitem__  is that we are able to call the __getitem__ fn as [] index operator
#and then passing the arguments required for fn if any within []
#x[i] is roughly equivalent to type(x).__getitem__(x, i) where [] is index operator
#since it is just for giving the value at index so we cant ask for multiple values together
#note it is not that we are giving any value we are just asking for information that is already stored
# in fn.

#__getitem__ method is used to get an item from the invoked instances’ attribute. __getitem__ is commonly used with containers like list, tuple, etc.

#__setitem__ method is used to set the item into a specific index of the invoked instances’ attribute.
# Similar to __getitem__, __setitem__ is also used with containers.

class SetItemExample:
    def __init__(self, item):
        self.item = item
    def __setitem__(self, index, item1):
        self.item[index] = item1
#the one index var is for asking which index to change and item1 var for the value to which we have
# to change
setitem_instance = SetItemExample([1, 2, 3])
#setitem_instance - object , argument given to class is a list [1,2,3]
print(f"Items before setting: {setitem_instance.item}")
setitem_instance[1] = 5
#changed the item at index 1 to 5
print(f"Items after setting: {setitem_instance.item}")
# Output
# Items before setting: [1, 2, 3]
# Items after setting: [1, 5, 3]