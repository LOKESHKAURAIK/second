#join method creates a string from itrable objects

from lib2to3.pytree import type_repr


l = ["hi" , "hello" , "good" , "morning"]
sentance = " and ".join(l)
print(sentance)
print(type(sentance))