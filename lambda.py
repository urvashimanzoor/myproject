from functools import reduce
my_list =[5,4,3]
new_list=list(map(lambda x:x**2, my_list))
print(new_list)

a=[(0,2),(4,-87),(10,-1),(9,-9)]
a1=[(0,2),(4,3),(10,-1),(9,9)]
a.sort(key=lambda x:x) #for sorting through first digit of tuple in list (a)
a1.sort(key=lambda x:x[1]) #for sorting through second digit of tuple in list (a) we use index [1]
#print(list(map(lambda x: for i,j in x: j.sort(), a)))
print(a)
print(a1)

print(list(filter(lambda item:item%2!=0, my_list)))

print(reduce(lambda acc,item: acc+item, my_list ,4))
print(reduce(lambda acc,item: acc+item, my_list))
#taking 4 as the first value for acc else 0 by default