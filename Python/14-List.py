marks = [95, 98, 97]
print(marks[1])
print(marks[2])
print(marks[0])
print(marks[-1])
print(marks[-2])
print(marks[-3])
print(marks[0:2])
print(marks[1:3])

#For Loop on List
for score in marks:
    print(score)

# Operations on List
marks.append(99)
print(marks)

marks.insert(0, 99)
print(marks)

print(99 in marks)
print(93 in marks)

print(len(marks))

# While Loop on List

i = 0
while i < len(marks):
    print(marks[i])
    i = i + 1

marks.clear()
print(marks)