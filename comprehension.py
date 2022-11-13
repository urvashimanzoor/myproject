#Without condition: for every value in iterable do this action
#with condition: if the condition mets, then for every value in iterable do this action
#variable= {/[action to be taken on value for every parameter in iterable if condition
my_dict = {num:num*2 for num in [1,2,3]}
print(my_dict)

simple_dict={
    "a":1,
    "b":2
}
my_dict1={key:value**2 for key,value in simple_dict.items()if value%2==0}
print(my_dict1)

my_list=[1,2,3]
my_list3=[num**2 for num in my_list if num%2!=0]
print(my_list3)


some_list=['a','b','c','b','d','m','n','n']
# duplicates=[]
# for alphabet in some_list:
#     if some_list.count(alphabet)>1:
#         if alphabet not in duplicates:
#             duplicates.append(alphabet)
# print(duplicates)
duplicates1= list({value for value in some_list if some_list.count(value)>1})
#used{} as it will return as set and in set there is no duplicate value
#used list since we need answer in list
print(duplicates1)