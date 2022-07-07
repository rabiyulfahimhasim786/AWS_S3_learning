
#from functools import reduce
#print(content.items())
#print(content.values())
#list(reduce(lambda x, y: x + y, content.items()))
#a = list(reduce(lambda x, y: x + y, content.items()))
#print(a[1])
a = 'foldername/subfoldername/filename.format'
Prefix='foldername'
key = f"{Prefix}/{a}"
key1 = a
print(key1)
#reference for formatting
age = 18
message = f"You are {age} years old"
print(message)