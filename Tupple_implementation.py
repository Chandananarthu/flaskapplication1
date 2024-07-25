"""Functions that can be used for both lists and tuples:

len(), max(), min(), sum(), any(), all(), sorted()

count(), Index()Tuples can be stored in lists.Lists can be stored in tuples.Both ‘tuples’ and ‘lists’ can be nested.Methods that cannot be used for tuples:

append(), insert(), remove(), pop(), clear(), sort(), reverse()we generally use ‘tuples’ for heterogeneous (different) data types and ‘lists’ for homogeneous 
(similar) data types.Iterating through a ‘tuple’ is faster than in a ‘list’.‘Lists’ are mutable whereas ‘tuples’ are immutableMethods that cannot be used for tuples:

append(), insert(), remove(), pop(), clear(), sort(), reverse()we generally use ‘tuples’ for heterogeneous (different) data types and ‘lists’ for homogeneous (similar) 
data types.Iterating through a ‘tuple’ is faster than in a ‘list’.‘Lists’ are mutable whereas ‘tuples’ are immutable.."""
tupple=(1)
print(tupple)


Tuple1 = ('Geeks')
a=type(Tuple1)
print(a)
n = 5
print("\nTuple with a loop")
for i in range(int(n)):
    Tuple1 = (Tuple1,)
    print(Tuple1)

Tuple1 = ('Geeks',)
n = 5
a=type(Tuple1)
print(a)
print("\nTuple with a loop")
for i in range(int(n)):
    Tuple1 = (Tuple1,)
    a=type(Tuple1)
    print(a)
    print(Tuple1)

Tuple1 = ('Geeks')
n = 5
a=type(Tuple1)
print(a)
print("\nTuple with a loop")
for i in range(int(n)):
    Tuple1 = (Tuple1,)
    a=type(Tuple1)
    print(a)
    print(Tuple1)
    """we cant append elemts in tuple inorder to intialize it we have do following way:
"""
elements = ()
for i in range(1, 6):
    elements += (i,)  

print(elements)  

elements = ()
for i in range(1, 6):
    a=input()
    elements += (a,)  

print(elements) 
