# loop
for i in range(1,31):
    if (i % 3 == 0):
        print(i )

# List
marks = [20,30,40,50,60,70]
print(marks[-1])
print(marks[-3:])

for score in marks:
    print(score)

#append
marks.append(60)
print(marks)
#insert
marks.insert(1,10)
print(marks)

#check

print(100 in marks)


#check length
print(len(marks))

#clear the list
marks.clear()
print(marks)

