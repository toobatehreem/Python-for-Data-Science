#tuples

rating = (0, 5, 2, 7, 8, 3)
print(rating)

ratings = rating
print(ratings)
ratings = sorted(rating)
print(ratings)

num = (0 ,3, ("Hello", "World"), 9 , ("Pop", "up"))
print(num[2][1])

#list

name = ["Tooba", "Tehreem", 4, 7, "Sheikh"]
print(name[1:3])
name[1] = "toobay"
print(name)

names = name + ["Aliya" , "Khan"]
print(names)
names.append("Hello") #adds only one element
print(names)
names.extend(["Yo", "Bro"]) #can add multiple elements
print(names)
names[3] = "Disco"
print(names)

del names[3]
print(names)
names.remove("Bro")
print(names)
names.pop(2)
print(names)
names.append("Hard rock")
print(names)

"Hard rock".split(",") #using delimiter
print(names)
hello = ["Hard Rock"]
print(hello)

#Aliasing # changes elements in B if we change elements in A
A = ["hard", 'rock', 4]
print(A)
B = A
print(B)
A[0] = "banana"
print(A)
print(B)
 #cloning #does not change elements in B if we change elements in A , makes a new copy
C = ["hard", 'rock', 4]
D = C[:]
print(C)
print(D)
C[0] = "banana"
print(C)
print(D)

#print(help(C))


#dictionaries

dict = {1 : "Hello", 2: 'world'}
print(dict)
for keys in dict.keys():
    print(keys)
for items in dict.items():
    print(items)
for values in dict.values():
    print(values)
print(dict[2])
dict["Graduation"] = '1987'
print(dict)
del(dict[2])
print(dict)
print('Graduation'in dict) #returns if element is present in the dictionary or not

#sets

name = ["tooba", "Tehreem", "sheikh", "Sheikh"]
sets = set(name)
print(sets)

sets.add("Hello")
sets.remove("Sheikh")
print(sets)
print("Tehreem" in sets)

#to find the intersection of two sets use &

A = {"tooba", "Tehreem", "sheikh", "Sheikh"}
B = {"Tooba", "sheikh", 3, 2}
print(A & B)

#to find the union of two sets use .union()

print(A.union(B))
# to find if a set is a subset of other
C = {"tooba", "sheikh"}
print(C.issubset(A))

#using reverse function on a list

lists = [3, 6,1 ,4,5,6,8]
print(lists.reverse())