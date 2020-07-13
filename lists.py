mylist = [
    1,
    2,
    3,
]
mylist.append(4)
# print(mylist.count(1))
# print(mylist.pop())
mylist.reverse()
mylist.sort()

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
first_column = [row[2] for row in matrix]
print(first_column)