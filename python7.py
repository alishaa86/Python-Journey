# TUPLE

t = (3,8,9,2,1,6,3)
print(t.count(1))
print(t.index(3))

# SET

a = {3,7,9,3,7,54}
a2 = {83,9,82,65}
# print(a.clear())
# print(a.pop())
# a.add(2)
# a.union(a2)
print(a.intersection(a2))
print(a)
print(a2)

# DICTIONARY

dict = {}
print(type(dict))

dict1 = {"hey": "how are you python?",
          "1": "hope you are fine"}

print(dict1)
print(dict1["hey"])
print(dict1["1"])
dict1["python"]="i am good"
print(dict1)
print(dict1.keys())
print(dict1.values())
